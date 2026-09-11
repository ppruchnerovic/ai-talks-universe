#!/usr/bin/env bash
# The whole refresh, on the machine that has the keys.
#
#     tools/refresh_local.sh                 # refresh, fetch up to 300 transcripts, push a PR
#     tools/refresh_local.sh --limit 50      # spend at most 50 Supadata credits
#     tools/refresh_local.sh --no-transcripts
#     tools/refresh_local.sh --dry-run       # print the plan, touch nothing
#
# Why this exists: the GitHub Actions refresh could enumerate but never
# enrich (no key in the repo's secrets) and by design never fetched
# transcripts (YouTube meters captions per IP and blocks cloud ranges). Both
# keys live on this machine, so this is where the chain runs, daily, from the
# systemd timer in tools/systemd/ (see install_refresh_timer.sh).
#
# Keys are read from $ATU_ENV_FILE, default ~/.config/ai-talks-universe/env,
# a `KEY=value` file with mode 600 that a timer can read and a shell profile
# never is:
#
#     YOUTUBE_API_KEY=...       descriptions and dates (free tier)
#     SUPADATA_API_KEY=...      transcripts from any network (credits)
#
# What it does, and where it stops:
#
#   1. refuses a dirty tree, a second concurrent run, or a missing key
#   2. check_registry.py
#   3. sync_catalog.py --refresh, enrich.py for this year, sync_catalog.py
#   4. fetch_transcripts.py --source supadata for this year, capped by --limit
#   5. sync_catalog.py, build_index.py
#   6. refresh_report.py — exit 2 (a field lost coverage, the throttled-
#      enumeration signature) aborts the run and resets the tree
#   7. the offline test suites
#   8. commit to refresh-YYYY-MM-DD, push, open a pull request with the
#      report as its body. Merging is the human gate; it triggers pages.yml.
#
# A run that changes nothing exits 0 with no commit. Everything is logged to
# logs/refresh-YYYY-MM-DD.log (gitignored); the last lines are the summary.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TOOLS="$ROOT/tools"
PY="$TOOLS/.venv/bin/python"; [ -x "$PY" ] || PY=python3
LIMIT=300
TRANSCRIPTS=1
DRY=0
ENV_FILE="${ATU_ENV_FILE:-$HOME/.config/ai-talks-universe/env}"
YEAR="$(date +%Y)"
TODAY="$(date +%F)"
BRANCH="refresh-$TODAY"
LOCK="$ROOT/logs/refresh.lock"
LOG="$ROOT/logs/refresh-$TODAY.log"
REPORT="$ROOT/logs/refresh-$TODAY-report.md"

while [ $# -gt 0 ]; do
  case "$1" in
    --limit) LIMIT="$2"; shift 2 ;;
    --no-transcripts) TRANSCRIPTS=0; shift ;;
    --dry-run) DRY=1; shift ;;
    -h|--help) sed -n '2,40p' "$0"; exit 0 ;;
    *) echo "unknown option: $1" >&2; exit 2 ;;
  esac
done

mkdir -p "$ROOT/logs"
exec > >(tee -a "$LOG") 2>&1
echo "== refresh_local.sh $TODAY (limit $LIMIT, transcripts $TRANSCRIPTS, dry-run $DRY)"

run() {                       # print, then run unless --dry-run
  echo "+ $*"
  [ "$DRY" = 1 ] || "$@"
}

# ---- 1. preconditions ------------------------------------------------------
if [ -f "$ENV_FILE" ]; then
  set -a; . "$ENV_FILE"; set +a
fi
if [ -z "${YOUTUBE_API_KEY:-}" ]; then
  echo "YOUTUBE_API_KEY is not set (looked in $ENV_FILE). Without it enrich.py"
  echo "falls back to a yt-dlp extraction per video, hours long and IP-hostile." >&2
  exit 2
fi
if [ "$TRANSCRIPTS" = 1 ] && [ -z "${SUPADATA_API_KEY:-}" ]; then
  echo "SUPADATA_API_KEY is not set (looked in $ENV_FILE); pass --no-transcripts to skip." >&2
  exit 2
fi
command -v gh >/dev/null || { echo "gh (GitHub CLI) is required to open the pull request" >&2; exit 2; }
command -v yt-dlp >/dev/null || { echo "yt-dlp must be on PATH for enumeration" >&2; exit 2; }

cd "$ROOT"
# Untracked transcripts are allowed: an aborted run leaves the ones it bought
# in place (see abort), and the next run folds them in.
dirty="$(git status --porcelain | grep -v '^?? data/transcripts/' || true)"
if [ -n "$dirty" ]; then
  echo "working tree is dirty; commit or stash first:" >&2; echo "$dirty" | head >&2
  [ "$DRY" = 1 ] || exit 2
fi
if [ "$(git rev-parse --abbrev-ref HEAD)" != "main" ]; then
  echo "not on main (on $(git rev-parse --abbrev-ref HEAD))" >&2
  [ "$DRY" = 1 ] || exit 2
fi
if [ "$DRY" = 0 ]; then
  exec 9>"$LOCK"
  flock -n 9 || { echo "another refresh is running (lock $LOCK)" >&2; exit 2; }
fi

# ---- reset on any failure after this point ---------------------------------
abort() {
  echo "!! aborted at: $1"
  if [ "$DRY" = 0 ]; then
    # Tracked files go back to main. Untracked files are removed, except new
    # transcripts: those cost credits, they are good whatever went wrong
    # upstream, and the next run's sync_catalog.py folds them in.
    git checkout -q -- .
    git clean -qfd -e 'data/transcripts/*' data talks
    git checkout -q main 2>/dev/null || true
  fi
  echo "== FAILED $TODAY — tree reset, see $LOG"
  exit 1
}

run git pull --ff-only origin main || abort "git pull"

# ---- 2–3. registry, enumerate, enrich, derive -------------------------------
cd "$TOOLS"
run python3 check_registry.py || abort "check_registry.py"
run python3 sync_catalog.py --refresh || abort "sync_catalog.py --refresh"
run python3 enrich.py --min-year "$YEAR" --include-unknown-year || abort "enrich.py"
run python3 sync_catalog.py || abort "sync_catalog.py after enrich"

# ---- 4. transcripts, capped -------------------------------------------------
# The route is forced, so no --probe: the probe exists to choose a route and
# would cost a credit a day for nothing. A miss is bookkeeping, not failure —
# the fetcher records it in _misses.json and exits 0.
if [ "$TRANSCRIPTS" = 1 ]; then
  run "$PY" fetch_transcripts.py --source supadata --min-year "$YEAR" \
      --include-unknown-year --workers 32 --limit "$LIMIT" || abort "fetch_transcripts.py"
fi

# ---- 5. derive and index ----------------------------------------------------
run python3 sync_catalog.py || abort "sync_catalog.py after fetch"
run python3 build_index.py || abort "build_index.py"

cd "$ROOT"
if [ "$DRY" = 0 ] && [ -z "$(git status --porcelain)" ]; then
  echo "== nothing changed on $TODAY"; exit 0
fi

# ---- 6. the coverage gate ---------------------------------------------------
cd "$TOOLS"
set +e
run python3 refresh_report.py -o "$REPORT"; rc=$?
set -e
[ "$DRY" = 1 ] && rc=0
case "$rc" in
  0) ;;
  2) echo "!! a field lost more coverage than the tolerance allows — the throttled-enumeration"
     echo "   signature. Report kept at $REPORT; nothing committed."
     abort "refresh_report.py (regression)" ;;
  *) abort "refresh_report.py (exit $rc)" ;;
esac

# ---- 7. tests ---------------------------------------------------------------
for t in test_query test_excerpt test_infoq test_speakers test_topics \
         test_semantic test_fetch_transcripts test_stem; do
  run python3 "$t.py" >/dev/null || abort "$t.py"
done
echo "+ offline suites: all passed"

# ---- 8. branch, push, pull request ------------------------------------------
cd "$ROOT"
stats=""
[ "$DRY" = 1 ] || stats="$(python3 tools/query.py --stats 2>/dev/null | head -3 | tr '\n' ' ' || true)"
run git checkout -q -B "$BRANCH" || abort "git checkout"
run git add -A || abort "git add"
run git commit -q -m "Refresh the catalogue: $TODAY" -m "$stats" || abort "git commit"
run git push -f -u origin "$BRANCH" || abort "git push"
if [ "$DRY" = 0 ]; then
  if gh pr view "$BRANCH" >/dev/null 2>&1; then
    gh pr edit "$BRANCH" --body-file "$REPORT" >/dev/null
  else
    gh pr create --base main --head "$BRANCH" \
      --title "Refresh the catalogue: $TODAY" --body-file "$REPORT" >/dev/null
  fi
  url="$(gh pr view "$BRANCH" --json url -q .url)"
  git checkout -q main
  echo "== DONE $TODAY — $url"
  echo "$stats"
else
  echo "== dry run complete; would open a pull request from $BRANCH"
fi

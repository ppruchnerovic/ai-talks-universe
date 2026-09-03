#!/usr/bin/env bash
# Install the optional semantic layer — the only thing that ever builds it.
#
#   tools/install_semantic.sh              talk-level vectors (~10 s after the install)
#   tools/install_semantic.sh --chunks     plus transcript windows (~1.5 min more)
#   tools/install_semantic.sh --force      rebuild even when the stamp is current
#
# Runs from anywhere; resolves the repository from its own path. What it does,
# each step skipped when already done:
#
#   1. python3 -m venv tools/.venv-semantic            (needs python3-venv on Debian/Ubuntu)
#   2. pip install -r tools/requirements-semantic.txt  (prebuilt wheels only: no compiling,
#                                                      no torch, no onnx — ~70 MB on disk)
#   3. build_embeddings.py inside that venv, which fetches minishlab/potion-base-8M
#      (~30 MB, once, into tools/.venv-semantic/hf-cache) and writes data/embeddings/
#   4. `python3 tools/semantic.py --status` with the *system* python — the one query.py
#      runs on, which has no numpy — to prove the subprocess path works end to end
#
# Re-running with everything present rebuilds only if talks.json or the
# transcripts changed since the vectors were built (the stamp in
# talks.ids.json), or with --force. A layer built with --chunks keeps its
# chunks on later runs without the flag. Everything it creates is gitignored;
# `rm -rf tools/.venv-semantic data/embeddings` removes all of it, and nothing
# in the repository notices — see tools/semantic.py, rule 2.

set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$HERE/.." && pwd)"
VENV="$ROOT/tools/.venv-semantic"
PY="$VENV/bin/python"
REQ="$ROOT/tools/requirements-semantic.txt"
CACHE="$VENV/hf-cache"
EMB="$ROOT/data/embeddings"

CHUNKS=""
FORCE=""
for arg in "$@"; do
    case "$arg" in
        --chunks) CHUNKS="--chunks" ;;
        --force)  FORCE="yes" ;;
        -h|--help) sed -n '2,24p' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
        *) echo "install_semantic.sh: unknown option $arg (--chunks, --force, --help)" >&2; exit 2 ;;
    esac
done

kb() { du -sk "$1" 2>/dev/null | cut -f1 || echo 0; }          # KiB, or 0 when absent
mib() { echo "$(( ($1 + 512) / 1024 )) MiB"; }
say() { printf '%s\n' "$*"; }

T0=$SECONDS
cd "$ROOT"

# 1. the virtualenv
if [ -x "$PY" ]; then
    say "venv     present: $VENV"
else
    say "venv     creating $VENV"
    if ! python3 -m venv "$VENV"; then
        say "install_semantic.sh: python3 -m venv failed — on Debian/Ubuntu install the python3-venv package" >&2
        exit 1
    fi
fi

# 2. the libraries — wheels only, so a platform without one fails here, in
#    words, rather than three minutes into a compiler run.
BEFORE=$(kb "$VENV")
if ! "$PY" -m pip install --quiet --disable-pip-version-check --only-binary=:all: -r "$REQ"; then
    say "install_semantic.sh: pip could not install $REQ as prebuilt wheels for this platform" >&2
    exit 1
fi
AFTER=$(kb "$VENV")
if [ "$AFTER" -gt "$((BEFORE + 1024))" ]; then
    say "packages installed $(mib $((AFTER - BEFORE))) into the venv ($((SECONDS - T0)) s)"
else
    say "packages already present ($(mib "$AFTER") venv)"
fi

# 3. the model and the vectors. build_embeddings.py prints what it fetched
#    and how long each level took; --if-stale makes it a no-op when the stamp
#    matches the corpus.
#
#    pip trusts the operating system's certificate store; the Hub client
#    (httpx) trusts only certifi's bundle. Behind a corporate proxy that
#    re-signs TLS the two differ — pip installs, the model download fails
#    with CERTIFICATE_VERIFY_FAILED. Pointing httpx at the system bundle when
#    the user has not chosen one keeps verification on and makes the two
#    agree.
if [ -z "${SSL_CERT_FILE:-}" ]; then
    for bundle in /etc/ssl/certs/ca-certificates.crt /etc/pki/tls/certs/ca-bundle.crt /etc/ssl/cert.pem; do
        if [ -f "$bundle" ]; then export SSL_CERT_FILE="$bundle"; break; fi
    done
fi
if [ -z "$CHUNKS" ] && [ -f "$EMB/chunks.f16.npy" ]; then
    CHUNKS="--chunks"
    say "chunks   keeping: chunks.f16.npy exists, so the rebuild includes it"
fi
IF_STALE="--if-stale"
[ -n "$FORCE" ] && IF_STALE=""
CACHE_BEFORE=$(kb "$CACHE")
T1=$SECONDS
if ! "$PY" "$ROOT/tools/build_embeddings.py" $CHUNKS $IF_STALE; then
    say "install_semantic.sh: the build failed (see above). If it was the model download," >&2
    say "the network is needed once for ~30 MB from huggingface.co into $CACHE" >&2
    exit 1
fi
CACHE_AFTER=$(kb "$CACHE")
BUILD_S=$((SECONDS - T1))

# 4. the path query.py takes: system python3, no numpy, subprocess into the venv.
STATUS=$(python3 "$ROOT/tools/semantic.py" --status)
if ! grep -q '^available: True' <<<"$STATUS"; then
    say "$STATUS" >&2
    say "install_semantic.sh: built, but the system python3 cannot use the layer — see the status above" >&2
    exit 1
fi

say
say "semantic layer ready in $((SECONDS - T0)) s (build $BUILD_S s)"
say "  venv        $(mib "$AFTER")   $VENV"
say "  model cache $(mib "$CACHE_AFTER")   $CACHE$( [ "$CACHE_AFTER" -gt "$((CACHE_BEFORE + 1024))" ] && echo "  (fetched $(mib $((CACHE_AFTER - CACHE_BEFORE))))" )"
say "  vectors     $(mib "$(kb "$EMB")")   $EMB"
say "  $(grep '^vectors:' <<<"$STATUS" | sed 's|  */.*shape=| shape=|')"
say "  $(grep '^chunks:' <<<"$STATUS" | sed 's|  */.*shape=| shape=|')"
say "query.py uses it from now on; python3 tools/semantic.py --status says so, and why not if not."

#!/usr/bin/env bash
# Install (or refresh) the daily systemd user timer for tools/refresh_local.sh.
#
#     tools/install_refresh_timer.sh            # install and start
#     tools/install_refresh_timer.sh --remove
#
# It writes the unit files from tools/systemd/ into ~/.config/systemd/user/
# with this checkout's path filled in, creates the key file if it is missing,
# and enables the timer. Check on it with:
#
#     systemctl --user list-timers ai-talks-refresh.timer
#     systemctl --user start ai-talks-refresh.service      # run it now
#     journalctl --user -u ai-talks-refresh.service -n 50
#
# Timers run only while you are logged in unless lingering is on; the
# installer turns it on (loginctl enable-linger), --remove leaves it alone.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
UNITS="$HOME/.config/systemd/user"
ENV_FILE="$HOME/.config/ai-talks-universe/env"

if [ "${1:-}" = "--remove" ]; then
  systemctl --user disable --now ai-talks-refresh.timer 2>/dev/null || true
  rm -f "$UNITS"/ai-talks-refresh.{service,timer}
  systemctl --user daemon-reload
  echo "removed"; exit 0
fi

mkdir -p "$UNITS" "$(dirname "$ENV_FILE")"
sed "s|%h/git/ai-talks-universe|$ROOT|g; s|%h/.local/node/bin|$(dirname "$(command -v node || echo /usr/bin/node)")|" \
  "$ROOT/tools/systemd/ai-talks-refresh.service" > "$UNITS/ai-talks-refresh.service"
cp "$ROOT/tools/systemd/ai-talks-refresh.timer" "$UNITS/ai-talks-refresh.timer"

if [ ! -f "$ENV_FILE" ]; then
  printf 'YOUTUBE_API_KEY=\nSUPADATA_API_KEY=\nGH_TOKEN=\nSUPADATA_MONTHLY_BUDGET=3000\n' > "$ENV_FILE"
  chmod 600 "$ENV_FILE"
  echo "created $ENV_FILE — fill in the three keys before the first run"
else
  chmod 600 "$ENV_FILE"
fi

if [ "$(loginctl show-user "$USER" -p Linger --value 2>/dev/null)" != "yes" ]; then
  loginctl enable-linger "$USER" && echo "lingering enabled: the timer fires without a login session" \
    || echo "!! could not enable lingering; the timer runs only while you are logged in"
fi
systemctl --user daemon-reload
systemctl --user enable --now ai-talks-refresh.timer
systemctl --user list-timers ai-talks-refresh.timer --no-pager
echo "installed; next run above. Dry run now: tools/refresh_local.sh --dry-run"

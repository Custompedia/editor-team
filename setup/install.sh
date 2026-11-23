#!/usr/bin/env bash
# Editor Team: install the A-roll editing kit into a Claude Code cloud container.
# Idempotent: safe to run again. Usage: bash setup/install.sh   (from anywhere)
# Result: kit in /home/user/editkit, jobs in /home/user/jobs, skill at /home/user/editkit/skill, doctor READY.
set -euo pipefail
REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
K=/home/user/editkit
LOG=/tmp/editor-team-install.log
echo "== Editor Team install from $REPO (log: $LOG)"
for t in python3 node npm ffmpeg ffprobe fc-cache; do command -v $t >/dev/null || { echo "MISSING: $t"; exit 1; }; done

# 1) kit files (keep existing .venv / node_modules)
mkdir -p $K /home/user/jobs
cp -r "$REPO/editkit/." $K/
chmod +x $K/tools/*.sh $K/new_job.sh
mkdir -p $K/raw $K/work/tx $K/out $K/video/out
[ -f /home/user/jobs/registry.md ] || printf '# Worker Registry\n\n| Agent | Status | Job | Link | Output |\n|---|---|---|---|---|\n' > /home/user/jobs/registry.md

# 2) python venv. PyAV must stay <17 (newer breaks faster-whisper 1.2.1).
#    Python Playwright must match the preinstalled browser build in /opt/pw-browsers -> same version as the global Node playwright.
PWV=$(node -e "console.log(require('playwright/package.json').version)" 2>/dev/null || echo "")
[ -d $K/.venv ] || python3 -m venv $K/.venv
. $K/.venv/bin/activate
pip install --quiet --upgrade pip >>$LOG 2>&1
pip install --quiet "faster-whisper==1.2.1" "av<17" numpy pillow gdown yt-dlp "playwright${PWV:+==$PWV}" >>$LOG 2>&1
echo "python ok (playwright ${PWV:-latest})"

# 3) remotion (versions locked in package-lock.json) + Chrome Headless Shell
(cd $K/video && npm ci --no-audit --no-fund >>$LOG 2>&1 && npx remotion browser ensure >>$LOG 2>&1)
echo "remotion ok"

# 4) fonts as SYSTEM fonts (web fonts hang the renderer in this environment)
bash $K/tools/install_fonts.sh >/dev/null && echo "fonts ok"

# 5) sound effects (already in repo; regenerate if missing)
[ -f $K/video/public/sfx/click.wav ] || (cd $K && bash tools/make_sfx.sh >>$LOG 2>&1)

# 6) Whisper large-v3 (~3 GB, once per container)
python3 -c "from faster_whisper import WhisperModel; WhisperModel('large-v3', device='cpu', compute_type='int8')" >>$LOG 2>&1 && echo "whisper ok"

# 7) skill at a stable path for workers: /home/user/editkit/skill -> this repo's skill folder (always current).
#    No global copy in ~/.claude/skills: the repo's .claude/skills is loaded when a chat opens in this repo,
#    and a second copy would list the skill twice and can go stale.
ln -sfn "$REPO/.claude/skills/edit-aroll" $K/skill
rm -rf "$HOME/.claude/skills/edit-aroll"
rm -f $K/GUIDE-edit-aroll.md $K/STYLE_NOTES.md   # moved into the skill / docs
test -f $K/skill/SKILL.md && test -f $K/skill/reference/workflow.md && echo "skill ok"

# 8) preflight
cd $K && python3 tools/doctor.py | grep -E "FAIL|RESULT"

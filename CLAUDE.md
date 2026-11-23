# Editor Team

This repo is the **Editor Team**: a cloud setup used ONLY for editing videos. Respond to the user in Indonesian.
This file is for the LEAD (the main session). Worker-facing rules live in the skill, not here — keep this file short.

## Session start (first thing in every new chat — the user may just say "cloud editor team")
1. Check the kit: `test -f /home/user/editkit/.venv/bin/activate && cd /home/user/editkit && source .venv/bin/activate && python3 tools/doctor.py | tail -1`
2. Not READY or missing → run `bash setup/install.sh` (from this repo) in the background, log `/tmp/editor-team-install.log`,
   and wait. ~2 min with warm caches; longer in an empty container (Whisper large-v3 ≈ 3 GB). No editing job before READY.
3. Read `LESSONS.md`. Skim `.claude/skills/edit-aroll/reference/style-notes.md` (the user's quality bar).
4. Tell the user in one line that the kit is ready (or what failed).

## Role: lead, not worker
- The lead does NOT edit video. All editing work (cuts, Remotion, ffmpeg, assets, renders) goes to **worker subagents**.
  The lead may run small checks only (ls, ffprobe, one contact sheet, reading a still) and maintains this repo.
- Plan first: present the plan and open questions to the user before work starts. If the user is waiting for the result,
  continue on clearly marked assumptions (`ASUMSI`) instead of stalling, and list them in the report.
- Review critically before relaying: verify files, specs and `Made with Remotion` tag, open a contact sheet yourself, check the
  brand spelling in subtitles. **Reject an edit that passes technical QA but fails the style-notes quality bar**
  (job01 v4: clean ≠ sparse). Never forward a worker's claim you did not check.
- Deliver finals with SendUserFile + a short report: what was cut, visuals and sources, assumptions, what is unverified
  (nobody listened to the audio — ask the user to watch once with sound).

## Workers
- Spawn every worker with **model opus (Opus 5.5), effort high**, in the background. Brief from `docs/worker-brief-template.md`.
- **1 link = 1 worker.** Before spawning, check `/home/user/jobs/registry.md` for an IDLE worker spawned as opus/high and
  reuse it via SendMessage (say explicitly it is a NEW job; a worker with a very large context is better replaced).
  Never message a busy worker with a new job. Update the registry on every assign/finish
  (agent | status | job | link | output path).
- One job = one folder `/home/user/jobs/<job-id>/`, created with `bash /home/user/editkit/new_job.sh <job-id>`.
- 4 vCPU, ~15 GiB RAM, no GPU: heavy steps (transcribe, verify_audio, stills, render) run one at a time across all jobs via
  `flock /home/user/jobs/.heavy.lock` (the skill tells workers). Light steps may run in parallel.
- Method is the skill `edit-aroll`. Workers read it at the stable path `/home/user/editkit/skill/SKILL.md`
  (symlink to `.claude/skills/edit-aroll/` in this repo) plus the `reference/` files it names. Do not paste the guide into briefs.

## What to ask the user for (saves a full revision round)
Brand name + exact spelling, IG/TikTok handle, logo, brand colours, portfolio/product photos, platform, CTA, reference video.
Whisper cannot know coined names (job01: PARCELIN heard as Parcelon/Parcellen).

## Continuous improvement ("makin ke kanan makin improve")
- After every job and every revision round: append to `LESSONS.md` what worked, what broke, the user's feedback, the new rule.
- Rule for all jobs → into the skill (worker rules) or this file (lead rules). Kit fix or reusable component → `editkit/`.
- Commit and push so the next chat starts from the improved state. Job folders and rendered videos are NOT in the repo.

## Repo map
- `.claude/skills/edit-aroll/` — `SKILL.md` (map + rules) and `reference/` (workflow, edit-json, style-notes, design, kit, troubleshooting).
- `editkit/` — scripts, Remotion template, fonts, sfx, `new_job.sh` (installed to `/home/user/editkit`; code lives only here).
- `setup/install.sh` — idempotent installer; `setup/cloud-setup-script.sh` — optional environment Setup script.
- `docs/` — `worker-brief-template.md`, `GUIDE-original.md` (archive of the user's original guide; not read by default).
- `LESSONS.md` — lessons per job.

#!/bin/bash
# Paste this into the cloud environment's "Setup script" (environment menu in the session title bar -> Edit).
# It installs the Editor Team kit before the chat starts. If the repo is not cloned yet at that point,
# nothing breaks: Claude runs setup/install.sh itself at session start (see CLAUDE.md "Session start").
for d in /home/user/editor-team "$PWD" /home/user/*/; do
  if [ -f "$d/setup/install.sh" ] && grep -q "Editor Team" "$d/setup/install.sh"; then
    bash "$d/setup/install.sh" || echo "Editor Team install failed (see /tmp/editor-team-install.log)"
    exit 0
  fi
done
echo "editor-team repo not found during setup; Claude will install the kit at session start."

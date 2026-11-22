#!/usr/bin/env bash
# Create a new job folder wired to the shared kit.  Usage: bash /home/user/editkit/new_job.sh <job-id>
set -euo pipefail
K=/home/user/editkit; J=/home/user/jobs/${1:?job-id required}
[ -e "$J" ] && { echo "EXISTS: $J"; exit 1; }
mkdir -p $J/raw $J/work/tx $J/work/cand $J/work/ref $J/out $J/video/out $J/video/public/{shots,photos,broll,logos,gen,music}
ln -s $K/.venv $J/.venv
cp -r $K/tools $J/tools
cp $K/work/edit.example.json $J/work/
cp -r $K/video/src $K/video/package.json $K/video/tsconfig.json $K/video/stills.mjs $J/video/
ln -s $K/video/node_modules $J/video/node_modules
cp -r $K/video/public/sfx $J/video/public/sfx
bash $K/tools/install_fonts.sh >/dev/null
echo "READY: $J"

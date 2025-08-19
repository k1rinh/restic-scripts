#!/bin/bash
set -euo pipefail

source ./env.sh

restic forget \
    --group-by 'host,tags' \
    --keep-last 3 \
    --keep-daily 7 \
    --keep-monthly 6 \
    --keep-yearly 3

restic prune

restic check --read-data-subset=1G

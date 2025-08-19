#!/bin/bash
set -euo pipefail

source ../env.sh

restic backup \
    --tag "freshrss" \
    --group-by 'host,tags' \
    --skip-if-unchanged \
    --files-from ./includes.txt \
    --exclude-file ./excludes.txt

#!/bin/bash
set -euo pipefail

source ../env.sh

restic backup \
    --tag "memos" \
    --group-by 'host,tags' \
    --skip-if-unchanged \
    --files-from ./includes.txt \
    --exclude-file ./excludes.txt

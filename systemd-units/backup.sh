#!/bin/bash
set -euo pipefail

source ../env.sh

restic backup \
    --compression max \
    --cleanup-cache \
    --tag "$RESTIC_TAG" \
    --group-by 'host,tags' \
    --exclude-caches \
    --files-from ./includes.txt \
    --exclude-file ./excludes.txt

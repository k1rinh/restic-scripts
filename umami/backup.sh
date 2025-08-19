#!/bin/bash
set -euo pipefail

source ../env.sh

restic backup \
    --stdin-filename "umami-postgresql-db.sql" \
    --tag "umami" \
    --group-by 'host,tags' \
    --skip-if-unchanged \
    --stdin-from-command \
    -- docker exec -t umami-db-1 \
        pg_dumpall --clean --if-exists --username umami

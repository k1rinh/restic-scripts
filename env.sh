#!/bin/bash
#set -euo pipefail

RESTIC_HOST="$(hostname)"

RESTIC_REPOSITORY_FILE=~/.config/restic/repository.txt
RESTIC_PASSWORD_FILE=~/.config/restic/password.txt

export RESTIC_HOST RESTIC_REPOSITORY_FILE RESTIC_PASSWORD_FILE 

restic cat config
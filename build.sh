#!/usr/bin/env bash
# Render build step
set -o errexit
pip install uv
uv sync --frozen --no-dev
.venv/bin/python manage.py collectstatic --noinput

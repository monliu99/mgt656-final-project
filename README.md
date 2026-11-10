# I Do List (team nameless-wind)

An AI wedding planner for couples planning without a human one. MGT 656 final project.

## Run locally
```bash
uv sync
export DEBUG=1 SEED_ADMIN_PASSWORD=change-me SEED_COUPLE1_PASSWORD=change-me-too SEED_COUPLE2_PASSWORD=change-me-three
uv run python manage.py migrate
uv run python manage.py seed
uv run python manage.py runserver
uv run python manage.py test
```
Config is read from environment variables: `SECRET_KEY`, `DATABASE_URL`, `ALLOWED_HOSTS`,
`CSRF_TRUSTED_ORIGINS`, `DEBUG`, `SEED_ADMIN_PASSWORD`, `SEED_COUPLE1_PASSWORD`, `SEED_COUPLE2_PASSWORD`.
Without `DATABASE_URL` it uses SQLite (local development only).

## A/B test page
`/2c65d9f` and `/2c65d9f/stats` (SHA-1 of `nameless-wind`).

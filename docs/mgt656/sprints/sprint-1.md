# Sprint 1 report: walking skeleton

## Sprint goal
Get the whole pipeline working end to end before building real features: a Django app with user accounts, connected to Postgres, deployed to staging, with a seed command and the A/B test page.

## What shipped
- [#4 Walking skeleton: accounts, seed, A/B page, staging deploy](https://github.com/monliu99/wedding-planner/issues/4), closed by [PR #5](https://github.com/monliu99/wedding-planner/pull/5)
  - Django 5.2 app with standard signup, login and logout
  - 12-factor setup: configuration and secrets in environment variables, database attached through `DATABASE_URL`, logs to stdout, listens on `$PORT`, schema changes through migrations
  - `manage.py seed` creates `admin@example.com`, `couple1@example.com` and `couple2@example.com`; safe to run repeatedly; passwords come from environment variables, not git
  - A/B test page at `/2c65d9f` and live JSON stats at `/2c65d9f/stats` (hash of team nickname `nameless-wind`)
  - 12 automated tests covering the A/B counting rules, authentication and the seed command
  - `docs/mgt656/team.yaml` with all five members, and a pull request template
- Backlog: nine user stories with acceptance criteria, [#6](https://github.com/monliu99/wedding-planner/issues/6) to [#14](https://github.com/monliu99/wedding-planner/issues/14), covering the intake form, the AI plan, the checklist, deadlines, the budget, vendors, the guest list and RSVPs
- [Project board](https://github.com/users/monliu99/projects/1) linked to the repo, with one iteration per sprint dated to the course deadlines
- This final report, [#16](https://github.com/monliu99/wedding-planner/issues/16)

## What works on staging now
Staging: https://nameless-wind-staging.onrender.com (Render web service, Neon Postgres)
- Signup, login and logout
- The three seeded accounts can log in
- `/2c65d9f` shows one `kudos` or `thanks` button, assigned at random and kept per visitor, with one impression and at most one click counted per visitor
- `/2c65d9f/stats` returns JSON with a live `preferred` value

Not yet built: wedding features, AI plan generation, production environment (Sprint 2).

## Working with our agents
The agent first wrote `render.yaml` with a `preDeployCommand` to run migrations and seeding. Render's free tier does not support pre-deploy commands, so the deploy would have failed. We caught it by reading the config against Render's free-tier limits before deploying, and moved `migrate` and `seed` into the start command, which is safe because both can run repeatedly. A second lesson: the first deploy failed because `DATABASE_URL` was set to something that was not a real connection string, so we now check the value starts with `postgresql://` before saving. We also changed the agent's first seed accounts (admin and member) to match our team's plan of two demo couples.

## Backlog changes for next sprint
- At Sprint 2 planning, choose which of #6 to #14 we commit to and put them in the Sprint 2 iteration. Proposed order: the checklist and budget first, since the AI plan creates tasks and budget lines, then guests and RSVPs, then vendors.
- Add stories for a production environment and for deploying staging automatically when we merge to `main`
- Give the seed accounts demo wedding data once the models exist
- Add the OpenRouter key and a mocked-LLM test setup
- Carry over from Sprint 1: the README rewrite ([#15](https://github.com/monliu99/wedding-planner/issues/15)) and pointing the staging service at `main`

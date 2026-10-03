# Quartermaster — learn discord.py by building a bot over 7 days

Quartermaster is a small community-helper Discord bot: dice, polls, reminders,
and light moderation. It is also a **curriculum**. The repo starts as
documentation plus stubs (docstrings, pseudocode, failing tests) and you fill
it in one day at a time.

**Start here: [`PLAN.md`](PLAN.md)** (schedule, time estimates, how to track progress).

## What the finished bot does

| Feature | Commands / behaviour | Taught on |
|---|---|---|
| Connection, events | logs in, reacts to messages | Day 1 |
| Prefix commands, dice | `!ping`, `!roll 2d6+3` | Day 2 |
| Slash commands, embeds | `/ping`, `/roll`, `/about`, `/userinfo` | Day 3 |
| Cogs & extensions | modular code, `/admin reload`, logging | Day 4 |
| Buttons, selects, modals | `/poll create` with live voting buttons | Day 5 |
| Background tasks, SQLite | `/remind me 1h30m "stretch"` survives restarts | Day 6 |
| Events, permissions, deploy | welcome message, automod, `/purge`, Dockerfile | Day 7 |

## Quick start

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env          # you fill in the token on Day 1
make status                   # shows which days' tests pass
make day N=2                  # run only Day 2's tests
python -m quartermaster       # run the bot (works from Day 1 onward)
```

## Repo map

```
PLAN.md              the schedule and time estimates (read first)
PROGRESS.md          your checklist; tick as you go
docs/day-0N.md       the lesson for each day
docs/architecture.md how the finished bot fits together
docs/cheatsheet.md   asyncio refresher + discord.py quick reference
quartermaster/       the bot package (stubs -> real code)
tests/               pure-logic tests, tagged by day (red -> green = progress)
scripts/status.py    progress dashboard behind `make status`
```

## Conventions

* Branch per day: `git switch -c day-02`; merge to `main` when the day's tests pass.
* Tag finished days: `git tag day-02-done`.
* Never commit `.env`. If a token leaks, reset it in the Developer Portal immediately.

# Day 6 — Time and persistence (≈2.5 h)

**Goal:** `/remind me 1h30m "stretch"` fires on time and survives a restart.
`make day N=6` green.

| Block | Time |
|---|---|
| `durations.py` to green | 30 min |
| `storage.py` to green (aiosqlite) | 45 min |
| `tasks.loop` + cog wiring | 45 min |
| Restart test, edge cases | 30 min |

## Concepts

* **Persistence changes the design.** In-memory `asyncio.sleep(3600)` is lost
  on restart. Store due times and *poll* them with a periodic task.
* **`discord.ext.tasks`.** `@tasks.loop(seconds=15)` runs a coroutine on a
  schedule, handles reconnection, and exposes `start/cancel/restart`. Await
  `bot.wait_until_ready()` in `before_loop` so channel lookups work. An
  uncaught exception stops the loop, so guard the body.
* **`aiosqlite`.** Same API shape as `sqlite3` but awaitable, so DB I/O never
  stalls the loop. Always use `?` parameters, never f-strings, for SQL values.
* **Time.** Store timezone-aware UTC, format for users with Discord
  timestamps (`discord.utils.format_dt(dt, "R")`) so every client renders local time.
* **Delivery semantics.** Delete *after* send succeeds: a crash in between
  causes a duplicate, never a loss (at-least-once). State the trade-off in a comment.
* **Cog lifecycle.** `cog_load` / `cog_unload` start/stop the loop, so
  `/admin reload reminders` doesn't leak a second loop.

## Steps

1. `core/durations.py`: parse/format with tests.
2. `core/storage.py`: `ReminderStore` with tests (use `":memory:"`).
3. `bot.setup_hook`: open the store, attach to `bot.store`; close it in `bot.close`.
4. `cogs/reminders.py`: `/remind me|list|cancel`, `check_reminders` loop. Add it to `COGS`.
5. Manual: `/remind me 10s hi`; stop the bot with a 2-minute reminder pending,
   restart after it is due, and confirm late delivery.

## Read

`discord.ext.tasks` (including `before_loop`, `cog_load`), `aiosqlite` README,
`discord.utils.format_dt`, Python `datetime` timezone docs.

## If you're stuck

* `TypeError: can't compare offset-naive and offset-aware datetimes`: mixed naive/aware; use `datetime.now(timezone.utc)` everywhere.
* Loop never fires: forgot `.start()` or the cog isn't loaded.
* "database is locked": two connections or a missed `await commit()`.

## Done when

- [ ] `make day N=6` green
- [ ] Reminder fires within ~15 s of due; `list` and `cancel` work, cancel is owner-only
- [ ] Survives restart
- [ ] You can explain why `aiosqlite` and what `before_loop` is for
- [ ] Tagged `day-06-done`

## Stretch

Recurring reminders (`every 1d`), or switch the poll loop to a smarter
"sleep until the next due time" (`next_due()` query + `loop.change_interval`).

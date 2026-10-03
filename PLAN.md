# The Plan: discord.py in 7 sessions

## Who this is for

You have a CS degree and working Python, possibly rusty. You know what a
process, socket, and HTTP API are. You may not have used `async`/`await`
recently, or ever in Python. We will not re-teach CS; we focus on (1) the
asyncio mental model and (2) how discord.py maps onto Discord's gateway + REST
model.

## Time estimates

Assumes **7 sessions of 1.5-2.5 hours** (about **14-15 hours total**), one per
day or every other day. Estimates include reading docs, coding, and the usual
debugging; they do not include rabbit holes.

| Day | Theme | Est. | Biggest time sink |
|---|---|---|---|
| 1 | Setup, connect, events | 1.5 h | Developer Portal clicking, intents confusion |
| 2 | Prefix commands, converters, errors | 2 h | Understanding `async`/`await` and the event loop |
| 3 | Slash commands & embeds | 2 h | Command sync behaviour (global vs guild) |
| 4 | Cogs, extensions, config, logging | 2 h | Refactoring without breaking things |
| 5 | Buttons, selects, modals (Views) | 2.5 h | View lifecycle, timeouts, interaction responses |
| 6 | Background tasks, SQLite persistence | 2.5 h | Task lifecycle, datetimes/timezones |
| 7 | Moderation, permissions, deploy | 2.5 h | Permission model, hosting choices |
| | **Total** | **~15 h** | |

Add a ~20% buffer for Days 2, 5 and 6; they are the conceptually densest.

**Faster track (~10 h):** skip every "Stretch" section, and on Day 7 do only
the welcome message and the Dockerfile.
**Slower track (~20 h):** split Days 5 and 6 over two sessions each.

> If a day runs more than ~50% over its estimate, stop and read the "If you're
> stuck" section of that day's doc before pushing on. Overruns almost always
> come from a missed concept, not from missing effort.

## How the repo keeps you on track

1. **Docs-first stubs.** Every module's docstring describes the *finished*
   behaviour as if it already worked. Function bodies are pseudocode comments
   plus `raise NotImplementedError`. Your job is to make the docs true.
2. **Tests as a progress bar.** Pure-logic pieces (dice, durations, storage,
   poll tallies, automod) have tests tagged `day2`, `day6`, etc. They fail at
   the start. `make status` shows a per-day table; green means done.
   Discord-facing code can't be unit-tested cheaply, so each day doc ends with
   a manual **"Done when"** checklist you verify in a real server.
3. **`PROGRESS.md`** is the checklist. Tick items, commit.
4. **Git rhythm.** Branch `day-NN`, small commits, merge when done, tag
   `day-NN-done`. `git log --oneline` becomes your learning journal.

## Day summaries

### Day 1 — Hello, gateway (1.5 h)
Create the application and bot user, understand **intents**, invite the bot to
a private test server, connect with the bare `discord.Client`, handle
`on_ready` and `on_message`. *Concept:* gateway (websocket events) vs REST.
Doc: [`docs/day-01.md`](docs/day-01.md)

### Day 2 — Commands the classic way (2 h)
Switch to `commands.Bot`; write prefix commands, arguments, converters, and
error handlers; implement the pure dice parser behind `!roll`.
*Concept:* coroutines, `await`, why blocking calls are fatal.
Doc: [`docs/day-02.md`](docs/day-02.md)

### Day 3 — Slash commands & embeds (2 h)
`app_commands`, parameter descriptions, choices, autocomplete, `Interaction`
responses (the 3-second rule), embeds, ephemeral replies, command syncing.
*Concept:* interactions are a different delivery path from messages.
Doc: [`docs/day-03.md`](docs/day-03.md)

### Day 4 — Structure: cogs, extensions, config, logging (2 h)
Move everything into cogs, load them from `setup_hook`, hot-reload with an
owner-only command, typed config from environment, real logging.
*Concept:* making a bot maintainable and debuggable.
Doc: [`docs/day-04.md`](docs/day-04.md)

### Day 5 — Interactive UI (2.5 h)
`discord.ui.View`, buttons, select menus, modals; build `/poll create` with
live vote tallies using the pure `PollState` class.
*Concept:* stateful UI over a stateless HTTP interaction model.
Doc: [`docs/day-05.md`](docs/day-05.md)

### Day 6 — Time and persistence (2.5 h)
`tasks.loop`, SQLite via `aiosqlite`, reminders that survive restarts, duration
parsing. *Concept:* long-running task lifecycle; never block the loop.
Doc: [`docs/day-06.md`](docs/day-06.md)

### Day 7 — Guardrails and shipping (2.5 h)
Member events, automod, permission checks, bulk delete, rate limits,
Dockerfile, deployment notes. *Concept:* least privilege and operational basics.
Doc: [`docs/day-07.md`](docs/day-07.md)

## Ground rules

* **Private test server only.** Create a throwaway server; never test on a real community.
* **Token hygiene.** `.env` is gitignored; the token is a password.
* **Read the real docs.** These lessons point at sections of the official
  discord.py documentation (https://discordpy.readthedocs.io). The library
  moves; this repo pins `discord.py>=2.4` and was checked against 2.7. Where this
  repo and the docs disagree, the docs win; fix the repo and commit the fix.
* **Out-of-date check for you.** If you last used Python before 3.10, skim
  `docs/cheatsheet.md` first (type hints with `|`, `match`, dataclasses, `asyncio.run`).

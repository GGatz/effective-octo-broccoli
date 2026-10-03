# Progress

Tick as you go (`- [x]`) and commit. `make status` shows the automated half.
Log actual time spent so you can calibrate: estimates are in `PLAN.md`.

| Day | Est. | Actual | Started | Finished |
|---|---|---|---|---|
| 1 | 1.5 h | | | |
| 2 | 2 h | | | |
| 3 | 2 h | | | |
| 4 | 2 h | | | |
| 5 | 2.5 h | | | |
| 6 | 2.5 h | | | |
| 7 | 2.5 h | | | |

## Day 1 — Hello, gateway
- [ ] Test server created; application + bot user created in Developer Portal
- [ ] Token in `.env` (not committed); Message Content intent enabled
- [ ] Bot invited with `bot` scope; shows online
- [ ] `on_ready` logs the bot's name and guild count
- [ ] `on_message` replies "pong" to "ping" and ignores its own messages
- [ ] Can explain: gateway vs REST, what an intent is

## Day 2 — Prefix commands
- [ ] `make day N=2` is green (dice parser)
- [ ] `!ping`, `!roll 2d6+3` work in the server
- [ ] Bad input to `!roll` gives a friendly error, not a stack trace
- [ ] Can explain: what `await` does; why `time.sleep` freezes the bot

## Day 3 — Slash commands & embeds
- [ ] `make day N=3` is green (embed helper)
- [ ] `/ping`, `/roll` (with autocomplete or choices), `/about`, `/userinfo` work
- [ ] Guild-scoped sync for development; understand global sync delay
- [ ] Can explain: why you must respond to an interaction within 3 seconds, and what `defer` does

## Day 4 — Structure
- [ ] Commands live in cogs under `quartermaster/cogs/`
- [ ] Extensions load in `setup_hook`; `/admin reload` works (owner only)
- [ ] Config is loaded from env into a dataclass; missing token fails with a clear message
- [ ] Logging to console and a rotating file
- [ ] Can explain: what `setup_hook` is for vs `on_ready`

## Day 5 — Views
- [ ] `make day N=5` is green (`PollState`)
- [ ] `/poll create` posts a poll with buttons; counts update live
- [ ] A modal collects the question and options
- [ ] Poll closes on timeout or via a Close button restricted to the creator
- [ ] Can explain: custom_id, view timeout, `interaction.response` vs `followup`

## Day 6 — Time & persistence
- [ ] `make day N=6` is green (durations, storage)
- [ ] `/remind me 10s "hi"` pings you ~10 seconds later
- [ ] Restart the bot with a pending reminder; it still fires
- [ ] `/remind list` and `/remind cancel` work
- [ ] Can explain: why `aiosqlite` instead of `sqlite3`; what `before_loop` is for

## Day 7 — Guardrails & shipping
- [ ] `make day N=7` is green (automod rules)
- [ ] Welcome message on member join (needs Members intent)
- [ ] `/purge` requires Manage Messages for both user and bot
- [ ] Automod warns on mass mentions / banned words
- [ ] `docker build` works; README has run instructions
- [ ] Can explain: least privilege for intents and permissions

## Retrospective
- What was harder than estimated?
- What would you build next? (ideas in `docs/day-07.md` stretch section)

# Day 2 — Commands the classic way (≈2 h)

**Goal:** move to `commands.Bot`, add `!ping` and `!roll`, and get
`make day N=2` green. This is the day the asyncio mental model has to click.

| Block | Time |
|---|---|
| asyncio refresher (`cheatsheet.md`) | 25 min |
| Dice parser to green tests | 40 min |
| `commands.Bot`, commands, error handling | 40 min |
| Manual test + commit | 15 min |

## Concepts

* **Coroutines.** `async def` returns a coroutine object; nothing runs until
  it is awaited or scheduled. `await` suspends *this* coroutine and lets the
  loop run others. One thread, cooperative multitasking.
* **Never block the loop.** `time.sleep(5)` or a slow `requests.get` freezes
  the whole bot, including its heartbeat, and Discord may disconnect you. Use
  `await asyncio.sleep`, async libraries, or `asyncio.to_thread` for blocking work.
* **`commands.Bot`** = `Client` + command framework: prefix, parsing, converters,
  checks, cogs, error handling.
* **Converters.** Type annotations (`count: int`, `member: discord.Member`)
  make the framework parse and validate arguments; failures raise
  `commands.BadArgument` / `MissingRequiredArgument` into your error handler.
* **Pure logic first.** `core/dice.py` has no Discord imports: write it with
  the tests, *then* wire it up.

## Steps

1. `core/dice.py`: implement `parse`, `roll`, `RollResult.describe` until `make day N=2` passes.
2. `bot.py`: `QuartermasterBot(commands.Bot)` with intents and prefix from config.
   Update `__main__.py` to use `async with bot: await bot.start(token)`.
3. Temporarily define commands inside `bot.py` (cogs come Day 4) or in
   `cogs/general.py` loaded manually.
4. `!ping` → latency; `!roll 2d6+3` → `describe()`; bad input → friendly message.
5. Add `on_command_error`: friendly text for `CommandNotFound` (maybe ignore),
   `MissingRequiredArgument`, `BadArgument`; `log.exception` for anything else.

## Read

*Commands* (ext.commands intro), *Converters*, *Error handling* in the docs,
Python's `asyncio` "Coroutines and Tasks" overview.

## If you're stuck

* Commands don't fire: forgot `message_content` intent, or overrode
  `on_message` without calling `await self.process_commands(message)`.
* "coroutine was never awaited": you forgot `await`.
* Test fails only on `describe`: the test just wants rolls and total visible.

## Done when

- [ ] `make day N=2` green
- [ ] `!ping`, `!roll d20`, `!roll 2d6+3` work; `!roll banana` replies politely
- [ ] You can explain why `time.sleep` is harmful here and what to use instead
- [ ] Tagged `day-02-done`

## Stretch

`!roll` with multiple expressions (`!roll 2d6 d20`), or advantage/disadvantage (`!roll d20 adv`).

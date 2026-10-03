# Day 4 — Structure: cogs, extensions, config, logging (≈2 h)

**Goal:** the structure of a real bot. No new Discord features; this is a
disciplined refactor, and the one day with no tests to guide you, so commit often.

| Block | Time |
|---|---|
| Read: cogs, extensions | 20 min |
| Move commands into `General` cog | 30 min |
| `config.py`, `logging_setup.py`, `__main__.py` | 40 min |
| `Admin` cog with reload | 30 min |

## Concepts

* **Cog** = a class grouping commands/listeners/state. Listeners use
  `@commands.Cog.listener()` (many cogs can listen to one event, unlike
  overriding `on_message` on the bot).
* **Extension** = a module with `async def setup(bot)`; loaded by dotted path
  with `bot.load_extension`. Reloading re-imports the module: edit code, reload, no restart.
* **`setup_hook` vs `on_ready`.** `setup_hook` runs once before the websocket
  connects: load extensions, open DB connections, sync. `on_ready` can run many times.
* **Config at the edge.** Parse environment variables once into a frozen
  dataclass; pass `Config` around instead of reading `os.environ` in cogs.
* **Logging**, not `print`: levels, timestamps, files, and tracebacks via
  `log.exception`. Use `logging.getLogger(__name__)` per module.

## Steps

1. `config.py` → `load_config()` (token required; clear message when missing).
2. `logging_setup.py` → console + rotating file.
3. Move commands into `cogs/general.py`; implement `setup`. Cog-level error
   handling via `cog_command_error` / `cog_app_command_error`.
4. `bot.py` `setup_hook` loops over `COGS`. Cogs without implementation yet
   (`polls`, `reminders`, `moderation`) raise `NotImplementedError` from
   `setup`; comment their names out of `COGS` until their day.
5. `cogs/admin.py`: `/admin reload <cog>` (owner only), `/admin sync`, `/admin shutdown`.
6. Practise the loop: change the `/ping` text, `/admin reload general`, see it update live.

## Read

*Cogs*, *Extensions* (`load_extension`, `reload_extension`), `Bot.setup_hook`,
`Setting Up Logging`.

## If you're stuck

* `ExtensionFailed`: look at `__cause__`/the traceback for the real error.
* Commands duplicated after reload: the cog wasn't removed (reload handles
  this) or you registered the same command twice.
* Slash commands missing after refactor: tree sync needed again.

## Done when

- [ ] No commands defined outside cogs
- [ ] Missing token → one-line error, no traceback
- [ ] `logs/bot.log` is written and rotates
- [ ] `/admin reload` works and is refused for non-owners
- [ ] You can explain `setup_hook` vs `on_ready`
- [ ] Tagged `day-04-done`

## Stretch

Per-guild settings (prefix) stored in a dict now, SQLite on Day 6. Or a
`/help` command listing commands per cog.

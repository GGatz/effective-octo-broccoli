# Cheatsheet

## Modern-Python refresher (3.10+)

```python
def f(x: int | None = None) -> list[str]: ...      # PEP 604 unions, builtin generics

from dataclasses import dataclass
@dataclass(frozen=True)
class P: x: int; y: int = 0

if (m := pattern.match(s)): ...                    # walrus

match command:                                     # structural pattern matching
    case ["roll", expr]: ...
    case _: ...

from pathlib import Path; Path("logs").mkdir(exist_ok=True)
```

## asyncio in five minutes

```python
import asyncio

async def fetch(n):            # coroutine function
    await asyncio.sleep(1)     # yields to the loop; time.sleep would block everything
    return n

async def main():
    a = await fetch(1)                                   # sequential: 1 s
    b, c = await asyncio.gather(fetch(2), fetch(3))      # concurrent: 1 s total
    t = asyncio.create_task(fetch(4))                    # fire and (later) await; keep a reference!
    await t
    r = await asyncio.to_thread(blocking_function)       # escape hatch for blocking code

asyncio.run(main())            # one loop per program, at the top
```

Rules: a coroutine does nothing until awaited; no blocking calls in `async`
code; exceptions in un-awaited tasks are easy to lose, so log them.

## discord.py map

| Want to… | Use |
|---|---|
| React to an event | `@client.event` / `@commands.Cog.listener()` |
| Prefix command | `@commands.command()` → `ctx.send` |
| Slash command | `@app_commands.command()` → `interaction.response.send_message` |
| Take >3 s | `await interaction.response.defer()` then `interaction.followup.send` |
| Only invoker sees it | `ephemeral=True` |
| Pretty message | `discord.Embed` |
| Buttons / selects | `discord.ui.View`, `@discord.ui.button` |
| Popup form | `discord.ui.Modal` |
| Run periodically | `@tasks.loop(...)` |
| Check permissions | `app_commands.checks.has_permissions` / `commands.has_permissions` |
| One-time startup | `Bot.setup_hook` |
| Local time for everyone | `discord.utils.format_dt(dt, "R")` |

Docs: https://discordpy.readthedocs.io (check the version selector matches your install: `pip show discord.py`).

"""The bot object.

Finished behaviour
------------------
``create_bot(config)`` returns a ``QuartermasterBot`` (a ``commands.Bot``):

* Intents: ``Intents.default()`` plus ``message_content`` (prefix commands, automod)
  and ``members`` (welcome messages). Both are *privileged* and must be enabled
  in the Developer Portal. Request only what you use.
* ``setup_hook`` (runs once, before connecting, inside the event loop):
    1. open the SQLite store and attach it as ``bot.store``
    2. ``load_extension`` for each module in ``COGS``
    3. sync the slash command tree: to ``DEV_GUILD_ID`` instantly in development
       (``copy_global_to`` then ``sync(guild=...)``), globally otherwise
* ``on_ready`` only logs; it can fire multiple times (reconnects), so never put
  one-time setup there.
* ``close`` closes the store, then defers to ``super().close()``.
* A global ``on_command_error`` turns common errors into friendly replies and
  logs everything else with a traceback.

Evolution: Day 1 uses a bare ``discord.Client`` in ``__main__``. Day 2 moves to
``commands.Bot`` here. Day 3 adds the tree sync. Day 4 adds cog loading.
Day 6 adds the store.
"""
from discord.ext import commands

from .config import Config

# Dotted module paths of extensions, in load order. Each defines ``async def setup(bot)``.
COGS = [
    "quartermaster.cogs.general",
    "quartermaster.cogs.admin",
    "quartermaster.cogs.polls",
    "quartermaster.cogs.reminders",
    "quartermaster.cogs.moderation",
]


class QuartermasterBot(commands.Bot):
    def __init__(self, config: Config, **kwargs):
        # TODO(Day 2): intents = discord.Intents.default(); intents.message_content = True
        #   super().__init__(command_prefix=config.command_prefix, intents=intents, **kwargs)
        #   self.config = config
        raise NotImplementedError

    async def setup_hook(self) -> None:
        # TODO(Day 4): for name in COGS: await self.load_extension(name)
        # TODO(Day 3): sync tree (see docs/day-03.md, "Syncing")
        # TODO(Day 6): self.store = await ReminderStore.open(self.config.database_path)
        raise NotImplementedError

    async def on_ready(self) -> None:
        # TODO(Day 1): log f"Logged in as {self.user} (id={self.user.id}) in {len(self.guilds)} guild(s)"
        raise NotImplementedError

    async def close(self) -> None:
        # TODO(Day 6): await self.store.close()
        await super().close()


def create_bot(config: Config) -> QuartermasterBot:
    return QuartermasterBot(config)

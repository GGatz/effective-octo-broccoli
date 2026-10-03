"""Entry point: ``python -m quartermaster``.

Finished behaviour
------------------
1. Load configuration (``config.load_config``). Exit with a readable message
   if DISCORD_TOKEN is missing.
2. Configure logging (``logging_setup.setup_logging``).
3. Build the bot (``bot.create_bot``) and run it with ``bot.start(token)``
   inside ``asyncio.run`` so we control startup and shutdown (close the DB, etc).
4. Ctrl+C exits cleanly.

Day 1 version: skip steps 2-3; just create a ``discord.Client`` here, wire
``on_ready`` / ``on_message``, and call ``client.run(token)``. Refactor into
``bot.py`` on Days 2 and 4.
"""
import asyncio

# from .config import load_config
# from .logging_setup import setup_logging
# from .bot import create_bot


async def main() -> None:
    # TODO(Day 1): minimal client, then replace with the structure below.
    #
    # config = load_config()
    # setup_logging(config.log_level)
    # bot = create_bot(config)
    # async with bot:                 # ensures bot.close() runs
    #     await bot.start(config.token)
    raise NotImplementedError("Day 1: connect to Discord")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass

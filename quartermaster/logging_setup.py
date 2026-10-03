"""Logging configuration.

Finished behaviour
------------------
* Console handler at the configured level, file handler at ``logs/bot.log``
  rotating at ~1 MB with 3 backups.
* One format everywhere: ``2026-01-01 12:00:00 INFO quartermaster.cogs.polls: message``.
* discord.py's own logger (``discord``) is kept at INFO (WARNING if you want
  quieter output); ``discord.http`` at WARNING because it is chatty.
* We do NOT pass ``log_handler`` to ``bot.run``; we configure logging ourselves
  and start the bot with ``bot.start``.

Introduced Day 4.
"""
import logging


def setup_logging(level: str = "INFO") -> None:
    # TODO(Day 4):
    #   Path("logs").mkdir(exist_ok=True)
    #   fmt = logging.Formatter("%(asctime)s %(levelname)s %(name)s: %(message)s")
    #   console = logging.StreamHandler(); console.setFormatter(fmt)
    #   file = logging.handlers.RotatingFileHandler("logs/bot.log", maxBytes=1_000_000, backupCount=3)
    #   root = logging.getLogger(); root.setLevel(level); root.addHandler(...) x2
    #   logging.getLogger("discord.http").setLevel(logging.WARNING)
    raise NotImplementedError

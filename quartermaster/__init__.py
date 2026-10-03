"""Quartermaster: a community-helper Discord bot (and a discord.py curriculum).

Finished behaviour (see docs/architecture.md for the full picture):

* Connects to Discord, loads every cog in ``quartermaster.cogs``.
* General: ``/ping``, ``/roll``, ``/about``, ``/userinfo`` (+ ``!`` equivalents).
* Polls: ``/poll create`` posts a message with vote buttons and a Close button.
* Reminders: ``/remind me|list|cancel``; stored in SQLite, survive restarts.
* Moderation: welcome message, automod warnings, ``/purge``.
* Admin: ``/admin reload <cog>`` for the owner.

Run with ``python -m quartermaster``.
"""

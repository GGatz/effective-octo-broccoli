"""Reminders (Day 6).

Finished behaviour
------------------
* ``/remind me <when> <message>``: ``when`` is a duration like ``1h30m``
  (``core.durations.parse_duration``). Stores a row via ``bot.store`` with
  ``due_at = utcnow + delta`` and confirms with a Discord timestamp, e.g.
  ``<t:1767225600:R>`` ("in 2 hours"), which renders in each viewer's own
  timezone. See ``discord.utils.format_dt``.
* ``/remind list``: the caller's pending reminders (ephemeral).
* ``/remind cancel <id>``: deletes by id, only if the caller owns it.
* A single ``tasks.loop(seconds=15)`` called ``check_reminders``:
    1. ``due = await store.due(now)``
    2. for each: fetch the channel (``bot.get_channel`` then ``fetch_channel``),
       send ``<@user> reminder: <message>``; on ``discord.Forbidden`` or a
       missing channel, try DM; on failure, log and drop it.
    3. delete the reminder *after* a successful send (at-least-once delivery).
  ``@check_reminders.before_loop`` awaits ``bot.wait_until_ready()``.
  The loop starts in ``cog_load`` and is cancelled in ``cog_unload``.
* Restart safety: because state is in SQLite and the loop re-reads it, a bot
  restarted mid-wait still delivers (late, never lost).

Edge cases to handle: reminders that came due while the bot was offline
(deliver immediately, say how late), per-user cap (25 pending), message length
cap (500 chars), and exceptions inside the loop body (wrap so one bad row
doesn't kill the loop).

Teaches: ``discord.ext.tasks``, cog lifecycle hooks, ``aiosqlite``,
timezone-aware datetimes, defensive loops.
"""
from discord.ext import commands

# import discord
# from discord import app_commands
# from discord.ext import tasks
# from ..core.durations import parse_duration, format_duration


class Reminders(commands.Cog):
    """Set reminders that survive restarts."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # TODO(Day 6):
    #   async def cog_load(self): self.check_reminders.start()
    #   async def cog_unload(self): self.check_reminders.cancel()
    #
    #   @tasks.loop(seconds=15)
    #   async def check_reminders(self): ...
    #   @check_reminders.before_loop
    #   async def _wait(self): await self.bot.wait_until_ready()
    #
    #   remind = app_commands.Group(name="remind", description="Reminders")
    #   me / list / cancel commands as described above


async def setup(bot: commands.Bot) -> None:
    # TODO(Day 6): await bot.add_cog(Reminders(bot))
    raise NotImplementedError

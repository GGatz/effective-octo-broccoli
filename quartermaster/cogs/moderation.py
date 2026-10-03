"""Moderation and member events (Day 7).

Finished behaviour
------------------
* ``on_member_join``: posts a welcome embed in the guild's system channel
  (``guild.system_channel``) if it exists and the bot can send there. Requires
  the privileged **Members** intent (enable in portal *and* code).
* ``on_message``: runs ``core.automod.find_violations`` on non-bot messages.
  On violation: reply with a gentle warning that names the rule, delete only
  for ``BANNED_WORD``, and log to a ``#mod-log`` channel if one exists.
  Members with Manage Messages are exempt. Never ban or kick automatically.
* ``/purge <count>``: bulk-deletes the last 1-100 messages in the channel using
  ``channel.purge``. Guarded twice (least privilege):
    - ``@app_commands.checks.has_permissions(manage_messages=True)`` for the user
    - ``@app_commands.checks.bot_has_permissions(manage_messages=True)`` for the bot
  Reply ephemerally with how many were deleted. ``defer`` first: purging can
  take longer than the 3-second interaction window.
* A cog-level ``cog_app_command_error`` (or tree error handler) converts
  ``MissingPermissions`` / ``BotMissingPermissions`` / ``CommandOnCooldown``
  into friendly ephemeral messages. Add a per-user cooldown to ``/purge``
  (``@app_commands.checks.cooldown(1, 10)``).

Teaches: member events and intents, permission checks vs. permission
overwrites, cooldowns, rate-limit awareness (discord.py handles 429s for you,
but bulk operations still deserve restraint), audit-friendly logging.
"""
from discord.ext import commands

# import discord
# from discord import app_commands
# from ..core.automod import Rules, find_violations


class Moderation(commands.Cog):
    """Welcome messages, automod warnings, and purge."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # TODO(Day 7):
    #   @commands.Cog.listener() async def on_member_join(self, member): ...
    #   @commands.Cog.listener() async def on_message(self, message): ...
    #   @app_commands.command(name="purge") ... as described above


async def setup(bot: commands.Bot) -> None:
    # TODO(Day 7): await bot.add_cog(Moderation(bot))
    raise NotImplementedError

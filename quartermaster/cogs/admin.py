"""Owner-only administration (Day 4).

Finished behaviour
------------------
* ``/admin reload <cog>``: reloads one extension via ``bot.reload_extension``
  and replies with success or the exception text. Autocomplete lists ``COGS``.
  Restricted to the bot owner using a check (``bot.is_owner``), because code
  reload is remote code execution of whatever is on disk.
* ``/admin sync``: re-syncs the slash command tree to the dev guild and reports
  how many commands were synced.
* ``/admin shutdown``: closes the bot cleanly (``await bot.close()``).

Replies are ephemeral so admin output doesn't spam channels.

Teaches: owner checks, ``app_commands.Group``, extension lifecycle.
"""
from discord.ext import commands

# from discord import app_commands


class Admin(commands.Cog):
    """Owner-only maintenance commands."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # TODO(Day 4):
    #   admin = app_commands.Group(name="admin", description="Owner-only tools")
    #   async def interaction_check(self, interaction) -> bool:   # cog-wide check
    #       return await self.bot.is_owner(interaction.user)
    #   @admin.command(name="reload") ... await self.bot.reload_extension(f"quartermaster.cogs.{cog}")


async def setup(bot: commands.Bot) -> None:
    # TODO(Day 4): await bot.add_cog(Admin(bot))
    raise NotImplementedError

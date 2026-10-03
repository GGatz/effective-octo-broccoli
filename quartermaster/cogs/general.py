"""General-purpose commands (Days 2-4).

Finished behaviour
------------------
Every command exists as a hybrid: ``!name`` and ``/name`` share one function
(``@commands.hybrid_command``). Hybrids are a convenience; Day 3 first writes
the slash versions with ``app_commands`` directly so you see what hybrids hide.

* ``ping``: replies with the gateway latency in ms (``bot.latency``).
* ``roll <expression>``: uses ``core.dice.roll``. On ``ValueError`` replies
  ephemerally with the message. Autocomplete suggests common expressions
  (``d20``, ``2d6``, ``4d6``, ``d100``). Result shown in an embed.
* ``about``: embed with version, uptime, guild count, discord.py version.
* ``userinfo [member]``: embed with the member's name, ID, account age, join
  date, top role, and avatar thumbnail. Defaults to the invoker.

Per-command error handling: bad ``roll`` input must never reach the global error
handler as an unhandled exception.
"""
from discord.ext import commands

# import discord
# from discord import app_commands
# from ..core import dice
# from ..core.embeds import make_embed


class General(commands.Cog):
    """Everyday utility commands."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # --- Day 2: prefix versions ------------------------------------------------
    # @commands.command()
    # async def ping(self, ctx): await ctx.send(f"Pong! {round(self.bot.latency * 1000)} ms")
    #
    # @commands.command()
    # async def roll(self, ctx, *, expression: str = "d20"):
    #     try: result = dice.roll(expression)
    #     except ValueError as err: return await ctx.send(str(err))
    #     await ctx.send(result.describe())

    # --- Day 3: slash versions -------------------------------------------------
    # @app_commands.command(name="ping", description="Check the bot's latency")
    # async def ping_slash(self, interaction: discord.Interaction):
    #     await interaction.response.send_message(...)
    #
    # @app_commands.command(name="roll", description="Roll dice, e.g. 2d6+3")
    # @app_commands.describe(expression="Dice notation like 2d6+3")
    # async def roll_slash(self, interaction, expression: str = "d20"): ...
    # @roll_slash.autocomplete("expression")
    # async def roll_autocomplete(self, interaction, current: str) -> list[app_commands.Choice[str]]: ...
    #
    # about, userinfo: see docstring above.


async def setup(bot: commands.Bot) -> None:
    # TODO(Day 4): await bot.add_cog(General(bot))
    raise NotImplementedError

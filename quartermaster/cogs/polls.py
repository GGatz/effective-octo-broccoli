"""Polls with buttons (Day 5).

Finished behaviour
------------------
``/poll create`` opens a **modal** with fields: Question (short), Options
(paragraph, one per line, 2-5). On submit:

1. Build ``PollState`` (``core.poll_state``); on ``ValueError`` reply ephemerally.
2. Post an embed (question, one line per option with a bar and count) with a
   ``PollView`` attached: one button per option plus a red "Close poll" button.
3. Each option button calls ``state.vote``; the message is edited to show new
   tallies; the voter gets an ephemeral note ("Vote added / moved / removed").
4. "Close poll" works only for the creator (others get an ephemeral refusal);
   it disables all buttons, closes the state, and highlights the winner(s).
5. The view times out after 24 h of no interaction: buttons are disabled and
   the poll is marked closed (``on_timeout``).

Known limitation (documented honestly): polls are in-memory, so buttons stop
working after a restart. Making views persistent (``timeout=None``, stable
``custom_id``s, ``bot.add_view`` in ``setup_hook``, state in SQLite) is the
Day 5 stretch goal.

Teaches: ``discord.ui.View``/``Button``/``Modal``/``TextInput``, interaction
responses (``response.send_message`` / ``edit_message`` / ``followup``),
view timeouts, per-user authorization inside callbacks.
"""
from discord.ext import commands

# import discord
# from discord import app_commands
# from ..core.poll_state import PollState, PollClosed
# from ..core.embeds import make_embed


# class PollModal(discord.ui.Modal, title="Create a poll"):
#     question = discord.ui.TextInput(label="Question", max_length=200)
#     options = discord.ui.TextInput(label="Options (one per line)", style=discord.TextStyle.paragraph)
#     async def on_submit(self, interaction): ...
#
# class PollView(discord.ui.View):
#     def __init__(self, state: PollState): super().__init__(timeout=24 * 3600) ...
#     # Buttons are created dynamically in __init__ (one per option), each with a
#     # callback closure over its index. Add via self.add_item(button).
#     async def on_timeout(self): ...


class Polls(commands.Cog):
    """Create and vote on polls."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # TODO(Day 5):
    #   poll = app_commands.Group(name="poll", description="Polls")
    #   @poll.command(name="create") async def create(self, interaction): await interaction.response.send_modal(PollModal())


def render_poll_embed(*args, **kwargs):
    """Build the poll embed from a ``PollState`` (bars like ``██████░░░░ 3``)."""
    # TODO(Day 5)
    raise NotImplementedError


async def setup(bot: commands.Bot) -> None:
    # TODO(Day 5): await bot.add_cog(Polls(bot))
    raise NotImplementedError

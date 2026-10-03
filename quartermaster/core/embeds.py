"""Embed helpers so every message looks consistent (Day 3). Tests: ``make day N=3``.

Finished behaviour
------------------
``make_embed(title, description, kind="info")`` returns a ``discord.Embed``:

* ``kind`` is one of ``"info"`` (blurple), ``"success"`` (green),
  ``"warning"`` (gold), ``"error"`` (red). Unknown kinds raise ``ValueError``.
* Title is truncated to 256 chars and description to 4096 (Discord's limits),
  with a trailing ellipsis character when truncated.
* A footer reads ``Quartermaster`` so users can tell the bot's own output.

Optional ``fields`` is a list of ``(name, value, inline)`` tuples.
"""
import discord

COLORS = {
    "info": discord.Color.blurple(),
    "success": discord.Color.green(),
    "warning": discord.Color.gold(),
    "error": discord.Color.red(),
}
TITLE_LIMIT = 256
DESCRIPTION_LIMIT = 4096
FOOTER_TEXT = "Quartermaster"


def truncate(text: str, limit: int) -> str:
    """Return ``text`` unchanged if short enough, else cut to ``limit`` ending in '…'."""
    # TODO(Day 3)
    raise NotImplementedError


def make_embed(
    title: str,
    description: str = "",
    kind: str = "info",
    fields: list[tuple[str, str, bool]] | None = None,
) -> discord.Embed:
    # TODO(Day 3):
    #   validate kind against COLORS
    #   embed = discord.Embed(title=truncate(...), description=truncate(...), color=COLORS[kind])
    #   for name, value, inline in fields or []: embed.add_field(name=..., value=..., inline=...)
    #   embed.set_footer(text=FOOTER_TEXT)
    raise NotImplementedError

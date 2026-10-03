"""Dice notation parser and roller (Day 2). Tests: ``make day N=2``.

Finished behaviour
------------------
``roll("2d6+3")`` rolls two six-sided dice and adds 3.

Grammar (case-insensitive, whitespace ignored)::

    expr     := [count] "d" sides [modifier]
    count    := 1..MAX_DICE      (default 1 if omitted, so "d20" works)
    sides    := 2..MAX_SIDES
    modifier := ("+" | "-") integer

Errors: anything that does not match, or exceeds the limits, raises
``ValueError`` with a message safe to show to users (the commands layer shows
``str(error)`` directly).

``rng`` is injectable so tests are deterministic. It needs only
``randint(a, b)``, which ``random`` (the module) and ``random.Random`` provide.
"""
import random
import re
from dataclasses import dataclass

MAX_DICE = 100
MAX_SIDES = 1000

# Suggested: re.compile(r"^(\d*)d(\d+)([+-]\d+)?$") applied to the cleaned string.
_PATTERN = re.compile(r"^(\d*)d(\d+)([+-]\d+)?$")


@dataclass(frozen=True)
class RollResult:
    expression: str  # normalised, e.g. "2d6+3"
    rolls: list[int]  # each die, in order
    modifier: int
    total: int

    def describe(self) -> str:
        """Human text, e.g. ``2d6+3 -> [4, 6] +3 = 13``."""
        # TODO(Day 2): format rolls, modifier (omit if 0), and total.
        raise NotImplementedError


def parse(expression: str) -> tuple[int, int, int]:
    """Return ``(count, sides, modifier)`` or raise ``ValueError``."""
    # TODO(Day 2):
    #   cleaned = remove all whitespace, lowercase
    #   match = _PATTERN.match(cleaned); if not match -> ValueError("Use NdS+M, e.g. 2d6+3")
    #   count = int(group1) if group1 else 1
    #   enforce 1 <= count <= MAX_DICE and 2 <= sides <= MAX_SIDES (clear messages)
    raise NotImplementedError


def roll(expression: str, rng=random) -> RollResult:
    """Parse ``expression`` and roll it using ``rng.randint``."""
    # TODO(Day 2): count, sides, mod = parse(...); rolls = [rng.randint(1, sides) for _ in range(count)]
    #   build the normalised expression string; total = sum(rolls) + mod
    raise NotImplementedError

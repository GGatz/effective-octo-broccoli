"""Message rule checks for light auto-moderation (Day 7). Tests: ``make day N=7``.

Finished behaviour
------------------
``find_violations(content, mention_count, rules)`` returns a list of
``Violation`` codes (empty list means the message is fine). Pure function: the
cog supplies ``message.content`` and ``len(message.mentions)``.

Rules (all configurable via ``Rules``):

* ``BANNED_WORD``: any banned word appears as a whole word, case-insensitive
  (``"class"`` must not trigger on a banned word ``"ass"``).
* ``MASS_MENTION``: ``mention_count >= max_mentions`` (default 5).
* ``SHOUTING``: content has at least ``min_letters_for_caps`` (default 15)
  letters and more than ``max_caps_ratio`` (default 0.7) of them are uppercase.

The cog decides the *action* (warn, delete, log); this module only decides
*whether* something is wrong. Never auto-ban from a heuristic like this.
"""
import re
from dataclasses import dataclass, field
from enum import Enum


class Violation(Enum):
    BANNED_WORD = "banned_word"
    MASS_MENTION = "mass_mention"
    SHOUTING = "shouting"


@dataclass(frozen=True)
class Rules:
    banned_words: frozenset[str] = field(default_factory=frozenset)
    max_mentions: int = 5
    min_letters_for_caps: int = 15
    max_caps_ratio: float = 0.7


def find_violations(content: str, mention_count: int, rules: Rules) -> list[Violation]:
    # TODO(Day 7):
    #   violations = []
    #   banned: for each word, re.search(rf"\b{re.escape(word)}\b", content, re.IGNORECASE)
    #   mentions: mention_count >= rules.max_mentions
    #   caps: letters = [c for c in content if c.isalpha()]; ratio of c.isupper()
    #   return violations in the enum's declaration order, no duplicates
    raise NotImplementedError

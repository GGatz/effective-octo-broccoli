"""In-memory poll model (Day 5). Tests: ``make day N=5``.

Finished behaviour
------------------
``PollState`` holds a question, 2-5 options, and who voted for what.

* One vote per user. Voting again for a different option *moves* the vote;
  voting again for the same option *retracts* it (toggle).
* ``tally()`` returns counts per option index, including zeros.
* ``leaders()`` returns the indexes tied for most votes (empty list if no votes).
* After ``close()``, ``vote`` raises ``PollClosed``.
* Constructor validates: question non-empty; 2 <= len(options) <= 5; options
  non-empty and unique (case-insensitive). Raises ``ValueError``.

The Discord layer (``cogs/polls.py``) owns buttons and messages; this class
owns the rules. That split is what makes it testable.
"""


class PollClosed(Exception):
    """Raised when voting on a closed poll."""


class PollState:
    MIN_OPTIONS = 2
    MAX_OPTIONS = 5

    def __init__(self, question: str, options: list[str], creator_id: int):
        # TODO(Day 5): validate (see module docstring); store question, options, creator_id,
        #   self.votes: dict[int, int] = {}   # user_id -> option index
        #   self.closed = False
        raise NotImplementedError

    def vote(self, user_id: int, option_index: int) -> str:
        """Apply a vote. Returns ``"added"``, ``"moved"`` or ``"retracted"``."""
        # TODO(Day 5): raise PollClosed if closed; IndexError/ValueError for a bad index;
        #   toggle / move / add as described above.
        raise NotImplementedError

    def tally(self) -> list[int]:
        # TODO(Day 5)
        raise NotImplementedError

    def leaders(self) -> list[int]:
        # TODO(Day 5)
        raise NotImplementedError

    def close(self) -> None:
        # TODO(Day 5)
        raise NotImplementedError

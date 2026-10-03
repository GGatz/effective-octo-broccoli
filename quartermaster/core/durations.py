"""Human duration parsing/formatting (Day 6). Tests: ``make day N=6``.

Finished behaviour
------------------
``parse_duration("1h30m")`` -> ``timedelta(hours=1, minutes=30)``.

* Units: ``d`` days, ``h`` hours, ``m`` minutes, ``s`` seconds. Any subset, in
  any order, case-insensitive, optional spaces: ``"2d 3h"``, ``"90s"``, ``"1H30M"``.
* A bare number is not accepted (ambiguous); raise ``ValueError``.
* Zero or negative totals raise ``ValueError``; so does anything over
  ``MAX_DURATION`` (30 days) or an empty string.

``format_duration(td)`` -> ``"1h 30m"``; omits zero units, shows seconds only
when nothing larger is present or they are non-zero, and returns ``"0s"`` for zero.
"""
import re
from datetime import timedelta

MAX_DURATION = timedelta(days=30)

# Suggested: findall(r"(\d+)\s*([dhms])") and verify the matches consume the whole string.
_PART = re.compile(r"(\d+)\s*([dhms])")


def parse_duration(text: str) -> timedelta:
    # TODO(Day 6):
    #   cleaned = text.strip().lower(); empty -> ValueError
    #   verify the whole string is made of parts: re.fullmatch(r"(?:\d+\s*[dhms]\s*)+", cleaned)
    #   sum the parts using a unit->seconds table; range-check against 0 and MAX_DURATION
    raise NotImplementedError


def format_duration(delta: timedelta) -> str:
    # TODO(Day 6): split total_seconds into d/h/m/s with divmod; join non-zero parts with spaces
    raise NotImplementedError

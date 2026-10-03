import random

import pytest

from quartermaster.core import dice

pytestmark = pytest.mark.day2


class FixedRng:
    """Always returns the same value (clamped to the requested range)."""

    def __init__(self, value: int):
        self.value = value

    def randint(self, a: int, b: int) -> int:
        return max(a, min(b, self.value))


def test_parse_full_expression():
    assert dice.parse("2d6+3") == (2, 6, 3)


def test_parse_defaults_count_to_one():
    assert dice.parse("d20") == (1, 20, 0)


def test_parse_negative_modifier_case_and_spaces():
    assert dice.parse(" 3D8 - 2 ") == (3, 8, -2)


@pytest.mark.parametrize("bad", ["", "hello", "2d", "d", "2d6+", "2d6++1", "0d6", "1d1", "101d6", "1d1001", "-1d6"])
def test_parse_rejects_bad_input(bad):
    with pytest.raises(ValueError):
        dice.parse(bad)


def test_roll_total_with_fixed_rng():
    result = dice.roll("3d6+2", rng=FixedRng(4))
    assert result.rolls == [4, 4, 4]
    assert result.modifier == 2
    assert result.total == 14
    assert result.expression == "3d6+2"


def test_roll_normalises_expression():
    assert dice.roll("D20", rng=FixedRng(1)).expression == "1d20"


def test_roll_rolls_stay_in_range_with_real_rng():
    result = dice.roll("50d10", rng=random.Random(1234))
    assert len(result.rolls) == 50
    assert all(1 <= r <= 10 for r in result.rolls)
    assert result.total == sum(result.rolls)


def test_describe_mentions_rolls_and_total():
    text = dice.roll("2d6+3", rng=FixedRng(5)).describe()
    assert "5" in text and "13" in text

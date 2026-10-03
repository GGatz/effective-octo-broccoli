from datetime import timedelta

import pytest

from quartermaster.core.durations import format_duration, parse_duration

pytestmark = pytest.mark.day6


@pytest.mark.parametrize(
    "text,expected",
    [
        ("90s", timedelta(seconds=90)),
        ("5m", timedelta(minutes=5)),
        ("1h30m", timedelta(hours=1, minutes=30)),
        ("2d 3h", timedelta(days=2, hours=3)),
        ("1H30M", timedelta(hours=1, minutes=30)),
        ("30m1h", timedelta(hours=1, minutes=30)),
        ("  10 s ", timedelta(seconds=10)),
    ],
)
def test_parse_valid(text, expected):
    assert parse_duration(text) == expected


@pytest.mark.parametrize("bad", ["", "   ", "10", "abc", "1x", "0s", "0m0s", "31d", "1h foo", "-5m"])
def test_parse_invalid(bad):
    with pytest.raises(ValueError):
        parse_duration(bad)


def test_max_duration_is_allowed():
    assert parse_duration("30d") == timedelta(days=30)


@pytest.mark.parametrize(
    "delta,expected",
    [
        (timedelta(0), "0s"),
        (timedelta(seconds=45), "45s"),
        (timedelta(minutes=5), "5m"),
        (timedelta(hours=1, minutes=30), "1h 30m"),
        (timedelta(days=2, hours=3, seconds=4), "2d 3h 4s"),
    ],
)
def test_format(delta, expected):
    assert format_duration(delta) == expected


def test_round_trip():
    for text in ["1h 30m", "2d", "45s", "3d 4h 5m 6s"]:
        assert format_duration(parse_duration(text)) == text

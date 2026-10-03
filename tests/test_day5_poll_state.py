import pytest

from quartermaster.core.poll_state import PollClosed, PollState

pytestmark = pytest.mark.day5


def make(options=("Red", "Green", "Blue")):
    return PollState("Favourite colour?", list(options), creator_id=1)


@pytest.mark.parametrize(
    "question,options",
    [
        ("", ["a", "b"]),
        ("q", ["only"]),
        ("q", ["a", "b", "c", "d", "e", "f"]),
        ("q", ["a", ""]),
        ("q", ["a", "A"]),
    ],
)
def test_constructor_validation(question, options):
    with pytest.raises(ValueError):
        PollState(question, options, creator_id=1)


def test_initial_tally_is_zeros():
    assert make().tally() == [0, 0, 0]
    assert make().leaders() == []


def test_vote_add_move_retract():
    p = make()
    assert p.vote(10, 0) == "added"
    assert p.tally() == [1, 0, 0]
    assert p.vote(10, 2) == "moved"
    assert p.tally() == [0, 0, 1]
    assert p.vote(10, 2) == "retracted"
    assert p.tally() == [0, 0, 0]


def test_multiple_voters_and_leaders():
    p = make()
    p.vote(1, 0)
    p.vote(2, 1)
    assert p.leaders() == [0, 1]  # tie
    p.vote(3, 1)
    assert p.leaders() == [1]


def test_bad_option_index():
    p = make()
    with pytest.raises((IndexError, ValueError)):
        p.vote(1, 3)
    with pytest.raises((IndexError, ValueError)):
        p.vote(1, -1)


def test_closed_poll_rejects_votes_but_keeps_tally():
    p = make()
    p.vote(1, 0)
    p.close()
    with pytest.raises(PollClosed):
        p.vote(2, 1)
    assert p.tally() == [1, 0, 0]

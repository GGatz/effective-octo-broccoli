import pytest

from quartermaster.core.automod import Rules, Violation, find_violations

pytestmark = pytest.mark.day7

RULES = Rules(banned_words=frozenset({"ass", "heck"}))


def test_clean_message():
    assert find_violations("Hello there, friends!", 0, RULES) == []


def test_banned_word_whole_word_only():
    assert find_violations("what the HECK", 0, RULES) == [Violation.BANNED_WORD]
    assert find_violations("a classic class assignment", 0, RULES) == []


def test_banned_word_with_punctuation():
    assert find_violations("heck!", 0, RULES) == [Violation.BANNED_WORD]


def test_mass_mention_threshold():
    assert find_violations("hi", 4, RULES) == []
    assert find_violations("hi", 5, RULES) == [Violation.MASS_MENTION]


def test_shouting_needs_enough_letters():
    assert find_violations("HELLO", 0, RULES) == []  # too short to judge
    assert find_violations("THIS IS WAY TOO LOUD FOR ME", 0, RULES) == [Violation.SHOUTING]


def test_mixed_case_is_not_shouting():
    assert find_violations("This Is A Perfectly Normal Title Case Sentence", 0, RULES) == []


def test_multiple_violations_in_declaration_order_without_duplicates():
    out = find_violations("HECK HECK THIS IS ALL CAPS NOW", 9, RULES)
    assert out == [Violation.BANNED_WORD, Violation.MASS_MENTION, Violation.SHOUTING]


def test_regex_metacharacters_in_banned_words_are_escaped():
    rules = Rules(banned_words=frozenset({"c++"}))
    # An unescaped "c++" is an invalid regex ("multiple repeat") and would raise re.error.
    assert find_violations("plain text", 0, rules) == []

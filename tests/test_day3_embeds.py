import discord
import pytest

from quartermaster.core import embeds

pytestmark = pytest.mark.day3


def test_truncate_short_text_unchanged():
    assert embeds.truncate("hello", 10) == "hello"


def test_truncate_long_text_ends_with_ellipsis_and_respects_limit():
    out = embeds.truncate("x" * 50, 10)
    assert len(out) == 10
    assert out.endswith("…")


def test_make_embed_defaults():
    e = embeds.make_embed("Title", "Body")
    assert isinstance(e, discord.Embed)
    assert e.title == "Title"
    assert e.description == "Body"
    assert e.color == discord.Color.blurple()
    assert e.footer.text == "Quartermaster"


@pytest.mark.parametrize("kind", ["info", "success", "warning", "error"])
def test_each_kind_has_a_color(kind):
    assert embeds.make_embed("t", kind=kind).color == embeds.COLORS[kind]


def test_unknown_kind_raises():
    with pytest.raises(ValueError):
        embeds.make_embed("t", kind="purple")


def test_limits_enforced():
    e = embeds.make_embed("t" * 500, "d" * 5000)
    assert len(e.title) <= 256
    assert len(e.description) <= 4096


def test_fields_added():
    e = embeds.make_embed("t", fields=[("a", "1", True), ("b", "2", False)])
    assert [(f.name, f.value, f.inline) for f in e.fields] == [("a", "1", True), ("b", "2", False)]

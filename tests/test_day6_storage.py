import asyncio
from datetime import datetime, timedelta, timezone

import pytest

from quartermaster.core.storage import ReminderStore

pytestmark = pytest.mark.day6

NOW = datetime(2026, 1, 1, 12, 0, tzinfo=timezone.utc)


def run(coro):
    return asyncio.run(coro)


def test_add_and_list_for_user():
    async def scenario():
        store = await ReminderStore.open(":memory:")
        rid = await store.add(1, 100, "stretch", NOW + timedelta(hours=1))
        await store.add(2, 100, "other user", NOW + timedelta(hours=2))
        mine = await store.list_for_user(1)
        await store.close()
        return rid, mine

    rid, mine = run(scenario())
    assert len(mine) == 1
    assert mine[0].id == rid
    assert mine[0].message == "stretch"
    assert mine[0].due_at == NOW + timedelta(hours=1)
    assert mine[0].due_at.tzinfo is not None


def test_due_returns_only_past_ones_oldest_first():
    async def scenario():
        store = await ReminderStore.open(":memory:")
        await store.add(1, 1, "later", NOW + timedelta(hours=1))
        await store.add(1, 1, "second", NOW - timedelta(minutes=1))
        await store.add(1, 1, "first", NOW - timedelta(hours=1))
        due = await store.due(NOW)
        await store.close()
        return due

    assert [r.message for r in run(scenario())] == ["first", "second"]


def test_delete_respects_ownership():
    async def scenario():
        store = await ReminderStore.open(":memory:")
        rid = await store.add(1, 1, "mine", NOW)
        stolen = await store.delete(rid, user_id=2)
        still_there = await store.list_for_user(1)
        deleted = await store.delete(rid, user_id=1)
        gone = await store.list_for_user(1)
        missing = await store.delete(rid)
        await store.close()
        return stolen, len(still_there), deleted, len(gone), missing

    assert run(scenario()) == (False, 1, True, 0, False)


def test_naive_datetime_rejected():
    async def scenario():
        store = await ReminderStore.open(":memory:")
        try:
            await store.add(1, 1, "x", datetime(2026, 1, 1, 12, 0))
        finally:
            await store.close()

    with pytest.raises(ValueError):
        run(scenario())


def test_message_with_sql_metacharacters_is_stored_verbatim():
    nasty = "'); DROP TABLE reminders; --"

    async def scenario():
        store = await ReminderStore.open(":memory:")
        await store.add(1, 1, nasty, NOW)
        out = await store.list_for_user(1)
        await store.close()
        return out

    assert run(scenario())[0].message == nasty


def test_persists_across_reopen(tmp_path):
    path = str(tmp_path / "r.sqlite3")

    async def scenario():
        store = await ReminderStore.open(path)
        await store.add(1, 1, "survive", NOW)
        await store.close()
        store2 = await ReminderStore.open(path)
        out = await store2.list_for_user(1)
        await store2.close()
        return out

    assert [r.message for r in run(scenario())] == ["survive"]

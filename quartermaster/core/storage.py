"""SQLite persistence for reminders (Day 6). Tests: ``make day N=6``.

Finished behaviour
------------------
``ReminderStore`` wraps an ``aiosqlite`` connection. Why ``aiosqlite``: the
stdlib ``sqlite3`` API is blocking, and a blocking call inside the event loop
freezes the whole bot (heartbeats included). ``aiosqlite`` runs queries on a
worker thread and exposes ``await``-able methods.

Schema::

    CREATE TABLE IF NOT EXISTS reminders (
        id         INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id    INTEGER NOT NULL,
        channel_id INTEGER NOT NULL,
        message    TEXT    NOT NULL,
        due_at     TEXT    NOT NULL   -- ISO-8601 UTC, e.g. 2026-01-01T12:00:00+00:00
    );

All datetimes are timezone-aware UTC. Naive datetimes raise ``ValueError``.
Pass ``":memory:"`` as the path in tests.

API (all coroutines except the dataclass):

* ``ReminderStore.open(path)`` -> store (creates the table)
* ``add(user_id, channel_id, message, due_at)`` -> new reminder id
* ``due(now)`` -> reminders with ``due_at <= now``, oldest first
* ``list_for_user(user_id)`` -> that user's reminders, soonest first
* ``delete(reminder_id, user_id=None)`` -> True if a row was deleted; when
  ``user_id`` is given, only deletes if it owns the reminder
* ``close()``
"""
from dataclasses import dataclass
from datetime import datetime

import aiosqlite  # noqa: F401  (used once you implement the store)


@dataclass(frozen=True)
class Reminder:
    id: int
    user_id: int
    channel_id: int
    message: str
    due_at: datetime


class ReminderStore:
    def __init__(self, conn: aiosqlite.Connection):
        self._conn = conn

    @classmethod
    async def open(cls, path: str) -> "ReminderStore":
        # TODO(Day 6): conn = await aiosqlite.connect(path); execute CREATE TABLE; commit
        raise NotImplementedError

    async def add(self, user_id: int, channel_id: int, message: str, due_at: datetime) -> int:
        # TODO(Day 6): reject naive datetimes; INSERT with parameters (never f-strings!); commit; return cursor.lastrowid
        raise NotImplementedError

    async def due(self, now: datetime) -> list[Reminder]:
        # TODO(Day 6): ISO strings in one fixed format and timezone sort lexicographically,
        #   so `WHERE due_at <= ?` works; ORDER BY due_at
        raise NotImplementedError

    async def list_for_user(self, user_id: int) -> list[Reminder]:
        # TODO(Day 6)
        raise NotImplementedError

    async def delete(self, reminder_id: int, user_id: int | None = None) -> bool:
        # TODO(Day 6): DELETE ... WHERE id = ? [AND user_id = ?]; return cursor.rowcount > 0
        raise NotImplementedError

    async def close(self) -> None:
        # TODO(Day 6)
        raise NotImplementedError

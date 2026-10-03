# Architecture (finished bot)

```
                 Discord
          ┌─────────┴─────────┐
      Gateway (ws)         REST (https)
   events pushed to us    we call it to act
          └─────────┬─────────┘
                    │  discord.py (event loop, caching, rate limits)
            ┌───────┴────────┐
            │ QuartermasterBot│  bot.py: intents, setup_hook, error handling
            └───────┬────────┘
   ┌────────┬───────┼─────────┬────────────┐
 General  Admin   Polls   Reminders   Moderation      quartermaster/cogs/*
   │        │       │         │            │
   │        │   PollState  ReminderStore  automod     quartermaster/core/*  (pure logic)
   │        │       │         │ (aiosqlite)
   embeds, dice, durations ...                   SQLite file
```

## Principles

1. **Decisions in `core/`, plumbing in `cogs/`.** Core modules never touch the
   network and are unit-tested. Cogs translate between Discord objects and core calls.
2. **One composition root.** `__main__` builds config → logging → bot. Cogs
   receive the bot and read what they need (`bot.config`, `bot.store`).
3. **Startup in `setup_hook`**, not `on_ready`.
4. **Never block the event loop.** All I/O is awaited; blocking work goes to `asyncio.to_thread`.
5. **Fail soft toward users, loud toward logs.** Users get short messages
   (usually ephemeral); the log gets tracebacks.
6. **Least privilege** for intents, invite permissions and command checks.

## Data

* SQLite file (`DATABASE_PATH`), table `reminders` (see `core/storage.py`).
* Polls are in memory (stretch: persist them).

## Request flows

*Prefix command:* gateway `MESSAGE_CREATE` → `Bot.on_message` → `process_commands` → converters → command → `ctx.send` (REST).

*Slash command:* gateway `INTERACTION_CREATE` → `CommandTree` → checks → callback → `interaction.response.*` (≤3 s) → optional `followup`.

*Button click:* `INTERACTION_CREATE` (component) → `View` dispatch by `custom_id` → callback → `response.edit_message`.

*Reminder:* `tasks.loop` tick → `store.due(now)` → send → `store.delete`.

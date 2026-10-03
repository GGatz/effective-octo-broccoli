# Day 7 — Guardrails and shipping (≈2.5 h)

**Goal:** member events, automod, a safe `/purge`, and a container you can deploy. `make day N=7` green.

| Block | Time |
|---|---|
| `automod.py` to green | 30 min |
| Welcome + automod listeners | 40 min |
| `/purge`, permission checks, error handler | 40 min |
| Dockerfile, README run notes, retro | 40 min |

## Concepts

* **Least privilege**, twice: request only the intents you use (Members and
  Message Content are privileged, and verification is required past 100
  servers), and ask for only the permissions you need in the invite URL.
* **User permission vs bot permission.** `has_permissions` checks the invoker;
  `bot_has_permissions` checks the bot in that channel. Channel overwrites can
  differ from server-wide role permissions.
* **Server-side defaults.** `@app_commands.default_permissions(...)` hides a
  command from most users in the UI, but is *not* a security boundary. Always keep the runtime check.
* **Rate limits.** discord.py queues around 429s for you, but bulk loops
  (mass DMs, reacting in a loop) can still get an app flagged. Prefer
  `channel.purge` (bulk delete, only for messages under 14 days old).
* **Heuristic moderation** produces false positives: warn, log, never auto-ban.
* **Shipping**: pin dependencies, run as non-root, secrets via environment,
  persistent volume for SQLite, restart policy.

## Steps

1. `core/automod.py` to green (watch the regex-escaping and whole-word tests).
2. Moderation cog: `on_member_join`, `on_message` (skip bots, exempt Manage Messages), `/purge` with both permission checks, `defer`, and cooldown.
3. Error handler turning `MissingPermissions`, `BotMissingPermissions`, `CommandOnCooldown` into ephemeral messages.
4. Enable the Members intent in `bot.py` and the portal. Add `moderation` to `COGS`.
5. Write a `Dockerfile` (stub provided) and run `docker build .` (or review it if Docker isn't available).
6. Retrospective in `PROGRESS.md`.

## Read

`discord.Intents`, `app_commands.checks`, `Permissions`, `TextChannel.purge`,
`on_member_join`; Discord's developer docs on rate limits and on privileged intents.

## If you're stuck

* `on_member_join` never fires: Members intent off in portal or code.
* `/purge` "Missing Access": the bot lacks View Channel / Manage Messages in *that channel*.
* Interaction timeouts on purge: `defer(ephemeral=True)` first.

## Done when

- [ ] `make day N=7` green
- [ ] Join (use an alt) → welcome message; shouting/mass-mention → warning
- [ ] `/purge` refused for a normal user and for a bot lacking permission
- [ ] `docker build` succeeds
- [ ] Tagged `day-07-done`; retrospective filled in

## Where to go next

Sharding and `AutoShardedBot` (only past ~2,000 guilds), a web dashboard with
OAuth2, voice (needs `discord.py[voice]` and `ffmpeg`), tests that mock
`Interaction` objects (`dpytest` or hand-rolled fakes), persistent views,
or structured logging/metrics.

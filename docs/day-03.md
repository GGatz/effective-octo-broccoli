# Day 3 — Slash commands & embeds (≈2 h)

**Goal:** `/ping`, `/roll`, `/about`, `/userinfo` as slash commands with
embeds; `make day N=3` green.

| Block | Time |
|---|---|
| Embed helper to green tests | 25 min |
| Read: app commands, interactions | 25 min |
| Slash commands + autocomplete | 45 min |
| Syncing experiments, polish | 25 min |

## Concepts

* **Interactions ≠ messages.** A slash command arrives as an *interaction* via
  the gateway (or webhook). You must **respond within 3 seconds**
  (`interaction.response.send_message`) or `defer()` to get 15 minutes, then
  use `interaction.followup`. Each interaction can have only one initial response.
* **The command tree.** Slash commands are *registered with Discord*, not
  discovered from messages. `bot.tree.sync()` uploads your definitions.
* **Syncing, the #1 gotcha.** Global sync can take up to an hour to show up
  everywhere; **guild** sync is instant. During development:
  `bot.tree.copy_global_to(guild=g); await bot.tree.sync(guild=g)`. Sync only
  when definitions change, not on every start in production (rate limits).
* **Typed parameters.** Annotations → option types; `@app_commands.describe`
  → help text; `Choice`/`@app_commands.choices` → fixed lists; `autocomplete`
  → dynamic suggestions as the user types.
* **Ephemeral** replies are visible only to the invoker (`ephemeral=True`).
* **Hybrid commands** (`@commands.hybrid_command`) give prefix + slash from
  one function. Convenient, but write slash commands by hand first.

## Steps

1. `core/embeds.py`: `truncate`, `make_embed`; tests green.
2. In `setup_hook`: sync to `DEV_GUILD_ID` when set. The Applications Commands
   scope (`applications.commands`) is included with the normal bot invite for
   new apps; if commands don't appear, re-invite with that scope.
3. Add `/ping`, `/roll` (with `autocomplete`), `/about`, `/userinfo` per the
   docstring in `cogs/general.py`. You may still keep them in `bot.py` until Day 4.
4. Deliberately take >3 s in a command (`await asyncio.sleep(4)`), see the
   "application did not respond" error, then fix with `defer()`.

## Read

*Application Commands* section of the docs: `app_commands.command`,
`describe`, `choices`, autocomplete, `Interaction` (and `InteractionResponse`),
`discord.Embed`.

## If you're stuck

* Commands missing: wrong guild ID, didn't sync, or client not restarted.
* "Unknown interaction": you took too long; defer sooner.
* Embed rejected: a field or total exceeded Discord's limits (6000 chars total).

## Done when

- [ ] `make day N=3` green
- [ ] All four slash commands work; `/roll` autocomplete suggests expressions
- [ ] You can explain the 3-second rule and when to `defer`
- [ ] Tagged `day-03-done`

## Stretch

A context-menu command (`@app_commands.context_menu`) "Account age" on a user.

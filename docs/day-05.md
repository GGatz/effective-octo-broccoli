# Day 5 — Interactive UI: buttons, selects, modals (≈2.5 h)

**Goal:** `/poll create` opens a modal, posts a poll with buttons, tallies
live, and closes cleanly. `make day N=5` green.

| Block | Time |
|---|---|
| `PollState` to green tests | 35 min |
| Read: UI Kit (View, Button, Modal) | 25 min |
| Modal + view + embed rendering | 60 min |
| Close button, timeout, edge cases | 30 min |

## Concepts

* **Components** are interactive widgets attached to messages. A click is
  delivered as an interaction with a `custom_id` that identifies the widget.
* **`discord.ui.View`** is discord.py's local state machine for those widgets:
  it routes interactions to your callbacks, enforces a `timeout`, and holds
  Python state. Because that state lives in memory, views die on restart
  *unless* made persistent (`timeout=None`, fixed `custom_id`s, `bot.add_view`).
* **Callback responses.** Every callback must respond once: `response.send_message`,
  `response.edit_message` (update the original message), or `defer()`.
  `followup.send` after that.
* **Authorization is your job.** Anyone who can see the message can click.
  Check `interaction.user.id` inside callbacks (creator-only Close).
* **Modal** = popup form (`discord.ui.Modal` with `TextInput`s); must be the
  *first* response to an interaction (`response.send_modal`).
* **Newer API note.** discord.py 2.6+ added "Components V2" (`LayoutView`)
  for richer message layouts. The classic `View` used here is still supported;
  skim the docs' changelog before the stretch task to see whether the newer
  API suits you better. Verify against current docs; this area evolves fast.

## Steps

1. `core/poll_state.py`: implement until green.
2. `PollModal` (question + options paragraph) → `PollState`; reply ephemerally on `ValueError`.
3. `PollView`: dynamic buttons (one per option; careful with closures over the loop variable), a red Close button.
4. `render_poll_embed(state)`: option lines with bars (`█`/`░`) and counts.
5. Vote callback → `state.vote` → `interaction.response.edit_message(embed=..., view=self)`; send the vote feedback as an ephemeral followup.
6. Close: creator only; disable children, `state.close()`, final embed. `on_timeout`: same cleanup using the stored message (`view.message`).

## Read

*UI Kit* in the docs: `View`, `Button`, `Select`, `Modal`, `TextInput`;
`Interaction.response` methods; `Message.edit`.

## If you're stuck

* "This interaction failed": a callback raised or never responded; check logs.
* Late-binding closure bug (all buttons vote for the last option): bind the index as a default arg or use `functools.partial`.
* Buttons dead after restart: expected (see Concepts); stretch goal fixes it.

## Done when

- [ ] `make day N=5` green
- [ ] Two accounts (or alt) can vote; moving/retracting a vote works; counts update
- [ ] Non-creator pressing Close is refused politely
- [ ] After close or timeout, buttons are disabled
- [ ] You can explain `custom_id`, view timeout, and `response` vs `followup`
- [ ] Tagged `day-05-done`

## Stretch

Make polls persistent: store polls in SQLite, `timeout=None`, `custom_id=f"poll:{id}:{i}"`,
re-register views in `setup_hook`. Or replace buttons with a `Select` for multi-choice polls.

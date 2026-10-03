# Day 1 — Hello, gateway (≈1.5 h)

**Goal:** a bot user that is online in your test server, logs when it connects,
and replies "pong" when someone says "ping".

| Block | Time |
|---|---|
| Portal + server setup | 30 min |
| Read: intro and quickstart | 15 min |
| Code `__main__.py` / `config.py` | 30 min |
| Experiments and "Done when" | 15 min |

## Concepts

* **Two channels to Discord.** A **REST API** (HTTPS: send a message, fetch a
  user) and the **Gateway** (a long-lived websocket Discord pushes *events*
  to: message created, member joined, ...). discord.py hides both: you write
  `await channel.send(...)` (REST) and `async def on_message` (gateway).
* **Intents** declare which gateway events you want. Some are *privileged*
  (Message Content, Server Members, Presence) and must be enabled in the portal
  and in code. If your bot connects but can't see message text, it's this.
* **Token** = the bot's password. Never commit it.
* **Event loop.** `client.run()` starts an asyncio loop and blocks. Callbacks
  like `on_message` are coroutines run by that loop.

## Steps

1. Discord → create a throwaway server. Settings → Advanced → enable Developer Mode.
2. https://discord.com/developers/applications → New Application → Bot tab →
   Reset Token (copy once) → enable **Message Content Intent**.
3. OAuth2 → URL Generator → scope `bot`; permissions: View Channels, Send
   Messages, Read Message History. Open the URL, add to your server.
4. `cp .env.example .env`, paste the token. Confirm `git status` doesn't list `.env`.
5. Implement in `quartermaster/__main__.py` (use `config.py` for the token):
   ```python
   intents = discord.Intents.default()
   intents.message_content = True
   client = discord.Client(intents=intents)

   @client.event
   async def on_ready(): ...
   @client.event
   async def on_message(message): ...   # ignore message.author == client.user
   client.run(token)
   ```
   Note `main()` in the stub is async; for Day 1 it is simpler to call
   `client.run` from plain synchronous code. Adjust the stub; the finished
   structure returns on Day 4.
6. `python -m quartermaster`; say "ping" in the server.

## Read

discord.py docs: *Introduction*, *Quickstart*, *Setting Up Logging*, and the
*Intents* primer. API reference: `discord.Client`, `on_ready`, `on_message`.

## Experiments (10 min, worth doing)

* Remove `message_content` and watch `message.content` go empty.
* Remove the "ignore own messages" guard, think about what happens, then
  (carefully) try it with a bot that replies to anything.
* Log `on_ready` and kill your wifi briefly: it can fire again on reconnect.

## If you're stuck

* `LoginFailure`: token wrong or has a trailing space/newline.
* `PrivilegedIntentsRequired`: toggle the intent in the portal.
* Online but silent: bot lacks View Channel / Send Messages in that channel.

## Done when

- [ ] Bot shows online; terminal prints its name and guild count
- [ ] "ping" → "pong", and the bot doesn't reply to itself
- [ ] You can explain gateway vs REST and what an intent is
- [ ] Committed on branch `day-01`, merged, tagged `day-01-done`

## Stretch

React with an emoji to messages containing "hello" (`message.add_reaction`).

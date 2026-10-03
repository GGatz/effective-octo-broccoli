"""Typed configuration loaded from environment variables (and ``.env``).

Finished behaviour
------------------
``load_config()`` returns a frozen ``Config`` dataclass. Required: DISCORD_TOKEN.
Everything else has a default (see ``.env.example``). If the token is missing it
raises ``SystemExit`` with a one-line, human-friendly message, not a traceback.

Why a dataclass and not ``os.environ`` everywhere? One place to validate, one
place to document, and tests can construct a ``Config`` directly.

Introduced Day 1 (token only), completed Day 4.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class Config:
    token: str
    command_prefix: str = "!"
    dev_guild_id: int | None = None
    owner_id: int | None = None
    log_level: str = "INFO"
    database_path: str = "quartermaster.sqlite3"


def load_config() -> Config:
    # TODO(Day 1/4):
    #   from dotenv import load_dotenv; load_dotenv()      # reads .env if present
    #   token = os.environ.get("DISCORD_TOKEN")
    #   if not token: raise SystemExit("DISCORD_TOKEN is not set; see .env.example")
    #   dev_guild_id = int(raw) if (raw := os.environ.get("DEV_GUILD_ID")) else None
    #   ... same for OWNER_ID; strings for the rest
    #   return Config(...)
    raise NotImplementedError

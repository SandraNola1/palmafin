from dataclasses import dataclass
from os import getenv
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Config:
    bot_token: str = ""
    webapp_url: str = ""
    database_url: str = ""
    admin_ids: list = None

    def __post_init__(self):
        self.bot_token = getenv("BOT_TOKEN", "")
        self.webapp_url = getenv("WEBAPP_URL", "")
        self.database_url = getenv("DATABASE_URL", "palmafin.db")
        raw = getenv("ADMIN_IDS", "")
        self.admin_ids = [int(x) for x in raw.split(",") if x.strip().isdigit()]

        if not self.bot_token:
            raise RuntimeError("BOT_TOKEN не задан")
        if not self.webapp_url:
            raise RuntimeError("WEBAPP_URL не задан — нужен URL задеплоенного Mini App")

config = Config()

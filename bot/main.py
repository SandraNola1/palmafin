import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Message, WebAppInfo
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder
from config import config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("palmafin")

bot = Bot(token=config.bot_token)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    builder = InlineKeyboardBuilder()
    builder.button(
        text="🧠 Открыть Штаб-квартиру",
        web_app=WebAppInfo(url=config.webapp_url)
    )
    await message.answer(
        "👋 Добро пожаловать в <b>Palmafin</b>\n\n"
        "Твоя личная штаб-квартира — все агенты, финансы и проекты в одном месте.",
        reply_markup=builder.as_markup(),
        parse_mode="HTML"
    )

async def main():
    logger.info("Palmafin bot started")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

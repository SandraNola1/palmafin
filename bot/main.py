import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Message, WebAppInfo, MenuButtonWebApp, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder
from config import config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("palmafin")

bot = Bot(token=config.bot_token)
dp = Dispatcher()

WEBAPP_URL = "https://sandranola1.github.io/palmafin/"

@dp.message(CommandStart())
async def start(message: Message):
    # Кнопка меню — открывает Mini App автоматически
    await bot.set_chat_menu_button(
        chat_id=message.chat.id,
        menu_button=MenuButtonWebApp(text="🧠 Штаб", web_app=WebAppInfo(url=WEBAPP_URL))
    )
    # Клавиатура с большой кнопкой
    kb = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="🚀 Открыть Штаб-квартиру", web_app=WebAppInfo(url=WEBAPP_URL))]],
        resize_keyboard=True
    )
    await message.answer(
        "👋 Добро пожаловать в <b>Palmafin</b>\n\n"
        "Твоя штаб-квартира — все агенты, финансы и проекты в одном месте.\n\n"
        "Нажми кнопку ниже или кнопку меню слева ↙️",
        reply_markup=kb,
        parse_mode="HTML"
    )

async def main():
    # Устанавливаем кнопку меню глобально для всех чатов
    await bot.set_my_commands([])
    try:
        await bot.set_chat_menu_button(
            menu_button=MenuButtonWebApp(text="🧠 Штаб", web_app=WebAppInfo(url=WEBAPP_URL))
        )
    except Exception:
        pass
    logger.info("Palmafin bot started")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

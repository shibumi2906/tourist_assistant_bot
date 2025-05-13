import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties

from config import TELEGRAM_TOKEN
from logger import logger
from handlers import routers
from middleware.language_selector import LanguageMiddleware

# Современный способ инициализации бота
bot = Bot(
    token=TELEGRAM_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

dp = Dispatcher(storage=MemoryStorage())

# Middleware: язык
dp.message.middleware(LanguageMiddleware())
dp.callback_query.middleware(LanguageMiddleware())


async def main():
    logger.info("Инициализация Telegram-бота")

    for router in routers:
        dp.include_router(router)

    logger.info("Бот запущен. Ожидаем сообщения...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.warning("Бот остановлен вручную.")

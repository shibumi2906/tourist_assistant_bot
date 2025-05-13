import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from config import TELEGRAM_TOKEN
from logger import logger
from handlers import routers
from middleware.language_selector import LanguageMiddleware

# Инициализация бота и диспетчера
bot = Bot(token=TELEGRAM_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=MemoryStorage())

# Подключение middleware (язык)
dp.message.middleware(LanguageMiddleware())
dp.callback_query.middleware(LanguageMiddleware())


async def main():
    logger.info("Инициализация Telegram-бота")

    # Регистрация всех роутеров
    for router in routers:
        dp.include_router(router)

    logger.info("Бот запущен. Ожидаем сообщения...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.warning("Бот остановлен вручную.")


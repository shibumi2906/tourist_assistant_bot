import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from config import TELEGRAM_TOKEN
from logger import logger
from handlers import routers


async def main():
    logger.info("Инициализация бота...")

    bot = Bot(token=TELEGRAM_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()

    # Регистрируем все роутеры
    for router in routers:
        dp.include_router(router)

    logger.info("Бот запущен. Ожидаем сообщения...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.warning("Бот остановлен вручную.")


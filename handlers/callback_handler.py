from aiogram import Router
from aiogram.types import CallbackQuery
from logger import logger

callback_router = Router()

@callback_router.callback_query()
async def handle_callbacks(callback: CallbackQuery):
    logger.info(f"Callback: {callback.data} от {callback.from_user.id}")
    await callback.answer("Функция пока не реализована.")

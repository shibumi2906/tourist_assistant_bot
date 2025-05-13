from aiogram import Router, F
from aiogram.types import Message
from logger import logger

message_router = Router()

@message_router.message(F.text)
async def handle_user_text(message: Message):
    logger.debug(f"Сообщение от пользователя: {message.text}")
    await message.answer("Вы написали: " + message.text)

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from logger import logger

command_router = Router()

@command_router.message(CommandStart())
async def handle_start(message: Message):
    logger.info(f"/start от пользователя {message.from_user.id}")
    await message.answer("Привет! Я ваш туристический помощник 🤖")

@command_router.message(Command("help"))
async def handle_help(message: Message):
    await message.answer("Напиши, что ты хочешь: найти отель, маршрут, музей или купить билет.")

@command_router.message(Command("language"))
async def handle_language(message: Message):
    await message.answer("Выберите язык:\n🇷🇺 Русский\n🇬🇧 English\n(пока не реализовано)")

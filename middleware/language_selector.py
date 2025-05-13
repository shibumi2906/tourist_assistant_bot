from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery
from typing import Callable, Awaitable, Dict, Any
from aiogram.fsm.context import FSMContext
from config import DEFAULT_LANGUAGE


class LanguageMiddleware(BaseMiddleware):
    def __init__(self):
        self.default_lang = DEFAULT_LANGUAGE

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message | CallbackQuery,
        data: Dict[str, Any]
    ) -> Any:
        state: FSMContext = data.get("state")
        if not state:
            return await handler(event, data)

        user_data = await state.get_data()
        lang = user_data.get("lang")

        # Если язык ещё не установлен — используем язык Telegram, либо дефолт
        if not lang:
            telegram_lang = getattr(event.from_user, "language_code", None)
            lang = telegram_lang if telegram_lang in ["ru", "en"] else self.default_lang
            await state.update_data(lang=lang)

        data["lang"] = lang  # прокидываем в хендлеры
        return await handler(event, data)

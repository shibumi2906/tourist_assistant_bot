from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_confirmation_keyboard(yes_text: str = "✅ Да", no_text: str = "❌ Нет") -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=yes_text, callback_data="confirm_yes"),
                InlineKeyboardButton(text=no_text, callback_data="confirm_no")
            ]
        ]
    )


def get_booking_confirm_keyboard(link: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🔗 Перейти к бронированию", url=link)
            ],
            [
                InlineKeyboardButton(text="❌ Отмена", callback_data="cancel")
            ]
        ]
    )

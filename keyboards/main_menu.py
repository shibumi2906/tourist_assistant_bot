from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_language_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🇷🇺 Русский"), KeyboardButton(text="🇬🇧 English")]
        ],
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Выберите язык / Choose language"
    )


def get_main_menu_keyboard(lang: str = "ru") -> ReplyKeyboardMarkup:
    if lang == "en":
        buttons = [
            ["🏨 Find hotel", "📍 Attractions"],
            ["🗺️ Route", "✈️ Tickets"],
            ["🌐 Change language"]
        ]
    else:
        buttons = [
            ["🏨 Найти отель", "📍 Достопримечательности"],
            ["🗺️ Маршрут", "✈️ Билеты"],
            ["🌐 Сменить язык"]
        ]

    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=b) for b in row] for row in buttons],
        resize_keyboard=True
    )

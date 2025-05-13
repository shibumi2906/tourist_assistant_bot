from aiogram import Router, F
from aiogram.types import Message
from logger import logger

from services.nlp.intent_classifier import detect_intent
from services.bookings.booking_link import generate_booking_url
from keyboards.confirmation import get_booking_confirm_keyboard

message_router = Router()


@message_router.message(F.text)
async def handle_user_text(message: Message, lang: str):
    user_input = message.text.strip()
    logger.info(f"Получено сообщение: {user_input}")

    # Распознавание намерения через GPT
    try:
        intent_data = await detect_intent(user_input)
    except Exception as e:
        logger.exception("Ошибка при анализе намерения")
        await message.answer("Произошла ошибка при анализе запроса 😔")
        return

    intent = intent_data.get("intent", "unknown")
    params = intent_data.get("params", {})

    logger.info(f"Распознан intent: {intent}, параметры: {params}")

    # 👉 Обработка намерений
    if intent == "find_hotels":
        city = params.get("city")
        checkin = params.get("checkin")
        checkout = params.get("checkout")
        adults = params.get("adults", 2)

        if not city:
            await message.answer("Уточните, пожалуйста, в каком городе вы хотите найти отель 🏨")
            return

        url = generate_booking_url(city=city, checkin=checkin, checkout=checkout, adults=adults)

        await message.answer(
            f"Вот ссылка на поиск отелей в {city.title()} 👇",
            reply_markup=get_booking_confirm_keyboard(link=url)
        )

    elif intent == "book_tickets":
        await message.answer("✈️ Ищу билеты... (логика будет добавлена)")

    elif intent == "search_attractions":
        city = params.get("city")
        if city:
            await message.answer(f"📍 Достопримечательности в {city.title()} (будет вызов GPT или API)")
        else:
            await message.answer("Уточните, пожалуйста, какой город вас интересует для достопримечательностей.")

    elif intent == "plan_route":
        await message.answer("🗺️ Сейчас составим маршрут...")

    elif intent == "translate_phrase":
        await message.answer("🌐 Перевожу фразу...")

    else:
        await message.answer("Я пока не понял, что вы хотите 😅 Попробуйте переформулировать.")


# tourist_assistant_bot
 tourist_assistant_bot
* tourist_assistant_bot/
* ├── main.py                    # Точка входа, инициализация бота
* ├── config.py                  # Настройки: токены, API ключи, переменные окружения
* ├── logger.py                  # Настройка логгера loguru
* ├── handlers/
* │   ├── __init__.py
* │   ├── message_handler.py     # Обработка всех входящих сообщений
* │   ├── callback_handler.py    # Обработка инлайн-кнопок
* │   └── command_handler.py     # Обработка команд: /start, /help, /language и т.д.
* ├── services/
* │   ├── __init__.py
* │   ├── bookings/
* │   │   ├── __init__.py
* │   │   ├── ostrovok.py        # Интеграция с Ostrovok.ru
* │   │   ├── yandex.py          # Интеграция с Яндекс.Путешествия
* │   │   ├── hotellook.py       # Интеграция с Hotellook (международный)
* │   │   ├── booking_link.py    # Генерация deeplink Booking.com
* │   ├── flights/
* │   │   ├── __init__.py
* │   │   ├── aviasales.py       # Ссылки или API Aviasales
* │   │   ├── kiwi.py            # Генерация ссылок через Kiwi
* │   │   └── skyscanner.py      # (Опционально) API Skyscanner
* │   ├── transport/
* │   │   ├── trains.py          # Ссылки/интеграция RZD, Tutu
* │   │   └── buses.py           # Flixbus, Busfor, Omio
* │   ├── attractions/
* │   │   ├── __init__.py
* │   │   ├── gpt_recommender.py # GPT-подсказки с запросами по городу
* │   │   ├── opentrip.py        # Интеграция с OpenTripMap API
* │   │   └── local_cache.py     # Кэш популярных городов
* │   ├── routing/
* │   │   ├── maps.py            # Генерация маршрутов (Google / Yandex)
* │   │   └── location_utils.py  # Определение ближайших узлов, проверка РФ/не РФ
* │   └── nlp/
* │       ├── __init__.py
* │       ├── intent_classifier.py # GPT-анализ намерений
* │       └── prompt_templates.py  # Шаблоны для ChatGPT
* ├── middleware/
* │   ├── __init__.py
* │   ├── session_manager.py     # FSM / контекст диалога
* │   └── language_selector.py   # Обработка языка и переводов
* ├── keyboards/
* │   ├── __init__.py
* │   ├── main_menu.py
* │   └── confirmation.py        # Инлайн-кнопки подтверждений
* ├── data/
* │   ├── __init__.py
* │   ├── constants.py           # Список стран, кодов, интересов и т.д.
* │   └── cities_db.json         # Кэшированные данные по городам
* ├── utils/
* │   ├── __init__.py
* │   ├── text_cleaning.py       # Очистка и нормализация входящего текста
* │   └── date_parser.py         # Разбор дат из запроса
* ├── requirements.txt
* ├── README.md
* └── .env                       # Переменные окружения (не в репозиторий)
* 


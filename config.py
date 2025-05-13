import os
from dotenv import load_dotenv

load_dotenv()

# Базовые переменные окружения
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Флаг режима отладки
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

# Язык по умолчанию
DEFAULT_LANGUAGE = os.getenv("DEFAULT_LANGUAGE", "ru")

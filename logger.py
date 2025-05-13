from loguru import logger
import sys
from config import DEBUG

# Удаляем дефолтные обработчики
logger.remove()

# Настройка логгера
logger.add(
    sys.stdout,
    format="<green>{time:HH:mm:ss}</green> | "
           "<level>{level: <8}</level> | "
           "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
           "<level>{message}</level>",
    level="DEBUG" if DEBUG else "INFO"
)

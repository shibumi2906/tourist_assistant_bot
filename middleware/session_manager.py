from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


# Используется в main.py: dp = Dispatcher(storage=MemoryStorage())

class UserSession(StatesGroup):
    main = State()       # Пример: для логики /start
    waiting_input = State()  # Для дальнейших переходов

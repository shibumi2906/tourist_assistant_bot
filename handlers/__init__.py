from .command_handler import command_router
from .message_handler import message_router
from .callback_handler import callback_router

# Все маршруты объединяются в этом списке
routers = [
    command_router,
    message_router,
    callback_router
]

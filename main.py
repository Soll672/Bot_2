import os
from aiogram import Bot, Dispatcher
from aiogram.utils import executor
from dotenv import load_dotenv
from handlers import start_handler, info_handler, random_handler, callback_handlers

load_dotenv()

bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher(bot)

# Импортируем обработчики
start_handler.register_handlers(dp)
info_handler.register_handlers(dp)
random_handler.register_handlers(dp)

callback_handlers.register_handlers(dp)

if __name__ == '__main__':
    executor.start_polling(dp)

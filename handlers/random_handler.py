from aiogram import types, Dispatcher
import random

names = ("Игорь", "Ольга", "Анна", "Дмитрий")

async def random_name_command(message: types.Message):
    random_name = random.choice(names)
    await message.answer(f"Случайное имя: {random_name}")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(random_name_command, commands=['random'])

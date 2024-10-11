from aiogram import types, Dispatcher

async def myinfo_command(message: types.Message):
    user_data = (
        f"Ваш id: {message.from_user.id}\n"
        f"Ваше имя: {message.from_user.first_name}\n"
        f"Ваш ник: @{message.from_user.username if message.from_user.username else 'Не указан'}"
    )
    await message.answer(user_data)

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(myinfo_command, commands=['myinfo'])

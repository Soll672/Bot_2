from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

user_count = set()


async def start_command(message: types.Message):
    user_id = message.from_user.id
    user_count.add(user_id)

    buttons = InlineKeyboardMarkup(row_width=2).add(
        InlineKeyboardButton("Наш адрес", url="https://maps.google.com"),
        InlineKeyboardButton("Контакты", callback_data="contacts"),
        InlineKeyboardButton("О нас", callback_data="about"),
        InlineKeyboardButton("Наш сайт", url="https://example.com"),
        InlineKeyboardButton("Инстаграм", url="https://instagram.com/"),
        InlineKeyboardButton("Отзывы", callback_data="feedback"),
        InlineKeyboardButton("Вакансии", callback_data="vacancies")
    )

    await message.answer(
        f"Привет, {message.from_user.first_name}! Наш бот обслуживает уже {len(user_count)} пользователей.",
        reply_markup=buttons
    )


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])


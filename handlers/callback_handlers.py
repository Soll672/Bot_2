from aiogram import types, Dispatcher

async def process_contacts(callback_query: types.CallbackQuery):
    await callback_query.message.answer("Наш телефон: +123456789")

async def process_about(callback_query: types.CallbackQuery):
    await callback_query.message.answer("Мы — лучшая пиццерия в городе!")

def register_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(process_contacts, lambda c: c.data == 'contacts')
    dp.register_callback_query_handler(process_about, lambda c: c.data == 'about')

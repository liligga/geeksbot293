from aiogram import types


async def start(message: types.Message):
    kb = types.InlineKeyboardMarkup()
    kb.add(
        types.InlineKeyboardButton("Наш сайт", url='https://google.com'),
        types.InlineKeyboardButton("О нас", callback_data="about")
    )

    await message.answer(
        "Мы - компания Geeks",
        reply_markup=kb
    )


async def about(callback: types.CallbackQuery):
    # await callback.answer()
    await callback.message.answer("О нас .......")
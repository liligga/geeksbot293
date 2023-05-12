from aiogram import types


async def pic(message: types.Message):
    with open('images/cat.png', 'rb') as photo:
        await message.answer_photo(photo)

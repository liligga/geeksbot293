from aiogram.types import (
    Message,
    ReplyKeyboardMarkup, 
    KeyboardButton, 
    ReplyKeyboardRemove)


async def show_categories(message: Message):
    kb = ReplyKeyboardMarkup()
    kb.add(KeyboardButton("Женская обувь"))
    kb.add(KeyboardButton("Мужская обувь"))

    await message.answer("Выберите категорию товаров:", reply_markup=kb)


async def show_female_shoes(message: Message):
    kb = ReplyKeyboardRemove()
    await message.answer("У нас в наличии следующие женские модели:", reply_markup=kb)
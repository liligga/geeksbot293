from aiogram.types import (
    Message, CallbackQuery,
    ReplyKeyboardMarkup, 
    KeyboardButton, 
    ReplyKeyboardRemove,
    InlineKeyboardMarkup,
    InlineKeyboardButton)

from db.queries import fetch_books


async def show_categories(message: Message):
    kb = ReplyKeyboardMarkup()
    kb.add(KeyboardButton("Женская обувь"))
    kb.add(KeyboardButton("Мужская обувь"))

    await message.answer("Выберите категорию товаров:", reply_markup=kb)


def keyboard(product_id: int):
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("Купить", callback_data=f"buy_{product_id}"))
    return kb


async def show_female_shoes(message: Message):
    kb = ReplyKeyboardRemove()
    products = [
        (100, "Book 1"), (20, "Book 2"), (3001, "Book 3"),
    ]
    await message.answer("У нас в наличии следующие женские модели:", reply_markup=kb)
    for pr in products:
        await message.answer(pr[1], reply_markup=keyboard(pr[0]))

async def buy_product_handler(callback: CallbackQuery):
    print(callback.data)
    pr_id = int(callback.data[4:])
    print(pr_id)

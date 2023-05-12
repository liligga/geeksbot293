from aiogram import types


async def echo(message: types.Message):
    """Эта ф-я срабатывает на все сообщения пользователя"""
    await message.answer(message.text)

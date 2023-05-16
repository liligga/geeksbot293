from aiogram.types import (
    Message, 
    CallbackQuery, 
    ReplyKeyboardMarkup, 
    KeyboardButton
)
from aiogram import Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

# FSM - Finite state machine
# Конечный автомат
class Survey(StatesGroup):
    name = State()
    age = State()
    gender = State()


async def start_survey(message: Message):
    await Survey.name.set()
    await message.answer("Ваше имя:")


async def process_name(message: Message, state: FSMContext):
    async with state.proxy as data:
        data['name'] = message.text

    await Survey.next()
    await message.answer("Введите ваш возраст:")


async def proccess_age(message: Message, state: FSMContext):
    age = message.text
    if not age.isdigit():
        await message.answer("ВВодите только цифры")
    elif int(age) > 100 or int(age) < 10:
        await message.answer("Только от 8 и до 100")
    else:
        async with state.proxy() as data:
            data['age'] = int(age)
        
        await Survey.next()
        await message.answer("Укажите ваш пол")


async def process_gender(message: Message, state: FSMContext):
    gender = message.text

    await state.finish()
    await message.answer("Спасибо за уделенное время!")


async def cancel_survey(message: Message, state: FSMContext):
    await state.finish()
    await message.answer("Спасибо за уделенное время!")



def register_fsm_handlers(dp: Dispatcher):
    dp.register_message_handler(start_survey, commands=["surv"])
    dp.register_message_handler(process_name, state=Survey.name)
    dp.register_message_handler(proccess_age, state=Survey.age)
    dp.register_message_handler(cancel_survey, commands=["stop"], state="*")
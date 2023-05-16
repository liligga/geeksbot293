from aiogram import executor
from aiogram.dispatcher.filters import Text

from config import dp
from handlers.echo import echo
from handlers.picture import pic
from handlers.start import start, about
from handlers.shop import show_categories, show_female_shoes
from handlers.survey_fsm import register_fsm_handlers


if __name__ == "__main__":
    dp.register_message_handler(pic, commands=["pic"])
    dp.register_message_handler(start, commands=["start"])
    dp.register_callback_query_handler(about, lambda cb: cb.data == 'about')
    dp.register_message_handler(show_categories, commands=["shop"])
    dp.register_message_handler(show_female_shoes, Text(equals="женская обувь", ignore_case=True))

    # Survey FSM обработчики
    register_fsm_handlers(dp)

    dp.register_message_handler(echo)
    executor.start_polling(dp, skip_updates=True)

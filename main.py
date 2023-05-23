from aiogram import executor
from aiogram.dispatcher.filters import Text
import logging

from config import dp
from handlers.echo import echo
from handlers.picture import pic
from handlers.start import start, about
from handlers.shop import show_categories, show_female_shoes
from handlers.survey_fsm import register_fsm_handlers
from db.queries import (
    init_db, drop_tables, create_tables, insert_data
)

async def on_start(_):
    init_db()
    drop_tables()
    create_tables()
    insert_data()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    dp.register_message_handler(pic, commands=["pic"])
    dp.register_message_handler(start, commands=["start"])
    dp.register_callback_query_handler(about, lambda cb: cb.data == 'about')
    dp.register_message_handler(show_categories, commands=["shop"])
    dp.register_message_handler(show_female_shoes, Text(equals="женская обувь", ignore_case=True))

    # Survey FSM обработчики
    register_fsm_handlers(dp)

    dp.register_message_handler(echo)
    executor.start_polling(dp, skip_updates=True, on_startup=on_start)

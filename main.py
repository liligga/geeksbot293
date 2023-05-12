from aiogram import executor
from config import dp
from handlers.echo import echo
from handlers.picture import pic
from handlers.start import start, about


if __name__ == "__main__":
    dp.register_message_handler(pic, commands=["pic"])
    dp.register_message_handler(start, commands=["start"])
    dp.register_callback_query_handler(about, lambda cb: cb.data == 'about')

    dp.register_message_handler(echo)
    executor.start_polling(dp, skip_updates=True)

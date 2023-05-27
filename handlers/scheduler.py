from aiogram.types import Message
from config import bot, scheduler
from datetime import datetime


async def handle_sched(message: Message):
    # задача вылняется по интервалу
    # scheduler.add_job(
    #     send_notification,
    #     'interval',
    #     seconds = 5,
    #     args=(message.from_user.id, )
    # )
    # scheduler.add_job(
    #     send_notification,
    #     'date',
    #     run_date=datetime(2023, 5, 26, 17, 31),
    #     args=(message.from_user.id, )
    # )
    # scheduler.add_job(
    #     send_notification,
    #     'cron',
    #     month=5,
    #     hour=17,
    #     args=(message.from_user.id, )
    # )
    # scheduler.add_job(
    #     send_notification,
    #     'cron',
        # в мае, июне, июле, августе
    #     month='5-8',
        # в 17:00 и 21:00
    #     hour='17,21',
    #     args=(message.from_user.id, )
    # )
    scheduler.add_job(
        send_notification,
        'cron',
        # каждую последнюю пятницу
        day_of_week='last fri',
        hour='17',
        args=(message.from_user.id, ),
        id=message.from_user.id
    )
    await message.answer("Отлично")


async def send_notification(chat_id: int):
    await bot.send_message(
        chat_id=chat_id,
        text="привет"
    )


async def cancel_notif(message: Message):
    scheduler.remove_job(job_id=message.from_user.id)
    await message.answer("Ваша задача аннулирована")
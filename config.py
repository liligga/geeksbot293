from aiogram import Dispatcher, Bot
from dotenv import load_dotenv
import os



load_dotenv()
bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher(bot)

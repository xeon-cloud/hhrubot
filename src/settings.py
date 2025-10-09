from dotenv import load_dotenv
import os
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage


load_dotenv()

bot = Bot(os.environ['TOKEN'])
dp = Dispatcher(storage=MemoryStorage())
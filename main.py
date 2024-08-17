import dotenv
from dotenv import load_dotenv
import os

import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
import aiohttp

import sqlite3
import logging

dotenv.load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)


#Эти состояния будут использоваться для хранения и отслеживания, когда бот будет продолжать работу с пользователем
class Form(StatesGroup):
    name = State()
    age = State()
    city = State()

def init_db():
    conn = sqlite3.connect('user_data.db')
    cur = conn.cursor()
    cur.execute('''
	CREATE TABLE IF NOT EXISTS users (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL,
	age INTEGER NOT NULL,
	city TEXT NOT NULL)
	''')
    conn.commit()
    conn.close()

init_db()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Привет, {message.from_user.full_name}! Это урок TG03")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
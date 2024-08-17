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
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')

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
async def start(message: Message, state: FSMContext):
    await message.answer("Привет! Как тебя зовут?")
    await state.set_state(Form.name)

@dp.message(Form.name)
async def name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Сколько тебе лет?")
    await state.set_state(Form.age)

@dp.message(Form.age)
async def age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer("В каком городе ты живешь?")
    await state.set_state(Form.city)

@dp.message(Form.city)
async def city(message: Message, state: FSMContext):
    await state.update_data(city=message.text)
    user_data = await state.get_data()

    conn = sqlite3.connect('user_data.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO users (name, age, city) VALUES (?, ?, ?)', (user_data['name'], user_data['age'], user_data['city']))
    conn.commit()
    conn.close()

    await message.answer("Ваши данные сохранены")

    async with aiohttp.ClientSession() as session:
        async with session.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={user_data['city']}&appid={WEATHER_API_KEY}&units=metric") as response:



async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
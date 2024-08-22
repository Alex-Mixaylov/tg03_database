import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram import F
from dotenv import load_dotenv
import os
import keyboard as kb  # Импортируем клавиатуры из файла keyboard.py

# Загрузка переменных окружения
load_dotenv()
BOT_TOKEN = os.getenv("TOKEN")

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Задание 1: Команда /start с меню "Привет" и "Пока"
@dp.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer("Выберите опцию:", reply_markup=kb.kboard)

@dp.message(F.text == "Привет")
async def say_hello(message: types.Message):
    await message.answer(f"Привет, {message.from_user.first_name}!")

@dp.message(F.text == "Пока")
async def say_goodbye(message: types.Message):
    await message.answer(f"До свидания, {message.from_user.first_name}!")

# Задание 2: Команда /links с кнопками URL-ссылок
@dp.message(Command("links"))
async def show_links(message: types.Message):
    await message.answer("Выберите ссылку:", reply_markup=kb.inline_kboard)

# Задание 3: Команда /dynamic с динамическими инлайн-кнопками
@dp.message(Command("dynamic"))
async def dynamic_menu(message: types.Message):
    keyboard = await kb.dynamic_kboard()
    await message.answer("Нажмите кнопку для показа дополнительных опций:", reply_markup=keyboard)

@dp.callback_query(F.data == "show_more")
async def show_more_options(callback_query: types.CallbackQuery):
    keyboard = await kb.dynamic_options_kboard()
    await callback_query.message.edit_reply_markup(reply_markup=keyboard)

@dp.callback_query(F.data == "option_1")
async def option_1_selected(callback_query: types.CallbackQuery):
    await callback_query.message.answer("Вы выбрали Опцию 1")

@dp.callback_query(F.data == "option_2")
async def option_2_selected(callback_query: types.CallbackQuery):
    await callback_query.message.answer("Вы выбрали Опцию 2")

if __name__ == "__main__":
    dp.start_polling(bot, skip_updates=True)

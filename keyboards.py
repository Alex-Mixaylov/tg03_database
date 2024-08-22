from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

kboard = ReplyKeyboardMarkup(keyboard=[
   [KeyboardButton(text="Тестовая кнопка 1")],
   [KeyboardButton(text="Тестовая кнопка 2"), KeyboardButton(text="Тестовая кнопка 3")]
], resize_keyboard=True)

inline_kboard= InlineKeyboardMarkup(inline_keyboard=[
   [InlineKeyboardButton(text="Видео", url="https://www.examle.com/")]
])

builder = ["кнопка 1", "кнопка 2", "кнопка 3", "кнопка 4"]

async def builder_kboard():
   keyboard = ReplyKeyboardBuilder()
   for button in builder:
      keyboard.add(KeyboardButton(text=button))
   return keyboard.adjust(2).as_markup()
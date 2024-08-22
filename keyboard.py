from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

# Простая клавиатура с двумя кнопками: "Привет" и "Пока"
kboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Привет")],
        [KeyboardButton(text="Пока")]
    ],
    resize_keyboard=True
)

# Инлайн-клавиатура с URL-ссылками
inline_kboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Новости", url="https://www.youtube.com/watch?v=BIevJv2YhYk")],
        [InlineKeyboardButton(text="Музыка", url="https://www.youtube.com/watch?v=vABnCGBqjKY")],
        [InlineKeyboardButton(text="Видео", url="https://www.youtube.com/watch?v=dLw6aqKbpsg")]
    ]
)

# Динамическое создание кнопок
builder_buttons = ["Опция 1", "Опция 2"]

async def builder_kboard():
    keyboard = ReplyKeyboardBuilder()
    for button in builder_buttons:
        keyboard.add(KeyboardButton(text=button))
    return keyboard.adjust(2).as_markup()

# Инлайн-клавиатура для динамического изменения
async def dynamic_kboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="Показать больше", callback_data="show_more")
    return builder.as_markup()

async def dynamic_options_kboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="Опция 1", callback_data="option_1")
    builder.button(text="Опция 2", callback_data="option_2")
    return builder.as_markup()

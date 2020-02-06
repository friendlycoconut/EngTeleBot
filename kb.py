from aiogram import types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

button_hi = KeyboardButton('Привет! 👋')

greet_kb = ReplyKeyboardMarkup()
greet_kb.add(button_hi)

keyboard_markup = types.InlineKeyboardMarkup(row_width=3)
# default row_width is 3, so here we can omit it actually
# kept for clearness

text_and_data = (
    ('Я хочу пройти тест!', 'test'),
    ('Я хочу выучить слова!', 'words'),
)
# in real life for the callback_data the callback data factory should be used
# here the raw string is used for the simplicity
row_btns = (types.InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data)

keyboard_markup.row(*row_btns)
keyboard_markup.add(
    # url buttons have no callback data
    types.InlineKeyboardButton('Статистика', url='https://github.com/aiogram/aiogram'),
)


keyboard_markup_2 = types.InlineKeyboardMarkup()
text_and_data_2 = (
    ('A2 level', 'a2'),
)
row_btns_2=(types.InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data_2)
keyboard_markup_2.add(*row_btns_2)
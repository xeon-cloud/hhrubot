from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton)


MAIN = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Задачи')],
    [KeyboardButton(text='Настройки'), KeyboardButton(text='Статистика')]
], resize_keyboard=True)
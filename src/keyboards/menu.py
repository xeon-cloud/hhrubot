from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton)


MAIN = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Поиск вакансий')],
    [KeyboardButton(text='Создать таргет')]
], resize_keyboard=True)
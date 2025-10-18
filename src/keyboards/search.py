from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from typing import List


async def cities_key(data: List) -> InlineKeyboardMarkup:
    key = InlineKeyboardBuilder()
    for id, name in data:
        key.row(InlineKeyboardButton(
            text=name, callback_data=f'sel_search_city={id}'
        ))

    return key.adjust(1).as_markup()
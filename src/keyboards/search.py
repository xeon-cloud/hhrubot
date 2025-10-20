from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from typing import List, Union


async def cities_key(data: List) -> InlineKeyboardMarkup:
    key = InlineKeyboardBuilder()
    for id, name in data:
        key.row(InlineKeyboardButton(
            text=name, callback_data=f'sel_search_city={id}'
        ))

    return key.adjust(1).as_markup()


async def items_key(
    data: List,
    page: int,
    end_page: Union[str, int] = '-'
) -> InlineKeyboardMarkup:
    key = InlineKeyboardBuilder()
    for id, name in data:
        key.row(InlineKeyboardButton(
            text=name,
            callback_data=f'vacancy={id}_{page}'
        ))
    key.row(
        InlineKeyboardButton(
            text='⏪',
            callback_data=f'go_page={page - 1}'
        ),
        InlineKeyboardButton(
            text=f'{page + 1}/{end_page}',
            callback_data=' '
        ),
        InlineKeyboardButton(
            text='⏩',
            callback_data=f'go_page={page + 1}'
        )
    )
    return key.as_markup()


async def vacancy_key(
    url: str,
    page: Union[str, int]
) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Перейти', url=url)],
        [InlineKeyboardButton(text='◀️ Назад', callback_data=f'go_page={page}')]
    ])
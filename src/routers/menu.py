from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from ..keyboards import menu

router = Router()

@router.message(CommandStart())
async def start(m: Message):
    await m.answer('Вас приветствует парсер вакансий hh.ru\n\nОткрыто главное меню', reply_markup=menu.MAIN)
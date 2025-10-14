from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from ..keyboards import menu
from ..states import App as app_states

router = Router()


@router.message(CommandStart())
async def start(m: Message):
    await m.answer('Вас приветствует парсер вакансий hh.ru\n\nОткрыто главное меню', reply_markup=menu.MAIN)


@router.message(F.text == 'Поиск вакансий')
async def search_vacancies(m: Message, state: FSMContext):
    await m.answer('Введите ваш запрос')
    await state.set_state(app_states.search)


@router.message(F.text == 'Создать таргет')
async def create_target(m: Message):
    pass
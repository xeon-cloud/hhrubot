from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from ..builders.search import SearchBuilder
from ..states import App as app_states

router = Router()

@router.message(app_states.city_search)
async def handle_geo(m: Message, state: FSMContext):
    await SearchBuilder(
        message=m,
        state=state
    ).handle_city()


@router.callback_query(F.data.split('=')[0] == 'sel_search_city')
async def select_city(c: CallbackQuery, state: FSMContext):
    await SearchBuilder(
        callback=c,
        state=state
    ).save_area(c.data.split('=')[1])


@router.message(app_states.query_search)
async def handle_query(m: Message, state: FSMContext):
    await SearchBuilder(
        message=m,
        state=state
    ).go_search()
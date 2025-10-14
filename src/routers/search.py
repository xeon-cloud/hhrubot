from aiogram import Router, F
from aiogram.types import Message

from ..builders.search import SearchBuilder
from ..states import App as app_states

router = Router()


@router.message(app_states.search)
async def handle_query(m: Message):
    await SearchBuilder(message=m).go_search()
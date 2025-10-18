from aiogram.fsm.state import State, StatesGroup


class App(StatesGroup):
    add_task = State()
    city_search = State()
    query_search = State()
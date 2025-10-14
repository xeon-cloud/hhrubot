from aiogram.fsm.state import State, StatesGroup


class App(StatesGroup):
    add_task = State()
    search = State()
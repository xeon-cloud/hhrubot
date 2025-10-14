from aiogram import Dispatcher
from . import menu, search, task


async def includeRouters(dispatcher: Dispatcher) -> None:
    routers = [
        menu.router,
        search.router,
        task.router
    ]
    dispatcher.include_routers(*routers)
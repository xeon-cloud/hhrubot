from aiogram import Dispatcher
from . import menu

async def includeRouters(dispatcher: Dispatcher) -> None:
    routers = [
        menu.router
    ]
    dispatcher.include_routers(*routers)
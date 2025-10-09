import asyncio

from .settings import bot, dp
from .routers import includeRouters


async def initBot():
    await includeRouters(dp)
    await dp.start_polling(bot)


if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.DEBUG)

    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(initBot())
    except KeyboardInterrupt:
        loop.close()
import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from app.handlers import router


load_dotenv()
TOKEN=os.getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

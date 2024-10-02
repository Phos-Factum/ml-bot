import asyncio
import logging
import os

<<<<<<< HEAD
from dotenv import load_dotenv
=======
>>>>>>> dev-tg_bot
from aiogram import Bot, Dispatcher
from app.handlers import router


load_dotenv()
<<<<<<< HEAD
TOKEN = os.getenv("TOKEN")
=======
TOKEN=os.getenv("TOKEN")
>>>>>>> dev-tg_bot

bot = Bot(token=TOKEN)
dp = Dispatcher()


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

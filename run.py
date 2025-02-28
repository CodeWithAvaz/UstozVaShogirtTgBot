import asyncio
from aiogram import Bot, Dispatcher

from data.config import API_TOKEN
from handlers.start_hand import start_router
from handlers.sherik_hand import sherik_router

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


dp.include_router(start_router)
dp.include_router(sherik_router)

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    print("Bot ishladi..")
    asyncio.run(main())
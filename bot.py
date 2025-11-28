import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import os

TOKEN = os.getenv("TOKEN")  # ← Берём токен из Railway переменных

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    @dp.message(Command("start"))
    async def start(message: types.Message):
        await message.answer("Бот успешно работает на Railway! 🤖🔥")

    @dp.message()
    async def echo(message: types.Message):
        await message.answer(f"Ты сказал: {message.text}")

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
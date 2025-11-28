import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import os
import logging
from collections import deque

TOKEN = os.getenv("TOKEN")  # токен из Railway переменных

# Настройка логов
logging.basicConfig(level=logging.INFO)
log_history = deque(maxlen=50)  # храним последние 50 логов

# Функция для записи в лог и историю
def log(message):
    logging.info(message)
    log_history.append(message)

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    @dp.message(Command("start"))
    async def start(message: types.Message):
        log(f"/start от {message.from_user.id}")
        await message.answer("Бот успешно работает на Railway! 🤖🔥")

    @dp.message(Command("log"))
    async def send_log(message: types.Message):
        # Присылаем последние 50 логов
        if log_history:
            await message.answer("\n".join(log_history))
        else:
            await message.answer("Логи пока пустые.")

    @dp.message()
    async def echo(message: types.Message):
        log(f"Сообщение: {message.text}")
        await message.answer(f"Ты сказал: {message.text}")

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

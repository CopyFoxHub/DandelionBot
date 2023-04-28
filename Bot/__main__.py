# Необходимые библиотеки
import os
import asyncio
import logging
import openai
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand  # Описание команд

# Собственные пакеты
from Commands import register_commands  # Регистрация команд
from Resources import all_commands  # Список команд


async def main() -> None:
    """Подготовка к запуску"""

    # Логирование событий
    logging.basicConfig(level=logging.DEBUG)

    # Создание объектов для бота
    disp = Dispatcher()
    bot = Bot(token=os.getenv("bot_token"))

    # Создание описания команд
    await bot.set_my_commands(commands=[BotCommand(command=command[0],
                                                   description=command[1]) for command in all_commands])

    # Регистрация OpenAI токена
    openai.api_key = os.getenv("openai_token")

    # Регистрация команд
    register_commands(router=disp)

    # Старт пуллинга бота
    await disp.start_polling(bot)


# Запуск основной программы
if __name__ == "__main__":
    try:  # Начало пулинга
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):  # При отключение терминала
        print("Бот был выключен.")

# Список объектов, доступных для импорта
__all__ = ["register_commands"]

# Модули Aiogram
from aiogram import F  # Магический фильтр
from aiogram import Router  # Стандартный Роутер
from aiogram.filters import Command  # Команды

# Модули команд
from DandelionBot.Bot.Commands.menu import command_menu, call_menu  # Главное меню
from DandelionBot.Bot.Commands.dialog_chatgpt import (ask_chatgpt, command_chatgpt,
                                                      call_chatgpt, change_content)  # ChatGPT
from DandelionBot.Bot.Commands.voice import command_voice, call_voice  # Озвучивание текста


def register_commands(router: Router) -> None:
    """Регистрация команд в роутере"""

    # Главное меню
    router.message.register(command_menu, Command(commands=["start", "menu"]))  # Вызов меню командой
    router.callback_query.register(call_menu, F.data == "menu")  # Переход в меню

    # Озвучка текста
    router.message.register(command_voice, Command(commands="voice"))  # Озвучка текста
    router.callback_query.register(call_voice, F.data == "voice")  # Информация о озвучке

    # Ответы от ИИ
    router.message.register(command_chatgpt, Command(commands=["chatgpt"]))  # Информация о работе ChatGPT
    router.callback_query.register(call_chatgpt, F.data == "chatgpt")  # Информация о работе ChatGPT
    router.message.register(change_content, Command(commands=["set_content"]))  # Установить настройки ChatGPT
    router.message.register(ask_chatgpt, F.text)  # Ответ на вопрос

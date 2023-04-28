import os
import gtts
from aiogram import types
from aiogram.types import FSInputFile
from aiogram.filters import CommandObject
from DandelionBot.Bot.Resources import voice_phrase
from aiogram.utils.keyboard import InlineKeyboardBuilder


async def command_voice(message: types.Message, command: CommandObject) -> None:
    """Создание голосового ассистента"""

    # Проверка на наличие текста
    if command.args:

        # Сохранение mp3 файла озвучки
        user = f"{message.from_user.id}.mp3"
        (gtts.gTTS(text=command.args, lang="ru")).save(user)

        # Отправка файлов
        await message.answer_audio(audio=FSInputFile(user), performer="Одуванчик - Бот",
                                   title="Цветочный микс")
        # Удаление голосового
        os.remove(user)
    else:
        await message.answer(text="Отсутствует фраза, которую нужно сказать.")


async def call_voice(call: types.CallbackQuery) -> None:
    """Информация об Voice"""

    # Создание кнопок
    builder = InlineKeyboardBuilder()
    builder.button(text="Назад", callback_data="menu")

    # Отправка сообщений
    await call.message.edit_text(text=voice_phrase, reply_markup=builder.as_markup())

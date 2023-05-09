import openai  # Доступ к ИИ
from aiogram import types  # Типы сообщений
from aiogram.filters import CommandObject  # Аргументы
from openai.error import RateLimitError, InvalidRequestError  # Ошибка при спаме
from aiogram.utils.keyboard import InlineKeyboardBuilder  # Создание кнопок
from DandelionBot.Bot.Resources import chatgpt_phrase, chatgpt_content  # Всё для ChatGPT


async def ask_chatgpt(message: types.Message) -> None:
    """Ответ на любое сообщение от человека"""

    # Генерация ответа
    text = await generate_text([{"role": "system", "content": chatgpt_content[0]},
                               {"role": "user", "content": message.text}])
    # Отправка ответа
    await message.answer(text=text)


async def command_chatgpt(message: types.Message) -> None:
    """Инструкция по ChatGPT (Вызов командой)"""

    # Отправка сообщения
    await message.answer(text=chatgpt_phrase)


async def call_chatgpt(call: types.CallbackQuery) -> None:
    """Инструкция по ChatGPT (Вызов кнопкой в меню)"""

    # Создание кнопок
    builder = InlineKeyboardBuilder()
    builder.button(text="Назад", callback_data="menu")

    await call.message.edit_text(text=chatgpt_phrase, reply_markup=builder.as_markup())


async def change_content(message: types.Message, command: CommandObject) -> None:
    """Изменение настроек ChatGPT"""

    # Проверка на наличие аргумента
    if command.args:
        if command.args == "reset":
            chatgpt_content[0] = chatgpt_content[1]
            await message.answer(text="Настройки сброшены до заводских")
        else:
            chatgpt_content[0] = command.args
            await message.answer(text=f"Новые настройки бота: {command.args}\n\nВведите /set_content reset для сброса")

    # При его отсутствие
    else:
        await message.answer(text=f"Отсутствует текст для настроек ChatGPT\n\nТекущие настройки:\n{chatgpt_content[0]}")


async def generate_text(message_history) -> str:
    """Генерация ответа на запрос"""

    # Формирование ответа
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=message_history,
            temperature=0.7,
            stop=None,
            max_tokens=3800
            )
        return response.choices[0].message.content

    # При спаме
    except RateLimitError:
        return "Слишком большое количество запросов, попробуйте написать ещё раз через 20 секунд."
    except InvalidRequestError:
        return "Ваше предложение (или настройки бота) слишком большие. Попробуйте их/его изменить."

from aiogram import types  # Типы сообщений
from DandelionBot.Bot.Resources import menu_phrase  # Фразы для меню
from aiogram.utils.keyboard import InlineKeyboardBuilder  # Создание кнопок


# Меню для слеш-команд
async def command_menu(message: types.Message) -> None:
    """Главное меню, удаляет свой вызов и отправляет меню команд"""

    # Создание кнопок
    builder = InlineKeyboardBuilder()
    builder.add(
        types.InlineKeyboardButton(text="ChatGPT",
                                   callback_data="chatgpt"),  # Диалог с ИИ
        types.InlineKeyboardButton(text="Озвучка",
                                   callback_data="voice")  # Озвучивание сообщений
    )
    # Количество кнопок в таблице
    builder.adjust(2)

    # Удаление сообщения
    await message.delete()

    # Отправка сообщения
    await message.answer(text=menu_phrase,
                         reply_markup=builder.as_markup())


# Меню для вызова на кнопку
async def call_menu(call: types.CallbackQuery) -> None:
    """Главное меню, вызываемое при помощи Callback запроса"""

    # Создание кнопок
    builder = InlineKeyboardBuilder()
    builder.add(
        types.InlineKeyboardButton(text="ChatGPT",
                                   callback_data="chatgpt"),  # Диалог с ИИ
        types.InlineKeyboardButton(text="Озвучка",
                                   callback_data="voice")  # Озвучивание сообщений
    )
    # Количество кнопок в таблице
    builder.adjust(2)

    # Изменение сообщения
    await call.message.edit_text(text=menu_phrase,
                                 reply_markup=builder.as_markup())

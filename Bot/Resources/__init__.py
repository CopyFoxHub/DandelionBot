# Список объектов, доступных для импорта
__all__ = ["menu_phrase", "chatgpt_phrase", "voice_phrase", "all_commands", "chatgpt_content"]

# Необходимые ресурсы
from DandelionBot.Bot.Resources.settings import all_commands, chatgpt_content  # Список команд
from DandelionBot.Bot.Resources.replicas import menu_phrase, chatgpt_phrase, voice_phrase  # Фразы

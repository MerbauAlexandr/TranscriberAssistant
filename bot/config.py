TranscriberAssistant / bot / config.py
import os
from dotenv import load_dotenv

# Загрузка переменных окружения из файла .env
load_dotenv()


class Config:
    # OpenAI API
    OPENAI_API_KEY = os.getenv('API_KEY')

    # Telegram Bot
    BOT_TOKEN = os.getenv('BOT_TOKEN')

    # Организация
    ORGANIZATION_ID = os.getenv('ORGANIZATION_ID')

    # Настройки для обработки аудио
    MAX_AUDIO_SIZE = 20 * 1024 * 1024  # 20 MB в байтах

    # Настройки для транскрипции
    WHISPER_MODEL = "base"  # Можно изменить на другую модель при необходимости

    # Пути для сохранения файлов
    TEMP_AUDIO_DIR = "temp_audio"
    OUTPUT_DOC_DIR = "output_documents"

    # Настройки для форматирования документа
    MAX_TOKENS_PER_REQUEST = 4000  # Максимальное количество токенов для одного запроса к GPT

    @classmethod
    def create_directories(cls):
        """Создает необходимые директории, если они не существуют."""
        os.makedirs(cls.TEMP_AUDIO_DIR, exist_ok=True)
        os.makedirs(cls.OUTPUT_DOC_DIR, exist_ok=True)


# Создание необходимых директорий при импорте конфига
Config.create_directories()
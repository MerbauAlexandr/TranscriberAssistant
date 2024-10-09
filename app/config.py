# C:\Users\Pavlu4ini\PycharmProjects\TranscriberAssistant\app\config.py

import os
from dotenv import load_dotenv

# Загружаем переменные окружения из файла .env
load_dotenv()

# Токен бота
BOT_TOKEN = os.getenv("BOT_TOKEN")

# OpenAI API конфигурация
OPENAI_API_KEY = os.getenv("API_KEY")
OPENAI_ORG_ID = os.getenv("ORGANIZATION_ID")

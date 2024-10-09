# C:\Users\Pavlu4ini\PycharmProjects\TranscriberAssistant\app\bot.py

import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from config import BOT_TOKEN

if not BOT_TOKEN:
    raise ValueError("Токен бота не найден! Проверьте файл .env")

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))

from ai_interviewer import get_file_info, process_user_input
from audio_processing import process_audio_file, extract_audio_from_link
from transcriber import transcribe_audio
from ai_formatter import format_document

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Стартовая команда
async def start(update: Update, context: CallbackContext) -> None:
    logger.info("Команда /start получена")
    await update.message.reply_text('Привет! Я TranscriberAssistant бот. Отправь мне аудиофайл или ссылку на видео.')

# Обработка аудиофайлов
async def handle_audio(update: Update, context: CallbackContext) -> None:
    audio_file = update.message.audio
    if audio_file:
        file = await audio_file.get_file()
        file_path = f"downloads/{audio_file.file_id}.mp3"
        await file.download(file_path)

        # Получение информации от пользователя
        file_info = await get_file_info(update, context, file_path)
        await update.message.reply_text('Аудиофайл получен. Обрабатываю...')

        # Обработка аудио и транскрипция
        transcribed_text = transcribe_audio(file_path)
        formatted_doc = format_document(file_info, transcribed_text)
        await update.message.reply_text('Транскрипция завершена и документ готов!')

# Обработка ссылок на видео
async def handle_text(update: Update, context: CallbackContext) -> None:
    text = update.message.text
    if "youtube.com" in text or "rutube.ru" in text or "dzen.ru" in text:
        await update.message.reply_text('Ссылка на видео получена. Начинаю извлечение аудио...')
        audio_path = extract_audio_from_link(text)

        # Получение информации от пользователя
        file_info = await get_file_info(update, context, audio_path)
        await update.message.reply_text('Аудио извлечено. Обрабатываю...')

        # Обработка аудио и транскрипция
        transcribed_text = transcribe_audio(audio_path)
        formatted_doc = format_document(file_info, transcribed_text)
        await update.message.reply_text('Транскрипция завершена и документ готов!')
    else:
        await update.message.reply_text('Отправь аудиофайл или ссылку на видео.')

# Основная функция для запуска бота
async def main() -> None:
    # Создаем приложение
    application = Application.builder().token(BOT_TOKEN).build()

    # Регистрируем команды и обработчики
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.AUDIO, handle_audio))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

    # Инициализируем и запускаем приложение
    await application.initialize()
    await application.start()
    await application.updater.start_polling()

    # Бот будет работать до завершения
    await application.updater.stop()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())

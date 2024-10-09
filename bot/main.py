import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from config import Config
import openai

# Настройка логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Инициализация OpenAI
openai.api_key = Config.OPENAI_API_KEY

def start(update: Update, context: CallbackContext) -> None:
    """Отправляет приветственное сообщение при команде /start."""
    update.message.reply_text('Здравствуйте! Я бот-транскрибер. Отправьте мне аудиофайл или ссылку на видео, и я помогу вам с транскрипцией.')

def handle_message(update: Update, context: CallbackContext) -> None:
    """Обрабатывает входящие сообщения."""
    message = update.message.text
    chat_id = update.effective_chat.id

    # Используем GPT-4o-mini для генерации ответа
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",  # Убедитесь, что это правильное название модели
        messages=[
            {"role": "system", "content": "Вы — помощник для транскрипции аудио и видео. Помогите пользователю с вопросами о процессе транскрипции."},
            {"role": "user", "content": message}
        ]
    )

    bot_response = response.choices[0].message['content']
    update.message.reply_text(bot_response)

def main() -> None:
    """Запускает бота."""
    updater = Updater(Config.BOT_TOKEN)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
# C:\Users\Pavlu4ini\PycharmProjects\TranscriberAssistant\app\ai_interviewer.py

def get_file_info(update, context, file_path):
    """
    Запрашиваем у пользователя описание содержимого аудиофайла или видео
    и информацию о ролях участников.
    """
    update.message.reply_text('Опишите содержимое файла и укажите участников и их роли.')
    user_input = context.bot.wait_for_message(chat_id=update.message.chat_id, timeout=60)
    file_info = process_user_input(user_input.text)
    return file_info

def process_user_input(user_input):
    """
    Обрабатываем ввод пользователя, выделяем участников и их роли.
    """
    participants = []
    roles = []

    # Парсинг информации
    lines = user_input.split(',')
    for line in lines:
        parts = line.strip().split(':')
        if len(parts) == 2:
            participant, role = parts
            participants.append(participant.strip())
            roles.append(role.strip())

    file_info = {
        "participants": participants,
        "roles": roles
    }

    return file_info

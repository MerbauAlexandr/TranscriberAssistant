# C:\Users\Pavlu4ini\PycharmProjects\TranscriberAssistant\app\transcriber.py

import whisper

def transcribe_audio(audio_path):
    """
    Выполняем транскрипцию аудиофайла с помощью Whisper.
    """
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    return result["text"]

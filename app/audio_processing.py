# C:\Users\Pavlu4ini\PycharmProjects\TranscriberAssistant\app\audio_processing.py

from moviepy.editor import VideoFileClip
from pydub import AudioSegment
import os

def extract_audio_from_link(video_link):
    """
    Извлекаем аудио из ссылки на видео (YouTube, RuTube, Дзен).
    """
    # Здесь будет логика для извлечения аудио через youtube-dl или moviepy
    audio_path = "downloads/audio.mp3"
    return audio_path

def process_audio_file(audio_path):
    """
    Обрабатываем аудиофайл, разделяем его на части.
    """
    audio = AudioSegment.from_file(audio_path)
    duration = len(audio) / 1000  # в секундах
    parts = []

    # Разделение на части (каждая часть до 20 минут)
    for i in range(0, int(duration), 1200):
        part = audio[i*1000:(i+1200)*1000]
        part_path = f"downloads/part_{i}.mp3"
        part.export(part_path, format="mp3")
        parts.append(part_path)

    return parts

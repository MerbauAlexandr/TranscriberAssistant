#TranscriberAssistant / bot / conversation.py

import openai
import os
from dotenv import load_dotenv
from typing import Dict, List


class Conversation:
    def __init__(self, api_key: str):
        openai.api_key = api_key
        self.conversation_history = []

    def ask_question(self, question: str) -> str:
        self.conversation_history.append({"role": "user", "content": question})
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=self.conversation_history
        )
        assistant_response = response.choices[0].message['content']
        self.conversation_history.append({"role": "assistant", "content": assistant_response})
        return assistant_response

    def extract_info(self) -> Dict[str, List[str]]:
        participants = []
        roles = []
        for message in self.conversation_history:
            if message["role"] == "user":
                # Здесь нужно реализовать логику извлечения информации о участниках и их ролях
                # Это может быть сделано с помощью регулярных выражений или более сложных методов NLP
                pass

        return {
            "participants": participants,
            "roles": roles
        }

    def start_conversation(self):
        print("Бот: Здравствуйте! Пожалуйста, отправьте мне ссылку на видео или аудиофайл.")
        while True:
            user_input = input("Пользователь: ")
            if user_input.lower() == 'выход':
                break
            response = self.ask_question(user_input)
            print(f"Бот: {response}")

        return self.extract_info()


if __name__ == "__main__":
    api_key = "your-openai-api-key"
    conversation = Conversation(api_key)
    info = conversation.start_conversation()
    print("Извлеченная информация:", info)
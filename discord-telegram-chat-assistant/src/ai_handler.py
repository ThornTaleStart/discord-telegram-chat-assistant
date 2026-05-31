import openai
from config import Config

class AIHandler:
    def __init__(self):
        openai.api_key = Config.OPENAI_API_KEY
        self.history = []

    def get_response(self, user_message: str) -> str:
        self.history.append({"role": "user", "content": user_message})
        if len(self.history) > Config.CHAT_HISTORY_LIMIT:
            self.history = self.history[-Config.CHAT_HISTORY_LIMIT:]

        try:
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    *self.history
                ],
                max_tokens=150
            )
            reply = response.choices[0].message.content
            self.history.append({"role": "assistant", "content": reply})
            return reply
        except Exception as e:
            return f"Sorry, I encountered an error: {str(e)}"
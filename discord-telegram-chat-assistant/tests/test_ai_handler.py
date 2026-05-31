import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from ai_handler import AIHandler
from unittest.mock import patch

def test_ai_response():
    ai = AIHandler()
    with patch('openai.chat.completions.create') as mock_create:
        mock_create.return_value.choices[0].message.content = "Mock response"
        response = ai.get_response("Hello")
        assert response == "Mock response"
        assert len(ai.history) == 2

def test_history_limit():
    ai = AIHandler()
    with patch('openai.chat.completions.create') as mock_create:
        mock_create.return_value.choices[0].message.content = "Mock"
        for i in range(15):
            ai.get_response(f"Message {i}")
        assert len(ai.history) <= 10

def test_clear_history():
    ai = AIHandler()
    with patch('openai.chat.completions.create') as mock_create:
        mock_create.return_value.choices[0].message.content = "Mock"
        ai.get_response("Test")
        ai.history.clear()
        assert len(ai.history) == 0

if __name__ == "__main__":
    test_ai_response()
    test_history_limit()
    test_clear_history()
    print("All tests passed.")
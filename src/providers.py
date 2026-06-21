from abc import ABC, abstractmethod
from groq import Groq

class AIProvider(ABC):
    @abstractmethod
    def generate_text(self, prompt: str) -> str:
        """AI Provider interface for generating text based on a prompt."""
        pass

class GroqProvider(AIProvider):
    def __init__(self, api_key: str, oracle_model: str):
        self.client = Groq(api_key=api_key)
        self.oracle_model = oracle_model

    def generate_text(self, prompt: str) -> str:
        """Generate text using Groq's API."""
        response = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model=self.oracle_model,
        )
        content = response.choices[0].message.content
        if content is None:
            return "No content generated."
        return content
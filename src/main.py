from groq import Groq

from config import get_settings


def initialize_client(api_key: str) -> Groq:
    """Initialize and return Groq client."""
    return Groq(api_key=api_key)


def main():
    """Main function to run the chat completion."""
    settings = get_settings()
    client = initialize_client(api_key=settings.api_key)

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Explain the importance of fast language models",
            }
        ],
        model=settings.oracle_model,
    )

    print(chat_completion.choices[0].message.content)


if __name__ == "__main__":
    main()

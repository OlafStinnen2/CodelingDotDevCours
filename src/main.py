import os
from groq import Groq


def initialize_client(groq_api_key: str) -> Groq:
    """Initialize and return Groq client."""
    return Groq(api_key=groq_api_key)


def main():
    """Main function to run the chat completion."""
    client = initialize_client(groq_api_key=os.environ.get("API_KEY", ""))

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Explain the importance of fast language models",
            }
        ],
        model=os.environ.get("ORACLE_MODEL", ""),
    )

    print(chat_completion.choices[0].message.content)


if __name__ == "__main__":
    main()

from providers import get_ai_provider


def main():
    """Main function to run the chat completion."""
    provider = get_ai_provider()
    response = provider.generate_text("Explain the importance of fast language models")
    print(response)

if __name__ == "__main__":
    main()

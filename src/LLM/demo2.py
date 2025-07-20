from dotenv import load_dotenv
import os

load_dotenv()


try:
    openai_key = os.getenv("OPENAI_API_KEY")
    anthropic_key = os.getenv("ANTHROPIC_API_KEY")

    # Test API key
    if openai_key:
        print("✅ OpenAI API key found!")
    else:
        print("❌ OpenAI API key not found in .env")

    if anthropic_key:
        print("✅ Anthropic API key found!")
    else:
        print("❌ Anthropic API key not found in .env")
except Exception as e:
    print(f"An error occurred while checking API keys: {e}")

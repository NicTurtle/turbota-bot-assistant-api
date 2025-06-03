from openai import AsyncOpenAI
from config import OPENAI_API_KEY

client = AsyncOpenAI(api_key=OPENAI_API_KEY)

async def ask_gpt(user_message: str) -> str:
    try:
        response = await client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an AI assistant named TurbotaBot. "
                        "Your task is to emotionally support Ukrainians, "
                        "showing care, empathy, and psychological understanding."
                    )
                },
                {"role": "user", "content": user_message}
            ],
            max_tokens=100
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"[GPT ERROR]: {e}")
        return "An error occurred while contacting GPT. Please try again later."

async def test_openai_token() -> str:
    try:
        response = await client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "ping"},
                {"role": "user", "content": "ping"}
            ],
            max_tokens=1
        )
        return "✅ OpenAI API Key: valid"
    except Exception as e:
        print(f"[TOKEN ERROR]: {e}")
        return "❌ OpenAI API Key: connection error"

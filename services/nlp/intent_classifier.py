from openai import AsyncOpenAI
from config import OPENAI_API_KEY
from .prompt_templates import INTENT_SYSTEM_PROMPT

client = AsyncOpenAI(api_key=OPENAI_API_KEY)

async def detect_intent(user_input: str) -> dict:
    """
    Определение намерения пользователя через GPT.
    Возвращает JSON-словарь с полем intent и параметрами.
    """
    messages = [
        {"role": "system", "content": INTENT_SYSTEM_PROMPT},
        {"role": "user", "content": user_input}
    ]

    response = await client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        temperature=0.3
    )

    content = response.choices[0].message.content.strip()
    try:
        return eval(content) if content.startswith("{") else {"intent": "unknown", "raw": content}
    except Exception:
        return {"intent": "unknown", "raw": content}

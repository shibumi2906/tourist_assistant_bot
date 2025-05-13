from openai import AsyncOpenAI
from config import OPENAI_API_KEY

client = AsyncOpenAI(api_key=OPENAI_API_KEY)

async def get_city_attractions_gpt(city: str, language: str = "ru") -> str:
    prompt = (
        f"Составь список из 5 популярных достопримечательностей в городе {city} "
        f"с коротким описанием, зачем туда идти, и примерным временем посещения. "
        f"Ответ дай на языке: {language}."
    )

    response = await client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

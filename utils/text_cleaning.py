import re

def clean_text(text: str) -> str:
    """
    Удаляет лишние пробелы, спецсимволы и нормализует регистр.
    """
    text = text.strip().lower()
    text = re.sub(r"[^\w\s\-]", "", text)
    return text

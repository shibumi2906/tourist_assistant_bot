from datetime import datetime
import re

def parse_date_from_text(text: str) -> str | None:
    """
    Пробует извлечь дату в формате YYYY-MM-DD из текста.
    Возвращает строку или None.
    """
    match = re.search(r"(\d{1,2})[.\-/](\d{1,2})[.\-/](\d{2,4})", text)
    if not match:
        return None

    day, month, year = match.groups()
    year = "20" + year if len(year) == 2 else year

    try:
        parsed = datetime.strptime(f"{year}-{month}-{day}", "%Y-%m-%d")
        return parsed.strftime("%Y-%m-%d")
    except ValueError:
        return None

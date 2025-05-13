def generate_aviasales_link(origin: str, destination: str, date: str) -> str:
    """
    Формирует ссылку на поиск билетов на Aviasales.
    Дата в формате YYYY-MM-DD.
    """
    formatted_date = date.replace("-", "")
    return f"https://www.aviasales.ru/search/{origin[:3].upper()}{formatted_date[:4]}{destination[:3].upper()}1"

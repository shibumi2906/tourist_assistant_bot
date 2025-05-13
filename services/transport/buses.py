def generate_flixbus_link(from_city: str, to_city: str, date: str) -> str:
    return f"https://global.flixbus.com/search?from={from_city}&to={to_city}&departureDate={date}"

def generate_omio_link(from_city: str, to_city: str, date: str) -> str:
    return f"https://www.omio.com/search/{from_city}/{to_city}/{date}"

def generate_busfor_link(from_city: str, to_city: str) -> str:
    return f"https://busfor.ru/{from_city.lower()}-{to_city.lower()}"


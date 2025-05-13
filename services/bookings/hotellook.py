def generate_hotellook_link(city: str) -> str:
    return f"https://search.hotellook.com/?location={city.replace(' ', '%20')}"


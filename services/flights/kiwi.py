def generate_kiwi_link(origin: str, destination: str, date: str) -> str:
    return (
        f"https://www.kiwi.com/en/search/results/"
        f"{origin.upper()}/{destination.upper()}/{date}"
    )

def generate_skyscanner_link(origin: str, destination: str, date: str) -> str:
    return (
        f"https://www.skyscanner.com/transport/flights/{origin.lower()}/{destination.lower()}/{date}/"
    )

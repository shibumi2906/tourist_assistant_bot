from urllib.parse import urlencode

def generate_google_maps_link(origin: str, destination: str) -> str:
    base = "https://www.google.com/maps/dir/?api=1"
    params = {
        "origin": origin,
        "destination": destination,
        "travelmode": "transit"
    }
    return f"{base}&{urlencode(params)}"

def generate_yandex_maps_link(origin: str, destination: str) -> str:
    return (
        f"https://yandex.ru/maps/?rtext={origin.replace(' ', '+')}~{destination.replace(' ', '+')}&rtt=auto"
    )

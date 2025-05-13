def generate_rzd_link(from_city: str, to_city: str, date: str) -> str:
    return (
        f"https://rzd.ru/"
        f"?from={from_city.replace(' ', '+')}&to={to_city.replace(' ', '+')}&date={date}"
    )

def generate_tutu_link(from_city: str, to_city: str, date: str) -> str:
    return (
        f"https://www.tutu.ru/poezda/?from={from_city}&to={to_city}&date={date}"
    )

RU_CITIES = {
    "москва", "санкт-петербург", "казань", "новосибирск", "екатеринбург", "ростов", "нижний новгород"
}

def is_city_in_russia(city: str) -> bool:
    return city.lower() in RU_CITIES

def normalize_city_name(city: str) -> str:
    return city.strip().title()

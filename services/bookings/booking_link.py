from urllib.parse import urlencode

def generate_booking_url(city: str, checkin: str = "", checkout: str = "", adults: int = 2) -> str:
    base_url = "https://www.booking.com/searchresults.html"
    params = {
        "ss": city,
        "group_adults": adults
    }
    if checkin:
        y, m, d = checkin.split("-")
        params.update({
            "checkin_year": y,
            "checkin_month": m,
            "checkin_monthday": d
        })
    if checkout:
        y, m, d = checkout.split("-")
        params.update({
            "checkout_year": y,
            "checkout_month": m,
            "checkout_monthday": d
        })

    return f"{base_url}?{urlencode(params)}"

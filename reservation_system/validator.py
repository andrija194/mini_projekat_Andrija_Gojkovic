"""Jedna odgovornost: pretvaranje i validacija ulaznog reda."""
from .models import Reservation


def parse_reservation(row: dict[str, str]) -> Reservation:
    reservation_id = row["id"].strip()
    guest = row["guest"].strip()
    nights = int(row["nights"])
    price = float(row["price_per_night"])
    if not reservation_id or not guest or nights <= 0 or price < 0:
        raise ValueError("Neispravni podaci")
    # NaN i beskonačnost nijesu validne cijene.
    from math import isfinite
    if not isfinite(price):
        raise ValueError("Cijena mora biti konačan broj")
    return Reservation(reservation_id, guest, nights, price)

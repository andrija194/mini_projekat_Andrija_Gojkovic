"""Početna monolitna implementacija obrade hotelskih rezervacija."""
import csv
from math import isfinite
from pathlib import Path


def process_reservations(csv_path: str) -> dict:
    valid = []
    invalid = []
    with Path(csv_path).open(newline="", encoding="utf-8") as file:
        for row in csv.DictReader(file):
            try:
                reservation_id = row["id"].strip()
                guest = row["guest"].strip()
                nights = int(row["nights"])
                price = float(row["price_per_night"])
                if not reservation_id or not guest or nights <= 0 or price < 0 or not isfinite(price):
                    raise ValueError("Neispravni podaci")
                valid.append({"id": reservation_id, "guest": guest, "total": round(nights * price, 2)})
            except (ValueError, KeyError, TypeError) as error:
                invalid.append({"row": row, "reason": str(error)})
    result = {"valid": valid, "invalid": invalid, "revenue": round(sum(r["total"] for r in valid), 2)}
    print(f"Validne: {len(valid)}, Nevalidne: {len(invalid)}, Prihod: {result['revenue']:.2f} EUR")
    return result


if __name__ == "__main__":
    process_reservations(Path(__file__).resolve().parent / "reservations.csv")

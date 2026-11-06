"""Ulazna tačka: povezivanje konkretnih implementacija (composition root)."""
from pathlib import Path
from reservation_system.repository import CsvReservationSource
from reservation_system.reporter import ConsoleReservationReporter
from reservation_system.service import ReservationService


def main() -> None:
    csv_path = Path(__file__).resolve().parent / "reservations.csv"
    ReservationService(CsvReservationSource(csv_path), ConsoleReservationReporter()).process()


if __name__ == "__main__":
    main()

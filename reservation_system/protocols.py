"""Apstrakcije (DIP): servis poznaje samo ove ugovore."""
from typing import Protocol
from .models import ProcessingResult


class ReservationSource(Protocol):
    def load(self) -> list[dict[str, str]]:
        """Vrati sirove rezervacije, nezavisno od načina čuvanja."""
        ...


class ReservationReporter(Protocol):
    def report(self, result: ProcessingResult) -> None:
        """Prikaži ili sačuvaj obrađeni rezultat."""
        ...

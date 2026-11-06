"""Jedna odgovornost: učitavanje CSV rezervacija."""
import csv
from pathlib import Path


class CsvReservationSource:
    def __init__(self, path: str | Path) -> None:
        self.path = Path(path)

    def load(self) -> list[dict[str, str]]:
        with self.path.open(newline="", encoding="utf-8-sig") as file:
            return list(csv.DictReader(file))

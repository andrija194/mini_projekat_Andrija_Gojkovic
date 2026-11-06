"""Jedna odgovornost: konzolno izvještavanje."""
from .models import ProcessingResult


class ConsoleReservationReporter:
    def report(self, result: ProcessingResult) -> None:
        print(f"Validne: {len(result.valid)}, Nevalidne: {len(result.invalid)}, Prihod: {result.revenue:.2f} EUR")

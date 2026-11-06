"""Obrada rezervacija nezavisna od CSV-a i načina prikaza rezultata."""
from .models import InvalidReservation, ProcessedReservation, ProcessingResult
from .protocols import ReservationReporter, ReservationSource
from .validator import parse_reservation


class ReservationService:
    def __init__(self, source: ReservationSource, reporter: ReservationReporter) -> None:
        self.source = source
        self.reporter = reporter

    def process(self) -> ProcessingResult:
        valid: list[ProcessedReservation] = []
        invalid: list[InvalidReservation] = []
        for row in self.source.load():
            try:
                reservation = parse_reservation(row)
                valid.append(ProcessedReservation(
                    reservation.id, reservation.guest,
                    round(reservation.nights * reservation.price_per_night, 2),
                ))
            except (ValueError, KeyError, TypeError, AttributeError) as error:
                invalid.append(InvalidReservation(row, str(error)))
        result = ProcessingResult(valid, invalid, round(sum(item.total for item in valid), 2))
        self.reporter.report(result)
        return result

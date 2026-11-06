from reservation_system.models import ProcessingResult
from reservation_system.service import ReservationService


class FakeSource:
    def __init__(self, rows: list[dict[str, str]]) -> None:
        self.rows = rows

    def load(self) -> list[dict[str, str]]:
        return self.rows


class FakeReporter:
    def __init__(self) -> None:
        self.results: list[ProcessingResult] = []

    def report(self, result: ProcessingResult) -> None:
        self.results.append(result)


def make_service(rows: list[dict[str, str]]) -> tuple[ReservationService, FakeReporter]:
    reporter = FakeReporter()
    return ReservationService(FakeSource(rows), reporter), reporter


def test_valid_reservation_calculates_total() -> None:
    service, reporter = make_service([{"id": "1", "guest": "Ana", "nights": "3", "price_per_night": "80"}])
    result = service.process()
    assert len(result.valid) == 1
    assert result.valid[0].total == 240
    assert result.revenue == 240
    assert reporter.results == [result]


def test_invalid_nights_are_rejected() -> None:
    service, _ = make_service([{"id": "2", "guest": "Marko", "nights": "0", "price_per_night": "50"}])
    result = service.process()
    assert len(result.valid) == 0
    assert len(result.invalid) == 1
    assert result.revenue == 0


def test_mixed_rows_and_missing_field() -> None:
    service, _ = make_service([
        {"id": "3", "guest": "Jelena", "nights": "2", "price_per_night": "40"},
        {"id": "4", "guest": "Ivan", "nights": "1"},
        {"id": "5", "guest": "Mia", "nights": "1", "price_per_night": "20"},
    ])
    result = service.process()
    assert len(result.valid) == 2
    assert len(result.invalid) == 1
    assert result.revenue == 100


def test_empty_source_reports_zero() -> None:
    service, reporter = make_service([])
    result = service.process()
    assert result.revenue == 0
    assert reporter.results == [result]

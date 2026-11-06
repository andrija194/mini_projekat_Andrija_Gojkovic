"""Integracioni test: stvarni CSV iz privremenog direktorijuma."""
from pathlib import Path
from reservation_system.repository import CsvReservationSource
from reservation_system.service import ReservationService
from reservation_system.models import ProcessingResult


class CollectingReporter:
    def __init__(self) -> None:
        self.last: ProcessingResult | None = None

    def report(self, result: ProcessingResult) -> None:
        self.last = result


def test_csv_source_with_service(tmp_path: Path) -> None:
    path = tmp_path / "input.csv"
    path.write_text("id,guest,nights,price_per_night\nA,Ana,2,75\nB,Marko,0,50\n", encoding="utf-8")
    reporter = CollectingReporter()
    result = ReservationService(CsvReservationSource(path), reporter).process()
    assert len(result.valid) == 1
    assert len(result.invalid) == 1
    assert result.revenue == 150
    assert reporter.last is result

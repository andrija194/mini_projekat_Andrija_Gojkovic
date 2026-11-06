from dataclasses import dataclass


@dataclass(frozen=True)
class Reservation:
    id: str
    guest: str
    nights: int
    price_per_night: float


@dataclass(frozen=True)
class ProcessedReservation:
    id: str
    guest: str
    total: float


@dataclass(frozen=True)
class InvalidReservation:
    row: dict[str, str]
    reason: str


@dataclass(frozen=True)
class ProcessingResult:
    valid: list[ProcessedReservation]
    invalid: list[InvalidReservation]
    revenue: float

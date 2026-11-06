"""Dodatni testovi validacije, bez čitanja datoteka."""
import pytest
from reservation_system.validator import parse_reservation


def test_whitespace_is_trimmed() -> None:
    result = parse_reservation({"id": "  R1 ", "guest": " Ana ", "nights": "2", "price_per_night": "50"})
    assert result.id == "R1"
    assert result.guest == "Ana"


@pytest.mark.parametrize("price", ["-1", "nan", "inf"])
def test_invalid_price_is_rejected(price: str) -> None:
    with pytest.raises(ValueError):
        parse_reservation({"id": "R2", "guest": "Ana", "nights": "1", "price_per_night": price})

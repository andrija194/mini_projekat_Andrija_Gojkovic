import pytest
from api import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


@pytest.mark.parametrize(
    ("nights", "price", "total"),
    [(3, 4500, 13500), (1, 0, 0), (365, 1_000_000, 365_000_000)],
)
def test_quote(nights: int, price: int, total: int) -> None:
    response = client.post(
        "/reservations/quote",
        json={"nights": nights, "price_per_night_cents": price},
    )
    assert response.status_code == 200
    assert response.json() == {"total_cents": total}


@pytest.mark.parametrize(
    "payload",
    [
        {"nights": 0, "price_per_night_cents": 4500},
        {"nights": 366, "price_per_night_cents": 4500},
        {"nights": 1, "price_per_night_cents": -1},
        {"nights": 1, "price_per_night_cents": 1_000_001},
        {"nights": "1", "price_per_night_cents": 4500},
        {"nights": True, "price_per_night_cents": 4500},
        {"nights": 1},
        {"nights": 1, "price_per_night_cents": 4500, "discount": 90},
    ],
)
def test_invalid_quote(payload: dict[str, object]) -> None:
    response = client.post("/reservations/quote", json=payload)
    assert response.status_code == 422


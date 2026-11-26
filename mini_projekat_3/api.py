from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict, Field

app = FastAPI(title="API za hotelske rezervacije")


class Reservation(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)

    nights: int = Field(ge=1, le=365)
    price_per_night_cents: int = Field(ge=0, le=1_000_000)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/reservations/quote")
def quote(reservation: Reservation) -> dict[str, int]:
    return {
        "total_cents": reservation.nights * reservation.price_per_night_cents
    }


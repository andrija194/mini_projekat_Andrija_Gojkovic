# Mini projekat 3 – Testiran i obezbijeđen API

**Student:** Andrija Gojković  
**Predmet:** Napredno programiranje

FastAPI servis računa ukupnu cijenu hotelske rezervacije. Cijena se unosi u centima da bi račun bio tačan bez zaokruživanja.

| Metoda i putanja | Namjena |
| --- | --- |
| `GET /health` | Vraća `{"status":"ok"}` |
| `POST /reservations/quote` | Prima npr. `{"nights":3,"price_per_night_cents":4500}` i vraća `{"total_cents":13500}` |

Neispravan unos vraća HTTP 422. Dozvoljeno je 1–365 noćenja i 0–1.000.000 centi po noćenju.

## Pokretanje i provjere

Iz foldera `mini_projekat_3`, u virtuelnom okruženju:

```shell
python -m pip install -r requirements-dev.txt
python -m uvicorn api:app
```

Interaktivna dokumentacija je na http://127.0.0.1:8000/docs.

```shell
python -m ruff check .
python -m mypy api.py test_api.py
python -m pytest -q
python -m bandit api.py
python -m pip_audit -r requirements.txt
```

Pytest pokriva provjeru stanja servisa, obračun, dozvoljene granice, pogrešne tipove, nedostajuće i dodatne podatke. GitHub Actions pokreće iste provjere pri push-u i pull request-u. Bandit pregleda kod servisa, a pip-audit provjerava poznate ranjivosti u zavisnostima aplikacije.

## Rizici i mjere

| Rizik | Mjera |
| --- | --- |
| Negativna cijena ili nedozvoljen broj noćenja daju pogrešan iznos. | Model provjerava donje i gornje granice prije obračuna. |
| Implicitna konverzija tipova može prihvatiti tekst ili logičku vrijednost kao broj. | Stroga validacija zahtijeva cijele brojeve i odbija dodatna polja. |
| Zaokruživanje brojeva sa zarezom može promijeniti obračun. | I unos cijene i rezultat koriste cijele iznose u centima. |
| Zavisnost može sadržati poznatu ranjivost. | CI pokreće pip-audit nad zavisnostima aplikacije i prijavljuje nalaze u logu. |

Servis računa ponudu. Podaci se ne upisuju u bazu.


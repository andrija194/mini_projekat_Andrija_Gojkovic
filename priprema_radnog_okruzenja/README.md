# Priprema radnog okruženja

**Predmet:** Napredno programiranje  
**Student:** Andrija Gojković  
**Alati:** Python 3.12+, Visual Studio Code, GitHub, pytest, Ruff

## Opis zadatka

Cilj domaćeg zadatka je priprema Python radnog okruženja, korišćenje GitHub-a, alata `ruff` i `pytest`, kao i implementacija jednostavne funkcije uz pomoć AI asistenta.

Funkcija `prosjecna_cijena(cijene)` prima listu cijena i vraća njihov aritmetički prosjek. Za praznu listu prijavljuje `ValueError`. Neispravni tipovi, negativne i nekonačne vrijednosti se odbijaju kako bi rezultat imao smisla.

## Struktura

```text
priprema_radnog_okruzenja/
├── prosjecna_cijena.py
├── tests/
│   └── test_prosjecna_cijena.py
├── requirements.txt
├── pytest.ini
├── ruff.toml
├── .gitignore
└── README.md
```

## Pokretanje

U terminalu VS Code-a, iz foldera `priprema_radnog_okruzenja`:

```powershell
python -m pip install -r requirements.txt
python prosjecna_cijena.py
python -m pytest -v
python -m ruff check .
```

Ako Windows ne prepoznaje komandu `python`, može se napraviti i koristiti virtuelno okruženje preko putanje do instaliranog Python interpretera. Na primjer, nakon kreiranja `.venv`:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pytest -v
.\.venv\Scripts\python.exe -m ruff check .
```

Primjer izlaza programa:

```text
Prosječna cijena: 20.00 EUR
```

## Testiranje

Testovi provjeravaju prosjek više cijena, jednu cijenu, praznu listu, negativnu cijenu i `nan` vrijednost. `pytest` se koristi za automatsko testiranje, a `ruff` za provjeru stila i jednostavnih grešaka u kodu.

## AI asistent – korišćeni upiti i uočeni nedostaci

Korišćen je ChatGPT za pomoć u pripremi rješenja. Stvarni zahtjev bio je da se zadatak **„Priprema radnog okruženja“** sa fotografije uradi kao zaseban domaći, sa funkcijom `prosjecna_cijena`, testom i uputstvom za predaju. Zatraženo je i da se prati profesorova napomena o načinu postavljanja na GitHub.

**Odluke i provjere pri izradi:**

- Početna ideja prosjeka `sum(cijene) / len(cijene)` ne obrađuje praznu listu: zato je dodata razumljiva greška `ValueError`.
- Jednostavan prosjek ne prepoznaje nelogične negativne cijene i vrijednosti `nan` / `inf`: dodata je validacija ulaza.
- Dodati su testovi normalnog slučaja i rubnih slučajeva, kako bi se ispravke mogle provjeriti.
- Kod je tipiziran i pripremljen za provjeru alatom Ruff.

**Lična provjera prije predaje:** U VS Code-u izvršiti komande za `pytest` i `ruff`, provjeriti da prolaze i ovdje po želji upisati rezultate. Ne treba tvrditi da je provjera izvršena na lokalnom računaru prije nego što se zaista pokrene.

## Predaja

Prema napomeni profesora, **isti GitHub repozitorijum koristi se za sve mini projekte i završni projekat**. Ovaj domaći zadatak zato ide u zaseban folder `priprema_radnog_okruzenja` u već postojećem repozitorijumu, bez brisanja drugog projekta. Link tog repozitorijuma je predaja.

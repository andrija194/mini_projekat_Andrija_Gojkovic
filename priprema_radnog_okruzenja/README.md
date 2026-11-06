
# Priprema radnog okruženja

**Predmet:** Napredno programiranje  
**Student:** Andrija Gojković  
**Tehnologije:** Python 3.15.2, Visual Studio Code, Git, GitHub, pytest, Ruff

## 1. Opis projekta

U okviru ovog zadatka pripremljeno je radno okruženje za razvoj i testiranje Python programa.

Za pisanje i pokretanje koda korišćen je Visual Studio Code, dok su za provjeru ispravnosti i kvaliteta koda korišćeni pytest i Ruff. Projekat je postavljen na GitHub radi čuvanja i praćenja izmjena.

Uz pomoć ChatGPT-a implementirana je funkcija `prosjecna_cijena`, koja računa aritmetičku sredinu cijena iz zadate liste.

## 2. Implementacija funkcije

Funkcija `prosjecna_cijena(cijene)` prima listu numeričkih vrijednosti i vraća njihov prosjek.

Primjer korišćenja:

```python
cijene = [10, 20, 30]
rezultat = prosjecna_cijena(cijene)
print(rezultat)
```

Rezultat:

```text
20.0
```

Pored osnovnog izračunavanja, funkcija provjerava ispravnost ulaznih podataka:

- Lista ne smije biti prazna.
- Sve cijene moraju biti numeričke vrijednosti.
- Negativne cijene nijesu dozvoljene.
- Vrijednosti `nan` i `inf` nijesu dozvoljene.
- Logičke vrijednosti `True` i `False` ne prihvataju se kao cijene.

Za neispravne vrijednosti funkcija prijavljuje odgovarajuću grešku (`ValueError` ili `TypeError`).

## 3. Struktura projekta

```text
priprema_radnog_okruzenja/
│
├── prosjecna_cijena.py
├── README.md
├── requirements.txt
├── pytest.ini
├── ruff.toml
├── .gitignore
│
└── tests/
    └── test_prosjecna_cijena.py
```

- `prosjecna_cijena.py` – implementacija funkcije.
- `tests/test_prosjecna_cijena.py` – automatski testovi.
- `requirements.txt` – potrebne biblioteke.
- `pytest.ini` – podešavanja za pytest.
- `ruff.toml` – podešavanja za Ruff.
- `README.md` – dokumentacija projekta.

## 4. Pokretanje programa

Za instalaciju potrebnih biblioteka koristi se:

```powershell
python -m pip install -r requirements.txt
```

Pokretanje programa:

```powershell
python prosjecna_cijena.py
```

Rezultat izvršavanja:

```text
Prosječna cijena: 20.00 EUR
```

Pokretanje testova:

```powershell
python -m pytest -v
```

Provjera kvaliteta koda:

```powershell
python -m ruff check .
```

Provjera formatiranja:

```powershell
python -m ruff format --check .
```

## 5. Testiranje

Za testiranje je korišćen pytest. Napisano je pet testova koji provjeravaju:

1. Izračunavanje prosjeka više cijena.
2. Izračunavanje prosjeka jedne cijene.
3. Ponašanje funkcije kada je lista prazna.
4. Obradu negativnih cijena.
5. Obradu nekonačnih numeričkih vrijednosti.

Nakon pokretanja testova dobijen je rezultat:

```text
5 passed in 0.17s
```

Svih pet testova uspješno je prošlo.

### Provjera Ruff alatom

Za provjeru kvaliteta koda pokrenuta je komanda:

```powershell
python -m ruff check .
```

Rezultat:

```text
All checks passed!
```

Provjera formatiranja:

```powershell
python -m ruff format --check .
```

Rezultat:

```text
3 files already formatted
```

## 6. Korišćenje AI asistenta

Tokom rada korišćen je ChatGPT za pomoć pri implementaciji funkcije, pisanju testova, rješavanju problema tokom pokretanja i pripremi dokumentacije.

### 6.1. Korišćeni upiti

**Upit 1:**

> Hajde ovaj projekat da odradimo zasebno

Uz upit je dostavljena fotografija zadatka. Na osnovu nje pripremljena je Python funkcija za računanje prosječne cijene, zajedno sa testovima i konfiguracijom potrebnih alata.

**Upit 2:**

> Ovo je skroz drugi domaci znaci radimo ga tako i upoldujemo kao sto kaze

Ovim upitom dodatno je pojašnjena organizacija projekta. Datoteke su smještene u poseban folder unutar postojećeg GitHub repozitorijuma.

**Upit 3:**

> kako da viidm da li sve radi

Zatraženo je objašnjenje pokretanja Python programa, pytest testova i Ruff provjera u VS Code-u.

**Upit 4:**

> hajde mi readme poboljsaj za profesora

Zatražena je pomoć pri sređivanju dokumentacije i opisivanju korišćenih AI upita, nedostataka i izvršenih provjera.

### 6.2. Uočeni nedostaci i poboljšanja

Prilikom analize jednostavnog načina izračunavanja prosjeka uočeno je nekoliko mogućih problema.

| Uočeni nedostatak | Poboljšanje |
|---|---|
| Prazna lista može izazvati dijeljenje nulom. | Dodata provjera prazne liste. |
| Negativne cijene mogu biti prihvaćene kao ispravne. | Dodata provjera negativnih vrijednosti. |
| Vrijednosti `nan` i `inf` mogu dovesti do neispravnog rezultata. | Dodata provjera konačnosti brojeva. |
| Neodgovarajući tip podataka može izazvati nejasnu grešku. | Dodata provjera tipova podataka. |
| Samo jedan primjer nije dovoljan za provjeru funkcionalnosti. | Napisano pet pytest testova. |

Navedeni problemi predstavljaju nedostatke jednostavnog pristupa računanju prosjeka. Provjere su uključene u rješenje pripremljeno uz pomoć AI asistenta.

### 6.3. Problemi tokom pokretanja

Prilikom prvog pokretanja Python programa terminal nije prepoznavao komandu `python`.

Problem je riješen korišćenjem Python interpretera iz virtuelnog okruženja `.venv`.

Tokom pokretanja Ruff-a pojavila se greška:

```text
No module named ruff
```

Nakon instalacije biblioteke Ruff, provjera koda je uspješno izvršena.

Takođe, prilikom unošenja pojedinih komandi pojavile su se greške zbog pogrešno unesenih znakova. Nakon ispravke komandi program i testovi su uspješno pokrenuti.

### 6.4. Provjera rješenja

Nakon pripreme projekta izvršene su sljedeće provjere:

- Pokrenut je program `prosjecna_cijena.py`.
- Provjeren je rezultat izračunavanja prosječne cijene.
- Pokrenuto je pet pytest testova.
- Izvršena je Ruff provjera kvaliteta koda.
- Provjereno je formatiranje Python datoteka.
- Projekat je postavljen na GitHub.

Program je prikazao očekivani rezultat, svih pet testova je prošlo, a Ruff nije prijavio probleme.

## 7. Zaključak

Kroz ovaj zadatak pripremljeno je radno okruženje za razvoj Python programa i korišćenje osnovnih alata za testiranje i provjeru kvaliteta koda.

Implementirana je funkcija za računanje prosječne cijene, uz dodatne provjere ulaznih podataka.

Korišćenje AI asistenta pomoglo je pri izradi funkcije i testova, dok je ispravnost provjerena njihovim pokretanjem u Visual Studio Code-u.

## 8. GitHub repozitorijum

https://github.com/andrija194/mini_projekat_Andrija_Gojkovic

Datoteke ovog zadatka nalaze se u folderu `priprema_radnog_okruzenja`.

# Priprema radnog okruženja

**Predmet:** Napredno programiranje  
**Student:** Andrija Gojković    
**Tehnologije:** Python 3.15.2, Visual Studio Code, GitHub, pytest, Ruff

## 1. Opis zadatka

Cilj ovog domaćeg zadatka je priprema radnog okruženja za razvoj Python aplikacija, upoznavanje sa alatima za testiranje i provjeru kvaliteta koda, kao i korišćenje AI asistenta pri implementaciji jednostavne funkcije.

U okviru zadatka korišćeni su:

- **Python** – programski jezik za implementaciju funkcije.
- **Visual Studio Code** – razvojno okruženje za pisanje i pokretanje koda.
- **Git i GitHub** – verzionisanje i čuvanje projekta.
- **pytest** – automatsko testiranje funkcionalnosti.
- **Ruff** – provjera kvaliteta i formatiranja Python koda.
- **ChatGPT** – pomoć pri implementaciji, testiranju i dokumentovanju.

## 2. Implementacija funkcije

Uz pomoć AI asistenta implementirana je funkcija `prosjecna_cijena(cijene)`.

Funkcija prima listu cijena i računa njihov aritmetički prosjek.

Primjer:

```python
cijene = [10, 20, 30]
rezultat = prosjecna_cijena(cijene)
print(rezultat)
```

Rezultat:

```text
20.0
```

Prosječna cijena računa se tako što se zbir svih cijena podijeli brojem elemenata u listi.

Pored osnovnog izračunavanja, dodate su provjere ulaznih podataka:

- Lista ne smije biti prazna.
- Cijene moraju biti numeričke vrijednosti.
- Negativne cijene nijesu dozvoljene.
- Vrijednosti `nan` i `inf` nijesu dozvoljene.
- Logičke vrijednosti (`True` i `False`) ne prihvataju se kao cijene.

Ako je lista prazna ili sadrži nedozvoljenu numeričku vrijednost, funkcija prijavljuje `ValueError`. Za neodgovarajući tip podatka prijavljuje `TypeError`.

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

Datoteka `prosjecna_cijena.py` sadrži implementaciju funkcije, dok `test_prosjecna_cijena.py` sadrži automatske testove.

Datoteka `requirements.txt` definiše potrebne biblioteke, a `ruff.toml` podešavanja za provjeru kvaliteta koda.

## 4. Pokretanje projekta

Projekat je pokrenut u Visual Studio Code-u na Windows operativnom sistemu.

Potrebno je instalirati biblioteke:

```powershell
python -m pip install -r requirements.txt
```

Pokretanje programa:

```powershell
python prosjecna_cijena.py
```

Rezultat za primjer iz programa:

```text
Prosječna cijena: 20.00 EUR
```

Pokretanje automatskih testova:

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

Na mom računaru korišćeno je Python virtuelno okruženje `.venv`, jer komanda `python` u početku nije bila dostupna direktno iz Windows terminala.

## 5. Testiranje

Za testiranje funkcije korišćena je biblioteka `pytest`.

Implementirano je pet testova:

| Test | Šta provjerava |
|---|---|
| `test_prosjecna_cijena_vise_vrijednosti` | Ispravan prosjek više cijena |
| `test_prosjecna_cijena_jedna_vrijednost` | Prosjek liste sa jednom cijenom |
| `test_prazna_lista` | Odbijanje prazne liste |
| `test_negativna_cijena` | Odbijanje negativnih cijena |
| `test_nekonacna_cijena` | Odbijanje vrijednosti `nan` |

### 5.1. Rezultati pytest testiranja

Testovi su pokrenuti u VS Code terminalu.

Dobijeni rezultat:

```text
5 passed in 0.17s
```

Svih pet testova uspješno je prošlo, bez prijavljenih grešaka.

### 5.2. Provjera Ruff alatom

Ruff je korišćen za provjeru potencijalnih grešaka, stila i formatiranja koda.

Nakon instalacije pokrenuta je komanda:

```powershell
python -m ruff check .
```

Dobijeni rezultat:

```text
All checks passed!
```

Zatim je provjereno formatiranje:

```powershell
python -m ruff format --check .
```

Rezultat:

```text
3 files already formatted
```

Ovi rezultati potvrđuju da je kod prošao podešene Ruff provjere.

## 6. Korišćenje AI asistenta

Tokom izrade domaćeg zadatka koristio sam ChatGPT kao pomoć pri implementaciji funkcije, pisanju testova, objašnjenju grešaka i pripremi dokumentacije.

### 6.1. Upotrijebljeni upiti

**Upit 1 – Izrada domaćeg zadatka**

Dostavio sam fotografiju zadatka „Priprema radnog okruženja“ i napisao:

> Hajde ovaj projekat da odradimo zasebno

Cilj je bio da se implementira poseban domaći zadatak sa funkcijom `prosjecna_cijena`, testovima i potrebnim podešavanjima.

**Upit 2 – Pojašnjenje zahtjeva**

> Ovo je skroz drugi domaci znaci radimo ga tako i upoldujemo kao sto kaze

Ovim zahtjevom naglasio sam da domaći treba organizovati odvojeno od prethodnog projekta, uz poštovanje profesorovog uputstva o korišćenju istog GitHub repozitorijuma.

**Upit 3 – Provjera rada programa**

> kako da viidm da li sve radi

Tražio sam objašnjenje kako da pokrenem funkciju, pytest testove i Ruff provjere.

**Upit 4 – Poboljšanje dokumentacije**

> hajde mi readme poboljsaj za profesora

Zatražio sam doradu dokumentacije kako bi jasnije prikazivala implementaciju, upotrebu AI-ja, uočene nedostatke i rezultate testiranja.

### 6.2. Uočeni nedostaci i ispravke generisanog rješenja

Prilikom razmatranja početnog pristupa identifikovani su slučajevi koje jednostavna implementacija prosjeka ne obrađuje pravilno.

| Nedostatak početnog pristupa | Predložena ispravka |
|---|---|
| Prazna lista izaziva dijeljenje nulom | Dodata provjera prazne liste i `ValueError` |
| Negativne cijene se prihvataju bez provjere | Dodata provjera nenegativnosti |
| Vrijednosti `nan` i `inf` mogu dati neispravan rezultat | Dodata provjera konačnosti cijena |
| Neodgovarajući tipovi nijesu jasno obrađeni | Dodata provjera tipova i `TypeError` |
| Osnovni primjer ne provjerava granične slučajeve | Dodato pet pytest testova |

Navedene provjere i dorade predložene su uz pomoć AI asistenta. Nijesu sve nastale kao greške tokom izvršavanja programa, već su dio poboljšanja početnog pristupa.

### 6.3. Problemi prilikom pokretanja

Prilikom pokretanja projekta pojavio se problem jer Windows terminal nije prepoznavao komandu `python`.

Problem je riješen korišćenjem Python interpretera iz virtuelnog okruženja `.venv`.

Nakon toga program je uspješno pokrenut i prikazao očekivanu prosječnu cijenu od 20 EUR.

Prilikom prve Ruff provjere pojavila se poruka:

```text
No module named ruff
```

Uz pomoć AI asistenta instalirao sam nedostajuću biblioteku, nakon čega su Ruff provjere uspješno prošle.

Tokom unošenja komandi pojavile su se i greške zbog dodatnih znakova u terminalu. Nakon ispravke komandi program i alati izvršavali su se normalno.

### 6.4. Samostalna provjera

Nakon generisanja projekta samostalno sam u VS Code-u:

1. Pokrenuo funkciju `prosjecna_cijena`.
2. Provjerio rezultat izračunavanja.
3. Pokrenuo svih pet pytest testova.
4. Instalirao Ruff i izvršio provjeru kvaliteta koda.
5. Izvršio provjeru formatiranja.
6. Postavio projekat na GitHub koristeći Git komande.

Svi navedeni koraci uspješno su završeni.

## 7. GitHub repozitorijum

Projekat je postavljen na GitHub:

https://github.com/andrija194/mini_projekat_Andrija_Gojkovic

Prema uputstvu profesora, isti GitHub repozitorijum koristi se za sve mini projekte i završni projekat.

Ovaj domaći nalazi se u posebnom folderu `priprema_radnog_okruzenja`, kako bi bio jasno odvojen od ostalih zadataka.

## 8. Zaključak

Kroz ovaj domaći zadatak pripremio sam radno okruženje za razvoj Python aplikacija i upoznao se sa osnovnim alatima za kontrolu kvaliteta koda.

Implementirana je funkcija `prosjecna_cijena`, uz provjeru ispravnosti ulaznih podataka i automatsko testiranje.

Svih pet pytest testova uspješno je prošlo, a Ruff nije prijavio probleme sa kvalitetom i formatiranjem koda prema korišćenim podešavanjima.

Korišćenje AI asistenta pomoglo mi je pri pisanju i poboljšanju rješenja, dok sam ispravnost provjerio pokretanjem programa i odgovarajućih alata.

Zadatak predstavlja osnovu za naredne mini projekte iz predmeta Napredno programiranje.

# Mini projekat 1 – Restrukturiranje obrade rezervacija

**Predmet:** Napredno programiranje  
**Student:** Andrija Gojković  
**Tehnologije:** Python 3.10+, pytest, typing.Protocol  
**Tema:** Obrada hotelskih rezervacija

## 1. Opis projekta

Cilj projekta je reorganizacija postojeće monolitne Python skripte za obradu hotelskih rezervacija primjenom S i D principa iz SOLID-a.

Početna verzija programa nalazi se u datoteci `monolith.py`. U njoj su učitavanje podataka, validacija, obračun cijena i prikaz rezultata objedinjeni u jednoj skripti.

U poboljšanoj verziji ove odgovornosti podijeljene su u zasebne module kako bi kod bio pregledniji, jednostavniji za održavanje i lakši za testiranje.

Program omogućava:

- Učitavanje rezervacija iz CSV datoteke.
- Provjeru ispravnosti unesenih podataka.
- Izračunavanje ukupne cijene svake validne rezervacije.
- Evidentiranje nevalidnih rezervacija.
- Prikaz broja validnih i nevalidnih rezervacija i ukupnog prihoda.

Rezervacija je validna ako su ID i ime gosta popunjeni, broj noćenja pozitivan cio broj, a cijena po noćenju nenegativan konačan broj.

## 2. Struktura projekta

```text
mini projekat Andrija Gojkovic/
│
├── monolith.py
├── main.py
├── reservations.csv
├── requirements.txt
├── pytest.ini
├── README.md
├── .gitignore
│
├── reservation_system/
│   ├── __init__.py
│   ├── models.py
│   ├── validator.py
│   ├── protocols.py
│   ├── repository.py
│   ├── service.py
│   └── reporter.py
│
└── tests/
    ├── test_service.py
    ├── test_validator.py
    └── test_integration.py
```

Datoteka `__init__.py` označava Python paket i zato ne zahtijeva dodatnu implementaciju.

## 3. Primjena SOLID principa

### 3.1. S – Single Responsibility Principle

Princip jedne odgovornosti podrazumijeva da klasa ili modul treba da ima jednu osnovnu odgovornost.

U reorganizovanoj verziji programa odgovornosti su podijeljene na sljedeći način:

- `CsvReservationSource` – učitavanje podataka iz CSV datoteke.
- `parse_reservation` – validacija i pretvaranje ulaznih podataka u model rezervacije.
- `ReservationService` – obrada rezervacija i obračun ukupnog prihoda.
- `ConsoleReservationReporter` – prikaz rezultata u konzoli.

Na ovaj način promjena načina učitavanja podataka ne zahtijeva promjenu poslovne logike. Isto važi i za promjenu načina prikaza izvještaja.

### 3.2. D – Dependency Inversion Principle

Princip inverzije zavisnosti podrazumijeva da poslovna logika treba da zavisi od apstrakcija, a ne od konkretnih implementacija.

U projektu su pomoću `typing.Protocol` definisana dva interfejsa:

- `ReservationSource` – definiše način dobijanja podataka o rezervacijama.
- `ReservationReporter` – definiše način prikazivanja rezultata.

Klasa `ReservationService` koristi ove interfejse umjesto direktnog povezivanja sa CSV datotekom i konzolnim ispisom.

Konkretne implementacije povezuju se u `main.py`.

Ovakav pristup omogućava da se u testovima koriste zamjenske klase `FakeSource` i `FakeReporter`, bez potrebe za pristupom stvarnoj CSV datoteci.

## 4. Pokretanje programa

Projekat je izrađen u Pythonu i pokretan u razvojnom okruženju Visual Studio Code na Windows operativnom sistemu.

Za instalaciju potrebnih biblioteka koristi se:

```powershell
python -m pip install -r requirements.txt
```

Pokretanje početne monolitne verzije:

```powershell
python monolith.py
```

Pokretanje reorganizovane verzije:

```powershell
python main.py
```

Obje verzije za primjer podataka iz `reservations.csv` prikazuju:

```text
Validne: 3, Nevalidne: 1, Prihod: 780.00 EUR
```

Time je provjereno da reorganizacija koda nije promijenila rezultat obrade datog primjera.

## 5. Testiranje

Za automatsko testiranje korišćen je `pytest`.

Testovi se pokreću komandom:

```powershell
python -m pytest -v
```

Implementirano je ukupno devet testova koji obuhvataju:

- Obračun validnih rezervacija.
- Odbijanje neispravnog broja noćenja.
- Obradu mješovitih validnih i nevalidnih podataka.
- Obradu praznog izvora podataka.
- Uklanjanje nepotrebnih razmaka.
- Odbijanje negativnih i nekonačnih cijena.
- Integraciju CSV izvora sa servisom.

U testovima poslovne logike koriste se zamjenski izvor podataka i reporter, čime se omogućava nezavisno testiranje servisa.

**Rezultat testiranja u VS Code-u:**

```text
9 passed in 0.09s
```

Svih devet testova uspješno je prošlo.

## 6. Korišćenje AI alata

Tokom izrade projekta koristio sam ChatGPT kao pomoć pri pisanju i reorganizaciji koda, organizaciji projekta, dodavanju testova i pripremi dokumentacije.

### 6.1. Korišćeni upiti

U nastavku su navedeni stvarni zahtjevi koje sam koristio tokom rada.

**Upit 1 – Izrada početnog projekta**

Poslao sam fotografiju zadatka sa zahtjevima profesora i potvrdio da želim izradu kompletnog projekta.

Na osnovu toga generisana je početna verzija za obradu hotelskih rezervacija, zajedno sa modularno organizovanom implementacijom.

**Upit 2 – Pokretanje projekta**

> kako pokrecem ovo

Tražio sam objašnjenje kako da instaliram potrebne biblioteke, pokrenem program i izvršim pytest testove u VS Code-u.

**Upit 3 – Poboljšanje generisanog koda**

> hajde poneki fahjlovi su odje prazni hajde mi napravi dobro verziju za predaju i da sve bude kao sto profesor trazi

Nakon pregleda početne verzije zatražio sam dodatnu doradu projekta, jasniju organizaciju i proširenje testiranja.

**Upit 4 – Objašnjenje strukture projekta**

> zastoo je ovaj prazan

Tražio sam objašnjenje zašto je datoteka `__init__.py` gotovo prazna i koja je njena uloga u Python paketu.

**Upit 5 – Dokumentacija**

> hajde odradio dokumenotvanje

Zatražio sam pomoć pri pripremi README dokumentacije, posebno dijela koji se odnosi na korišćenje AI-ja i provjeru generisanog koda.

### 6.2. Izmjene i ispravke generisanog rješenja

Nakon prve verzije projekta zatražio sam poboljšanja, nakon čega je uz pomoć AI-ja pripremljena dopunjena verzija.

Najvažnije izmjene bile su:

1. Izdvajanje validacije u poseban modul `validator.py`, radi jasnijeg razdvajanja odgovornosti.
2. Korišćenje `Protocol` interfejsa za izvor podataka i izvještavanje.
3. Dodavanje zamjenskih klasa za testiranje bez stvarne CSV datoteke.
4. Dodavanje provjera za neispravne cijene, uključujući vrijednosti `nan` i `inf`.
5. Proširenje testova za granične slučajeve.
6. Poboljšanje određivanja putanje do CSV datoteke.

Navedene izmjene pripremljene su uz pomoć AI alata.

### 6.3. Provjera generisanog koda

Nakon dobijanja dopunjene verzije samostalno sam pokrenuo projekat u VS Code-u.

Prilikom početnog pokretanja pojavio se problem jer terminal nije prepoznavao komandu `python`. Uz objašnjenje AI alata koristio sam Python iz virtuelnog okruženja `.venv` i uspješno pokrenuo program.

Zatim sam izvršio sljedeće provjere:

- Pokrenuo sam `monolith.py`.
- Pokrenuo sam `main.py`.
- Uporedio sam rezultate obje verzije.
- Pokrenuo sam svih devet pytest testova.

Obje verzije prikazale su isti rezultat, a svih devet testova je prošlo.

Na osnovu ovih provjera zaključio sam da program ispravno radi za testirane slučajeve i da je reorganizovana verzija zadržala ponašanje početne verzije na korišćenim primjerima.

## 7. Zaključak

Kroz ovaj projekat prikazan je postupak reorganizacije monolitne Python skripte u modularno organizovanu aplikaciju.

Primjenom S principa razdvojene su odgovornosti pojedinačnih komponenti, dok je primjenom D principa smanjena zavisnost poslovne logike od konkretnih implementacija.

Korišćenje `Protocol` interfejsa omogućilo je jednostavniju zamjenu izvora podataka i reportera, što je posebno korisno prilikom automatskog testiranja.

AI alat korišćen je kao pomoć pri izradi i poboljšanju rješenja, dok je funkcionalnost provjerena pokretanjem obje verzije programa i izvršavanjem pytest testova.

Projekat predstavlja praktičan primjer značaja čitljivog, modularnog i testabilnog koda.

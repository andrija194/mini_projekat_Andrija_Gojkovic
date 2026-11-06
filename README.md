
# Mini projekat 1 – Refaktoring obrade rezervacija

**Predmet:** Napredno programiranje  
**Student:** Andrija Gojković  
**Tehnologije:** Python 3.10+, pytest, typing.Protocol  
**Tema:** Obrada hotelskih rezervacija

## 1. Opis projekta

Cilj projekta je refaktoring monolitne Python skripte za obradu hotelskih rezervacija primjenom S i D principa iz SOLID-a.

Početna verzija programa nalazi se u datoteci `monolith.py`. U njoj su učitavanje podataka, validacija, obračun cijena i prikaz rezultata objedinjeni u jednoj skripti.

Refaktorisana verzija razdvaja ove odgovornosti u zasebne module kako bi kod bio pregledniji, jednostavniji za održavanje i lakši za testiranje.

Program omogućava:

- Učitavanje rezervacija iz CSV datoteke.
- Provjeru ispravnosti unesenih podataka.
- Izračunavanje ukupne cijene svake validne rezervacije.
- Evidentiranje nevalidnih rezervacija.
- Prikaz broja validnih i nevalidnih rezervacija i ukupnog prihoda.

Rezervacija je validna ako su ID i ime gosta popunjeni, broj noćenja pozitivan cio broj, a cijena po noćenju nenegativan konačan broj.

Nevalidne rezervacije se evidentiraju, ali ne prekidaju obradu ostalih rezervacija.

## 2. Struktura projekta

```text
mini_projekat_Andrija_Gojkovic/
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

Datoteka `__init__.py` služi za označavanje Python paketa i zato ne zahtijeva dodatnu implementaciju.

## 3. Primjena SOLID principa

U projektu su primijenjena dva SOLID principa: Single Responsibility Principle (S) i Dependency Inversion Principle (D).

### 3.1. S – Single Responsibility Principle

Princip jedne odgovornosti podrazumijeva da svaka klasa ili modul treba da ima jednu jasno definisanu odgovornost.

U monolitnoj verziji sve funkcionalnosti bile su objedinjene u jednoj skripti.

Nakon refaktoringa odgovornosti su podijeljene na sljedeći način:

- `CsvReservationSource` – učitavanje podataka iz CSV datoteke.
- `parse_reservation` – validacija i pretvaranje ulaznih podataka u model rezervacije.
- `ReservationService` – obrada rezervacija i obračun ukupnog prihoda.
- `ConsoleReservationReporter` – prikaz rezultata u konzoli.

Ovakva podjela omogućava da se pojedini djelovi programa mijenjaju nezavisno.

Na primjer, promjena načina učitavanja podataka ne zahtijeva promjenu poslovne logike. Takođe, promjena formata izvještaja ne utiče na obračun rezervacija.

### 3.2. D – Dependency Inversion Principle

Princip inverzije zavisnosti podrazumijeva da poslovna logika treba da zavisi od apstrakcija, a ne od konkretnih implementacija.

U projektu su pomoću `typing.Protocol` definisana dva interfejsa:

- `ReservationSource` – definiše način dobijanja podataka o rezervacijama.
- `ReservationReporter` – definiše način prikazivanja rezultata obrade.

Klasa `ReservationService` u konstruktoru prima ove interfejse, umjesto da direktno zavisi od klasa `CsvReservationSource` i `ConsoleReservationReporter`.

Konkretne implementacije povezuju se u datoteci `main.py`.

Na ovaj način servis može koristiti različite izvore podataka i različite načine izvještavanja bez izmjene svoje osnovne logike.

Dodatna prednost je jednostavnije testiranje, jer se stvarne implementacije mogu zamijeniti klasama `FakeSource` i `FakeReporter`.

### 3.3. Uloga Protocol interfejsa

`Protocol` omogućava definisanje metoda koje neka klasa treba da podržava, bez obaveznog nasljeđivanja od bazne klase.

U ovom projektu omogućava odvajanje poslovne logike od načina učitavanja podataka i prikazivanja rezultata.

To je posebno korisno prilikom testiranja, jer se mogu koristiti zamjenski objekti koji ispunjavaju odgovarajući interfejs.

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

Pokretanje refaktorisane verzije:

```powershell
python main.py
```

Obje verzije za primjer podataka iz `reservations.csv` prikazuju:

```text
Validne: 3, Nevalidne: 1, Prihod: 780.00 EUR
```

Dobijeni rezultati pokazuju da refaktoring nije promijenio ponašanje programa za korišćeni primjer ulaznih podataka.

## 5. Testiranje

Za automatsko testiranje korišćen je `pytest`.

Testovi se pokreću komandom:

```powershell
python -m pytest -v
```

Implementirano je ukupno devet testova koji obuhvataju:

- Obračun ukupne cijene validne rezervacije.
- Odbijanje rezervacija sa neispravnim brojem noćenja.
- Obradu kombinacije validnih i nevalidnih podataka.
- Obradu praznog izvora podataka.
- Uklanjanje nepotrebnih razmaka iz ulaznih vrijednosti.
- Odbijanje negativnih cijena.
- Odbijanje nekonačnih vrijednosti `nan` i `inf`.
- Integraciju CSV izvora sa servisom.

U testovima servisa koriste se zamjenske implementacije `FakeSource` i `FakeReporter`.

Na taj način poslovna logika može da se testira nezavisno od stvarne CSV datoteke i konzolnog ispisa.

### 5.1. Rezultati testiranja

Nakon pokretanja testova u VS Code-u dobijen je rezultat:

```text
9 passed in 0.10s
```

Svih devet testova uspješno je prošlo.

Pored automatskog testiranja, pokrenute su i monolitna i refaktorisana verzija programa. Obje su dale isti rezultat:

```text
Validne: 3, Nevalidne: 1, Prihod: 780.00 EUR
```

Time je provjereno da refaktorisana verzija zadržava funkcionalnost početne verzije na testiranom primjeru.

## 6. Korišćenje AI alata

Tokom izrade projekta koristio sam ChatGPT kao pomoć pri generisanju početnog koda, refaktoringu, organizaciji projekta, pisanju testova i pripremi dokumentacije.

AI alat koristio sam i za objašnjenje pojedinih djelova implementacije i rješavanje problema prilikom pokretanja programa.

### 6.1. Korišćeni upiti

U nastavku su navedeni neki od stvarnih zahtjeva koje sam koristio tokom rada.

**Upit 1 – Izrada projekta**

Dostavio sam fotografiju zadatka „Mini projekat 1: refaktoring obrade rezervacija“ sa zahtjevima profesora i potvrdio izradu projekta odgovorom:

> Da

Na osnovu zadatka generisane su početna monolitna i refaktorisana verzija programa za obradu hotelskih rezervacija.

**Upit 2 – Pokretanje programa**

> kako pokrecem ovo

Tražio sam objašnjenje kako da instaliram potrebne biblioteke, pokrenem program i izvršim pytest testove u VS Code-u.

**Upit 3 – Poboljšanje projekta**

> hajde poneki fahjlovi su odje prazni hajde mi napravi dobro verziju za predaju i da sve bude kao sto profesor trazi

Nakon pregleda početne verzije zatražio sam dopunu projekta, poboljšanje strukture koda i proširenje automatskih testova.

**Upit 4 – Objašnjenje Python paketa**

> zastoo je ovaj prazan

Tražio sam objašnjenje zašto datoteka `__init__.py` sadrži veoma malo koda i koja je njena uloga.

**Upit 5 – Priprema dokumentacije**

> hajde odradio dokumenotvanje

Tražio sam pomoć pri pisanju README dokumentacije, posebno dijela koji se odnosi na korišćenje AI alata, upotrijebljene upite i ispravke generisanog koda.

### 6.2. Izmjene i ispravke generisanog koda

Nakon generisanja prve verzije zatražio sam dodatna poboljšanja kako bi projekat bio bolje organizovan i usklađen sa zahtjevima zadatka.

Uz pomoć AI alata izvršene su sljedeće dorade:

1. **Razdvajanje odgovornosti** – validacija je izdvojena u modul `validator.py`, dok su učitavanje podataka, obrada i izvještavanje organizovani u posebne module.

2. **Primjena Dependency Inversion principa** – korišćeni su `Protocol` interfejsi kako poslovna logika ne bi direktno zavisila od konkretnih implementacija.

3. **Dodavanje zamjenskih implementacija** – u testovima su korišćene klase `FakeSource` i `FakeReporter`, čime je omogućeno nezavisno testiranje servisa.

4. **Poboljšanje validacije** – dodate su provjere neispravnih cijena, uključujući negativne i nekonačne vrijednosti.

5. **Proširenje testova** – dodati su testovi za granične slučajeve, neispravne podatke i integraciju sa CSV izvorom.

6. **Poboljšanje učitavanja datoteka** – putanja do CSV datoteke određuje se relativno u odnosu na lokaciju skripte, kako bi program mogao pravilno da pronađe podatke.

Ove izmjene nastale su uz pomoć AI alata i predstavljaju doradu prvobitno generisanog rješenja.

### 6.3. Provjera generisanog koda

Nakon dobijanja dopunjene verzije samostalno sam pokrenuo projekat u Visual Studio Code-u.

Prilikom prvog pokretanja pojavio se problem jer Windows terminal nije prepoznavao komandu `python`.

Uz pomoć AI objašnjenja napravio sam i koristio virtuelno Python okruženje `.venv`, nakon čega je program uspješno pokrenut.

Zatim sam izvršio sljedeće provjere:

- Pokrenuo sam monolitnu verziju `monolith.py`.
- Pokrenuo sam refaktorisanu verziju `main.py`.
- Uporedio sam rezultate obje verzije.
- Pokrenuo sam svih devet pytest testova.
- Provjerio sam da se projekat izvršava bez prijavljenih grešaka u testiranim slučajevima.

Obje verzije prikazale su isti rezultat, a svih devet automatskih testova je prošlo.

Na osnovu ovih provjera zaključio sam da program ispravno funkcioniše za testirane slučajeve i da je refaktorisana verzija zadržala ponašanje početne verzije na korišćenom primjeru.

### 6.4. Zaključak o korišćenju AI-ja

AI alat je korišćen kao pomoć u procesu razvoja i refaktoringa programa, ali i kao sredstvo za objašnjenje implementacije i otklanjanje problema pri pokretanju.

Generisani kod je provjeren pokretanjem obje verzije aplikacije i izvršavanjem automatskih testova.

Ovaj proces pokazuje da AI može značajno pomoći u razvoju softvera, ali da je potrebno razumjeti generisano rješenje, provjeriti njegovo ponašanje i testirati funkcionalnosti prije predaje.

## 7. Ograničenja projekta

Projekat predstavlja jednostavan nastavni primjer obrade hotelskih rezervacija.

Podaci se učitavaju iz CSV datoteke, bez korišćenja baze podataka ili grafičkog korisničkog interfejsa.

Za obračun cijena koristi se tip `float`. U složenijim finansijskim aplikacijama prikladnije bi bilo koristiti `Decimal` radi preciznijeg rukovanja novčanim vrijednostima.

## 8. Zaključak

Kroz ovaj projekat prikazan je postupak refaktoringa monolitne Python skripte u modularno organizovanu aplikaciju.

Primjenom S principa razdvojene su odgovornosti pojedinačnih komponenti, dok je primjenom D principa smanjena zavisnost poslovne logike od konkretnih implementacija.

Korišćenje `Protocol` interfejsa omogućilo je jednostavniju zamjenu izvora podataka i reportera, što je posebno korisno prilikom automatskog testiranja.

Refaktorisana verzija zadržala je ponašanje početnog programa u provjerenim slučajevima, a svih devet pytest testova uspješno je prošlo.

Projekat pokazuje značaj čitljivog, modularnog i testabilnog koda, kao i važnost provjere AI-generisanih rješenja.

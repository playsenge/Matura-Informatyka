import datetime


def formatuj_date(x) -> datetime.date:
    [year, month, day] = [int(y) for y in x.strip().split('-')]
    return datetime.date(year=year, month=month, day=day)


zadanko = 1


def nastepne():
    global zadanko
    if zadanko > 1:
        print()
    print('=' * 5, f"Zadanie 6.{zadanko}.", '=' * 5)
    zadanko += 1


samochody = {}
ceny_za_dobe = {}
klienci = {}
wypozyczenia = {}

with open('DANE/samochody.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split(';')
        line[0] = int(line[0])
        samochody[line[0]] = line[1:]

with open('DANE/ceny_za_dobe.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split(';')
        ceny_za_dobe[line[0]] = int(line[1])

with open('DANE/klienci.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split(';')
        klienci[int(line[0])] = line[1:]

with open('DANE/wypozyczenia.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split(';')
        line[0] = int(line[0])
        line[1] = int(line[1])
        line[2] = formatuj_date(line[2])
        line[3] = formatuj_date(line[3])
        if line[0] not in wypozyczenia.keys():
            wypozyczenia[line[0]] = []
        wypozyczenia[line[0]].append(line[1:])

_6_1 = []

for nr_ew, x in wypozyczenia.items():
    for [nr_klienta, wypozyczenie, zwrot] in x:
        rejestracja = samochody[nr_ew][2]
        [imie, nazwisko] = klienci[nr_klienta]
        doby = (zwrot - wypozyczenie).days
        naleznosc = doby * ceny_za_dobe[samochody[nr_ew][0][0]]
        _6_1.append([imie, nazwisko, rejestracja, doby, naleznosc])

_6_1 = sorted(_6_1, key=lambda x: (x[1], x[0], x[2]))

nastepne()
print(*_6_1[0])
print(*_6_1[-1])

_6_2 = {}
for nr_ew, x in wypozyczenia.items():
    for [nr_klienta, wypozyczenie, zwrot] in x:
        klasa = samochody[nr_ew][0][0]

        if klasa not in _6_2.keys():
            _6_2[klasa] = 0

        _6_2[klasa] += 1

nastepne()
for x, y in _6_2.items():
    print(x, y)

_6_3 = {}
for nr_ew, x in wypozyczenia.items():
    for [nr_klienta, wypozyczenie, zwrot] in x:
        if nr_klienta not in _6_3.keys():
            _6_3[nr_klienta] = 0

        _6_3[nr_klienta] += 1

nastepne()
_6_3 = sorted(_6_3.items(), key=lambda x: x[1], reverse=True)
print(*klienci[_6_3[0][0]], _6_3[0][1])

_6_4_wypozyczone = list(set(wypozyczenia.keys()))
_6_4_niewypozyczone = []
for nr_ew, [nr_firmowy, miejscowosc, nr_rej] in samochody.items():
    if nr_ew not in _6_4_wypozyczone:
        _6_4_niewypozyczone.append(nr_ew)

_6_4 = {}
for nr_ew in _6_4_niewypozyczone:
    klasa = samochody[nr_ew][0][0]
    miasto = samochody[nr_ew][1]
    if miasto not in _6_4.keys():
        _6_4[miasto] = {}
    if klasa not in _6_4[miasto].keys():
        _6_4[miasto][klasa] = 0

    _6_4[miasto][klasa] += 1

nastepne()
for x, y in _6_4.items():
    print(x, end=': ')
    items = []
    for a, b in y.items():
        items.append(f"{a} {b}")
    print(', '.join(items))

nastepne()
_6_5 = 0
for nr_klienta, [imie, nazwisko] in klienci.items():
    wypozyczono = False
    for nr_ew, x in wypozyczenia.items():
        for [nr_klienta_2, wypozyczenie, zwrot] in x:
            if nr_klienta_2 == nr_klienta:
                wypozyczono = True
                break

    if not wypozyczono:
        _6_5 += 1
print(_6_5)
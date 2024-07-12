from collections import defaultdict
import datetime

samochody = {}
ceny_za_dobe = {}
klienci = {}
wypozyczenia = defaultdict(list)


def data_format(x: str) -> datetime.date:
    [year, month, day] = [int(y) for y in x.strip().split('-')]
    return datetime.date(year=year, month=month, day=day)


with open('DANE/samochody.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split(';')
        samochody[int(line[0])] = [line[1], line[2], line[3]]

with open('DANE/ceny_za_dobe.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split(';')
        ceny_za_dobe[line[0]] = int(line[1])

with open('DANE/klienci.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split(';')
        klienci[int(line[0])] = [line[1], line[2]]

with open('DANE/wypozyczenia.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split(';')
        wypozyczenia[int(line[0])].append([int(line[1]), data_format(line[2]), data_format(line[3])])

_6_1 = []
for nr_ew, lista in wypozyczenia.items():
    for [nr_klienta, wypozyczenie, zwrot] in lista:
        [imie, nazwisko] = klienci[nr_klienta]
        nr_rej = samochody[nr_ew][2]
        czas = (zwrot - wypozyczenie).days
        naleznosc = ceny_za_dobe[samochody[nr_ew][0][0]] * czas

        _6_1.append([imie, nazwisko, nr_rej, czas, naleznosc])

print('Zadanie 6.1.')
_6_1 = sorted(_6_1, key=lambda x: (x[1], x[0], x[2]))
print(*_6_1[0])
print(*_6_1[-1])

print('\nZadanie 6.2.')
_6_2 = defaultdict(int)
_6_3 = defaultdict(int)
for nr_ew, lista in wypozyczenia.items():
    for [nr_klienta, wypozyczenie, zwrot] in lista:
        _6_2[samochody[nr_ew][0][0]] += 1
        _6_3[nr_klienta] += 1

for x, y in _6_2.items():
    print(x, y)

print('\nZadanie 6.3.')
_6_3_max = max(_6_3.values())
for x, y in _6_3.items():
    if y == _6_3_max:
        print(*klienci[x], y)


def _6_4_init():
    return defaultdict(int)


_6_4 = defaultdict(_6_4_init)

for nr_ew, [nr_firmowy, miejscowosc, nr_rej] in samochody.items():
    if nr_ew not in wypozyczenia.keys():
        _6_4[nr_firmowy[0]][miejscowosc] += 1

print('\nZadanie 6.4.')
for x, y in _6_4.items():
    print(f'Klasa {x}: ', end='')
    u = []
    for z in list(y.items()):
        u.append(' '.join([str(x) for x in z]))
    print(', '.join(u))

print('\nZadanie 6.5.')
_6_5 = defaultdict(int)
for nr_ew, lista in wypozyczenia.items():
    for [nr_klienta, wypozyczenie, zwrot] in lista:
        _6_5[nr_klienta] += 1
print(len(klienci) - len(_6_5.values()))
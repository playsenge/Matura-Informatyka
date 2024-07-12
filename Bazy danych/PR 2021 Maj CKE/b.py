import datetime
from collections import defaultdict

gracze = {}
klasy = {}
jednostki = {}


def datetime_format(x: str) -> datetime.date:
    [year, month, day] = [int(y) for y in x.strip().split('-')]
    return datetime.date(year=year, month=month, day=day)


with open('DANE/gracze.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split('\t')
        gracze[int(line[0])] = [line[1], datetime_format(line[2])]

with open('DANE/klasy.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split('\t')
        klasy[line[0]] = [int(line[1]), int(line[2]), int(line[3]), int(line[4])]

with open('DANE/jednostki.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split('\t')
        jednostki[int(line[0])] = [int(line[1]), line[2], int(line[3]), int(line[4])]

_6_1 = defaultdict(int)
for id_gracza, [kraj, data_dolaczenia] in gracze.items():
    if data_dolaczenia.year == 2018:
        _6_1[kraj] += 1

_6_1 = sorted(_6_1.items(), key=lambda x: x[1], reverse=True)[:5]
for x in _6_1:
    print(*x)

print('=' * 10)

_6_2 = defaultdict(int)
for id_jednostki, [id_gracza, nazwa, lok_x, lok_y] in jednostki.items():
    if 'elf' in nazwa:
        _6_2[nazwa] += klasy[nazwa][1]
for x, y in _6_2.items():
    print(x, y)

print('=' * 10)

_6_3 = []
for id_gracza in gracze.keys():
    ma_artylerzyste = False

    for id_jednostki, [id_gracza_2, nazwa, lok_x, lok_y] in jednostki.items():
        if id_gracza_2 == id_gracza and nazwa == 'artylerzysta':
            ma_artylerzyste = True
            break

    if not ma_artylerzyste:
        print(id_gracza)

_6_4 = defaultdict(int)
for id_jednostki, [id_gracza, nazwa, lok_x, lok_y] in jednostki.items():
    szybkosc = klasy[nazwa][3]
    if abs(lok_x - 100) + abs(lok_y - 100) <= szybkosc:
        _6_4[nazwa] += 1

print('=' * 10)

_6_4 = sorted(_6_4.items(), key=lambda x: x[1], reverse=True)
for x in _6_4:
    print(*x)

print('=' * 10)

bitwy = 0
polacy = 0

sprawdzone_lokalizacje = []
for id_jednostki, [id_gracza, nazwa, lok_x, lok_y] in jednostki.items():
    lok = (lok_x, lok_y)
    if lok in sprawdzone_lokalizacje:
        continue

    sprawdzone_lokalizacje.append(lok)

    panstwa = [gracze[id_gracza][0]]
    ile_jednostek = 1
    for id_jednostki_2, [id_gracza_2, nazwa_2, lok_x_2, lok_y_2] in jednostki.items():
        if id_jednostki_2 != id_jednostki and id_gracza_2 != id_gracza and lok_x == lok_x_2 and lok_y == lok_y_2:
            ile_jednostek += 1
            panstwa.append(gracze[id_gracza_2][0])

    if ile_jednostek > 1:
        bitwy += 1
        if panstwa.count('Polska') > 0:
            polacy += 1

print(bitwy)
print(polacy)

import datetime

gracze = {}
klasy = {}
jednostki = {}

def data_formatuj(x):
    [year, month, day] = [int(y) for y in x.strip().split('-')]
    return datetime.date(year=year, month=month, day=day)

with open('DANE/gracze.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split('\t')
        line[0] = int(line[0])
        line[2] = data_formatuj(line[2])

        gracze[line[0]] = [line[1], line[2]]

with open('DANE/klasy.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split('\t')
        line[1], line[2], line[3], line[4] = int(line[1]), int(line[2]), int(line[3]), int(line[4])

        klasy[line[0]] = [line[1], line[2], line[3], line[4]]

with open('DANE/jednostki.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split('\t')
        line[0], line[1], line[3], line[4] = int(line[0]), int(line[1]), int(line[3]), int(line[4])

        jednostki[line[0]] = [line[1], line[2], line[3], line[4]]

##########################################

_6_1 = {}

for id_gracza, [kraj, data_dolaczenia] in gracze.items():
    if data_dolaczenia.year == 2018:
        if kraj not in _6_1.keys():
            _6_1[kraj] = 0
        _6_1[kraj] += 1

_6_1 = sorted(_6_1.items(), key=lambda x: x[1], reverse=True)

for x in _6_1[:5]:
    print(*x, sep='\t')

_6_2 = {}
for id_jednostki, [id_gracza, nazwa, lok_x, lok_y] in jednostki.items():
    if 'elf' in nazwa:
        if nazwa not in _6_2.keys():
            _6_2[nazwa] = 0
        _6_2[nazwa] += klasy[nazwa][1]

print('#' * 50)
for x, y in _6_2.items():
    print(x, y, sep='\t')

_6_3 = []
for id_gracza, [kraj, data_dolaczenia] in gracze.items():
    ma_artylerzyste = False

    for id_jednostki, [id_gracza_2, nazwa, lok_x, lok_y] in jednostki.items():
        if id_gracza == id_gracza_2 and nazwa == 'artylerzysta':
            ma_artylerzyste = True
            break

    if not ma_artylerzyste:
        _6_3.append(id_gracza)

print('#' * 50)
_6_3.sort()
print(*_6_3, sep='\n')

_6_4 = {}
for id_jednostki, [id_gracza, nazwa, lok_x, lok_y] in jednostki.items():
    szybkosc = klasy[nazwa][3]
    if abs(lok_x - 100) + abs(lok_y - 100) <= szybkosc:
        if nazwa not in _6_4.keys():
            _6_4[nazwa] = 0
        _6_4[nazwa] += 1

print('#' * 50)
_6_4 = sorted(_6_4.items(), key=lambda x: x[1], reverse=True)
for x in _6_4:
    print(*x, sep='\t')

przeskanowane_pola = set()
_6_5_bitwy = 0
_6_5_polacy = 0
for id_jednostki, [id_gracza, nazwa, lok_x, lok_y] in jednostki.items():
    if (lok_x, lok_y) in przeskanowane_pola:
        continue

    pole = [[id_jednostki, id_gracza, nazwa, lok_x, lok_y]]
    for id_jednostki_2, [id_gracza_2, nazwa_2, lok_x_2, lok_y_2] in jednostki.items():
        if id_jednostki != id_jednostki_2 and id_gracza != id_gracza_2 and lok_x == lok_x_2 and lok_y == lok_y_2:
            pole.append([id_jednostki_2, id_gracza_2, nazwa_2, lok_x_2, lok_y_2])

    if len(pole) > 1:
        _6_5_bitwy += 1
        panstwa = []
        for x in pole:
            panstwa.append( gracze[x[1]] [0] )
        if panstwa.count('Polska') > 0:
            _6_5_polacy += 1

    przeskanowane_pola.add((lok_x, lok_y))

print('#' * 50)
print(_6_5_bitwy)
print(_6_5_polacy)
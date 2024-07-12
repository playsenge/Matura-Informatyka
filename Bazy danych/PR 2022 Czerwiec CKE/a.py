import datetime
from collections import defaultdict

kluby = {}
sedziowie = {}
mecze = {}


def data_gen(x):
    x = [int(y) for y in x.strip().split('-')]
    return datetime.date(*x)


with open('DANE/kluby.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split(';')
        kluby[int(line[0])] = line[1:]

with open('DANE/sedziowie.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split(';')
        sedziowie[int(line[0])] = line[1:]

with open('DANE/mecze.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split(';')
        mecze[int(line[0])] = [data_gen(line[1]), int(line[2]), int(line[3]), int(line[4]), int(line[5])]

_6_1 = 0
for id_meczu, [data, id_klubu, sety_wygrane, sety_przegrane, id_sedziego] in mecze.items():
    if sety_wygrane + sety_przegrane == 5:
        _6_1 += 1

print('Zadanie 6.1.')
print(_6_1)

_6_2 = {}
for id_meczu, [data, id_klubu, sety_wygrane, sety_przegrane, id_sedziego] in mecze.items():
    miasto = ''
    for id_klubu_2, [nazwa_2, miasto_2] in kluby.items():
        if id_klubu == id_klubu_2:
            miasto = miasto_2
            break

    if miasto not in _6_2.keys():
        _6_2[miasto] = 0

    _6_2[miasto] += 1

print()
print('Zadanie 6.2.')
_6_2 = sorted(_6_2.items(), key=lambda x: x[1], reverse=True)
for x in _6_2:
    print(*x)

_6_3 = {}
for id_sedziego, [imie, nazwisko] in sedziowie.items():
    ich_mecze = 0
    for id_meczu, [data, id_klubu, sety_wygrane, sety_przegrane, id_sedziego_2] in mecze.items():
        if id_sedziego_2 == id_sedziego:
            ich_mecze += 1

    _6_3[id_sedziego] = ich_mecze

print()
print('Zadanie 6.3.')
_6_3_srednia = sum(_6_3.values()) / len(_6_3.values())
for id_sedziego, [imie, nazwisko] in sedziowie.items():
    if _6_3[id_sedziego] > _6_3_srednia:
        print(imie, nazwisko)

_6_4 = []
for id_sedziego, [imie, nazwisko] in sedziowie.items():
    poprowadzono = False

    for id_meczu, [data, id_klubu, sety_wygrane, sety_przegrane, id_sedziego_2] in mecze.items():
        if id_sedziego_2 == id_sedziego:
            for id_klubu_2, [nazwa_2, miasto_2] in kluby.items():
                if id_klubu_2 == id_klubu:
                    if miasto_2 in ['Licowo', 'Szymbark'] and data >= data_gen('2019-10-15') and data <= data_gen(
                            '2019-12-15'):
                        poprowadzono = True
                        break

    if not poprowadzono:
        _6_4.append([imie, nazwisko])

print()
print('Zadanie 6.4.')
for x in _6_4:
    print(*x)

_6_5_przegrane = defaultdict(int)
_6_5_wygrane = defaultdict(int)
for id_meczu, [data, id_klubu, sety_wygrane, sety_przegrane, id_sedziego_2] in mecze.items():
    if sety_wygrane > sety_przegrane:
        _6_5_wygrane[id_klubu] += 1
    else:
        _6_5_przegrane[id_klubu] += 1

print()
print('Zadanie 6.5.')
for id_klubu, [nazwa, miasto] in kluby.items():
    if _6_5_wygrane[id_klubu] >= _6_5_przegrane[id_klubu]:
        print(nazwa, miasto, _6_5_wygrane[id_klubu], _6_5_przegrane[id_klubu])

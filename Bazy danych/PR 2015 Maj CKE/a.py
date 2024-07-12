from collections import defaultdict

kierowcy = defaultdict(list)
wyscigi = defaultdict(list)
wyniki = defaultdict(list)

with open('DANE/Kierowcy.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split(';')
        kierowcy[line[0]] = line[1:]

with open('DANE/Wyscigi.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split(';')
        line[1] = int(line[1])
        wyscigi[line[0]] = line[1:]

with open('DANE/Wyniki.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split(';')
        line[1] = float(line[1].replace(',', '.'))
        wyniki[line[0]].append(line[1:])

id_robert_kubica = ''
for id_kierowcy, [nazwisko, imie, kraj] in kierowcy.items():
    if imie == 'Robert' and nazwisko == 'Kubica':
        id_robert_kubica = id_kierowcy
        break

_6_1 = []
for id_wyscigu, [rok, grandprix] in wyscigi.items():
    x_punkty = 0
    for id_kierowcy, wyscigix in wyniki.items():
        if id_kierowcy == id_robert_kubica:
            for [punkty, id_wyscigu_2] in wyscigix:
                if id_wyscigu_2 == id_wyscigu:
                    x_punkty += punkty
    if x_punkty > 0:
        _6_1.append([grandprix, rok, x_punkty])

print('Zadanie 6.1.')
_6_1 = sorted(_6_1, key=lambda x: x[2], reverse=True)
print(*_6_1[0][:2])

_6_2 = defaultdict(int)
for id_wyscigu, [rok, grandprix] in wyscigi.items():
    _6_2[grandprix] += 1

print()
print('Zadanie 6.2.')
_6_2 = sorted(_6_2.items(), key=lambda x: x[1])[0]
print(_6_2[0])

print()
print('Zadanie 6.3.')
_6_3 = defaultdict(list[tuple])
for id_kierowcy, [nazwisko, imie, kraj] in kierowcy.items():
    for rok_szukany in [2000, 2006, 2012]:
        wynik_ogolny = 0
        for id_kierowcy_2, wyscigix in wyniki.items():
            for [punkty, id_wyscigu_2] in wyscigix:
                if wyscigi[id_wyscigu_2][0] == rok_szukany and id_kierowcy == id_kierowcy_2:
                    wynik_ogolny += punkty
        _6_3[rok_szukany].append((id_kierowcy, wynik_ogolny))

for rok in _6_3.keys():
    element = sorted(_6_3[rok], key=lambda x: x[1], reverse=True)[0]
    print(rok, *kierowcy[element[0]][:2], element[1])

print()
print('Zadanie 6.4.')
_6_4 = defaultdict(set[str])
for id_kierowcy_2, wyscigix in wyniki.items():
    for [punkty, id_wyscigu_2] in wyscigix:
        if wyscigi[id_wyscigu_2][0] == 2012:
            _6_4[kierowcy[id_kierowcy_2][2]].add(id_kierowcy_2)
for kraj in _6_4.keys():
    print(kraj, len(_6_4[kraj]))
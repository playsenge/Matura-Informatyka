from collections import defaultdict

uczestnicy = {}
grupy = {}
przynaleznosc = defaultdict(list[str])

with open('DANE/uczestnicy.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split('\t')
        uczestnicy[line[0]] = line[1:]

with open('DANE/grupy.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split('\t')
        grupy[line[0]] = line[1]

with open('DANE/przynaleznosc.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split('\t')
        przynaleznosc[line[0]].append(line[1])

print('Zadanie 5.1.')
for grupa, nazwa in grupy.items():
    if nazwa[0].lower() == 'f':
        print(grupa, nazwa)

print()
print('Zadanie 5.2.')
_5_2 = 0
for id_czlonka, [imie, nazwisko] in uczestnicy.items():
    if imie[-1] == 'a':
        _5_2 += 1
print(_5_2)

print()
print('Zadanie 5.3.')
zdrowe_odzywianie = 'f15'
_5_3 = []
for id_czlonka, [imie, nazwisko] in uczestnicy.items():
    if zdrowe_odzywianie in przynaleznosc[id_czlonka]:
        _5_3.append([imie, nazwisko])
_5_3 = sorted(_5_3, key=lambda x: (x[0], x[1]))
for x in _5_3:
    print(*x)

print()
print('Zadanie 5.4.')
_5_4 = []
for id_czlonka, [imie, nazwisko] in uczestnicy.items():
    if len(przynaleznosc[id_czlonka]) == 10:
        _5_4.append([imie, nazwisko])
_5_4 = sorted(_5_4, key=lambda x: x[1])
for x in _5_4:
    print(*x)

print()
print('Zadanie 5.5.')
_5_5 = {}
for grupa, nazwa in grupy.items():
    czlonkowie = 0
    for id_czlonka, [imie, nazwisko] in uczestnicy.items():
        if grupa in przynaleznosc[id_czlonka]:
            czlonkowie += 1
    _5_5[nazwa] = czlonkowie
_5_5 = sorted(_5_5.items(), key=lambda x: x[1], reverse=True)[0]
print(*_5_5)
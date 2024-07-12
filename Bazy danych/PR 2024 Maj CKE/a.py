import datetime

kierowcy = {}
taryfikator = {}
rejestr = {}

with open('DANE/kierowcy.txt') as f:
    for x in f.readlines()[1:]:
        tablica = x.strip().split(';')
        kierowcy[tablica[0]] = tablica[1:]

with open('DANE/taryfikator.txt') as f:
    for x in f.readlines()[1:]:
        tablica = x.strip().split(';')
        taryfikator[tablica[0]] = [tablica[1], int(tablica[2]), int(tablica[3])]

with open('DANE/rejestr.txt') as f:
    for x in f.readlines()[1:]:
        tablica = x.strip().split(';')
        data = [int(x) for x in tablica[1].split('-')]
        rejestr[tablica[0]] = [datetime.date(data[0], data[1], data[2]), tablica[2], tablica[3]]

kwoty = {}

for zdarzenie, [data, id_osoby, id_wykroczenia] in rejestr.items():
    if id_osoby not in kwoty.keys():
        kwoty[id_osoby] = 0

    kwoty[id_osoby] += taryfikator[id_wykroczenia][2]

_8_1 = sorted(kwoty.items(), key=lambda x: x[1], reverse=True)[0]
print(kierowcy[_8_1[0]][0], kierowcy[_8_1[0]][1], _8_1[1])

_8_2 = {}

for zdarzenie, [data, id_osoby, id_wykroczenia] in rejestr.items():
    miesiac = data.month
    if miesiac not in _8_2.keys():
        _8_2[miesiac] = 0

    if int(id_wykroczenia) >= 3 and int(id_wykroczenia) <= 6:
        _8_2[miesiac] += taryfikator[id_wykroczenia][1]

print(*sorted(_8_2.items(), key=lambda x: x[1])[0])

_8_3 = []

for zdarzenie, [data, id_osoby, id_wykroczenia] in rejestr.items():
    rejestracja = kierowcy[id_osoby][2]
    if rejestracja not in _8_3:
        _8_3.append(rejestracja)

_8_3_bez = []

for id, [imie, nazwisko, rejestracja] in kierowcy.items():
    if rejestracja not in _8_3:
        _8_3_bez.append([imie, nazwisko, rejestracja])

_8_3_bez = sorted(_8_3_bez, key=lambda x: x[2])

for x in _8_3_bez:
    print(*x)

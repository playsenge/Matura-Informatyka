import datetime

kraje = {}
urzadzenia = {}
instalacje = []


def data(x):
    x = [int(y) for y in x.strip().split('.')]
    return datetime.date(x[2], x[1], x[0])


with open('DANE/kraje.txt') as f:
    for line in f.readlines()[1:]:
        tablica = line.strip().split('\t')
        kraje[tablica[0]] = [tablica[1], int(tablica[2])]

with open('DANE/urzadzenia.txt') as f:
    for line in f.readlines()[1:]:
        tablica = line.strip().split('\t')
        urzadzenia[int(tablica[0])] = tablica[1:]

with open('DANE/instalacje.txt') as f:
    for line in f.readlines()[1:]:
        tablica = line.strip().split('\t')
        instalacje.append([data(tablica[0]), tablica[1], int(tablica[2])])

_7_1 = {'Tablet': 0, 'Phone': 0, 'PC': 0}
for instalacja in instalacje:
    [data_i, kod_k, kod_u] = instalacja
    typ_u = ''

    for kod_u_2, [nazwa_u, producent_u, typ_u_2] in urzadzenia.items():
        if kod_u_2 == kod_u:
            typ_u = typ_u_2
            break

    _7_1[typ_u] += 1

print('Zadanie 7.1.')
for x, y in _7_1.items():
    print(x, y)

_7_2 = {}
for instalacja in instalacje:
    [data_i, kod_k, kod_u] = instalacja

    if data_i.month == 2 and data_i.year == 2019:
        nazwa_u, producent_u, typ_u = '', '', ''

        for kod_u_2, [nazwa_u_2, producent_u_2, typ_u_2] in urzadzenia.items():
            if kod_u == kod_u_2:
                nazwa_u, producent_u, typ_u = nazwa_u_2, producent_u_2, typ_u_2
                break

        if producent_u not in _7_2.keys():
            _7_2[producent_u] = 0
        _7_2[producent_u] += 1

print()
print('Zadanie 7.2.')
_7_2 = sorted(_7_2.items(), key=lambda x: x[1], reverse=True)
print(*_7_2[0])

_7_3 = {}
for kod_k, [nazwa_k, ludnosc_k] in kraje.items():
    if nazwa_k not in _7_3:
        _7_3[nazwa_k] = 0

    for instalacja in instalacje:
        [data_i, kod_k_2, kod_u] = instalacja
        if kod_k_2 == kod_k:
            _7_3[nazwa_k] += 1

_7_3b = {}
for x, y in _7_3.items():
    pop = 0
    for kod_k, [nazwa_k, ludnosc_k] in kraje.items():
        if nazwa_k == x:
            pop = ludnosc_k
            break

    if pop >= 1000000:
        _7_3b[x] = y / pop * 1000000

print()
print('Zadanie 7.3.')
_7_3b = sorted(_7_3b.items(), key=lambda x: x[1], reverse=True)
for i in range(5):
    print(_7_3b[i][0], str(round(_7_3b[i][1], 2)).replace('.', ','))

_7_4 = {}
for kod_u, [nazwa_u, producent_u, typ_u] in urzadzenia.items():
    if typ_u == 'Tablet':
        panstwa = []
        for instalacja in instalacje:
            [data_i, kod_k_2, kod_u_2] = instalacja
            if kod_u_2 == kod_u:
                if kod_k_2 not in panstwa:
                    panstwa.append(kod_k_2)
        _7_4[kod_u] = [nazwa_u, len(panstwa)]

print()
print('Zadanie 7.4.')
_7_4 = sorted(_7_4.items(), key=lambda x: x[1][1], reverse=True)
print(_7_4[0][0], *_7_4[0][1])

"""
SELECT firmy.nazwa, Count(*)
FROM firmy INNER JOIN instalacje ON firmy.id_firmy = instalacje.id_firmy
GROUP BY firmy.nazwa
ORDER BY Count(*) DESC;
"""

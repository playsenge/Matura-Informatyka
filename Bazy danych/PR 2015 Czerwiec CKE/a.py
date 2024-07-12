import datetime
from collections import defaultdict

wykroczenia = defaultdict(list)
mandaty = defaultdict(list)
kierowcy = defaultdict(list)


def formatuj_date(x) -> datetime.date:
    [year, month, day] = [int(y) for y in x.strip().split('-')]
    return datetime.date(year=year, month=month, day=day)


with open('DANE/wykroczenia.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split('\t')
        line[0] = int(line[0])
        line[2] = int(line[2])
        line[3] = int(line[3])
        wykroczenia[line[0]] = line[1:]

with open('DANE/mandaty.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split('\t')
        mandaty[line[0]].append([formatuj_date(line[1]), int(line[2])])

with open('DANE/kierowcy.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split('\t')
        kierowcy[line[0]] = [formatuj_date(line[1]), line[2]]

_5_1 = defaultdict(int)
for pesel, lista_wykroczen in mandaty.items():
    for data_wyk, kod_wyk in lista_wykroczen:
        _5_1[kod_wyk] += 1

print('Zadanie 5.1.')
_5_1 = sorted(_5_1.items(), key=lambda x: x[1], reverse=True)[0]
print(wykroczenia[_5_1[0]][0], _5_1[1])

print('\nZadanie 5.2.')
for pesel, [data_prawa_jazdy, miasto] in kierowcy.items():
    if data_prawa_jazdy.year == 2013:
        punkty_karne = 0
        for pesel_2, lista_wykroczen in mandaty.items():
            if pesel_2 == pesel:
                for data_wyk, kod_wyk in lista_wykroczen:
                    punkty_karne += wykroczenia[kod_wyk][2]

        if punkty_karne > 20:
            print(pesel, punkty_karne)

print('\nZadanie 5.3.')
for kod_wyk, [nazwa, mandat, punkty] in wykroczenia.items():
    if 'naruszenie zakazu' in nazwa.lower():
        print(nazwa)

_5_4 = defaultdict(list[int])
for pesel, lista_wykroczen in mandaty.items():
    for data_wyk, kod_wyk in lista_wykroczen:
        miesiac = data_wyk.month
        _5_4[miesiac].append(wykroczenia[kod_wyk][1])

nazwy_miesiecy = [
    'styczen', 'luty', 'marzec', 'kwiecien', 'maj', 'czerwiec', 'lipiec', 'sierpien', 'wrzesien', 'pazdziernik',
    'listopad', 'grudzien'
]

_5_4 = sorted(_5_4.items(), key=lambda x: len(x[1]))
print('\nZadanie 5.4.')
print(nazwy_miesiecy[_5_4[0][0] - 1], sum(_5_4[0][1]), len(_5_4[0][1]))

_5_5 = 0
_5_5_miasta = {}
print('\nZadanie 5.5.')
for pesel, [data_prawa_jazdy, miasto] in kierowcy.items():
    ma_mandaty = False
    for pesel_2, lista_wykroczen in mandaty.items():
        if pesel_2 == pesel:
            ma_mandaty = True
            break

    if not ma_mandaty:
        if miasto not in _5_5_miasta.keys():
            _5_5_miasta[miasto] = 0
        _5_5_miasta[miasto] += 1
        _5_5 += 1
_5_5_miasta = sorted(_5_5_miasta.items(), key=lambda x: x[1], reverse=True)
print(_5_5, _5_5_miasta[0][0])

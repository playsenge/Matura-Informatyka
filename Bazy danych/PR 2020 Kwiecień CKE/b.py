import datetime
from math import fsum
from collections import defaultdict

klienci = {}
zabiegi = {}
wizyty = {}


def datetime_format(x: str) -> datetime.date:
    [year, month, day] = [int(y) for y in x.split('-')]
    return datetime.date(year=year, month=month, day=day)


with open('DANE/klienci.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split('\t')
        klienci[line[0]] = [line[1], line[2]]

with open('DANE/zabiegi.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split('\t')
        zabiegi[line[0]] = [line[1], line[2], int(line[3])]

with open('DANE/wizytydane.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split('\t')
        wizyty[int(line[0])] = [datetime_format(line[1]), int(line[2]), line[3], []]

with open('DANE/wizytyzabiegi.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split('\t')
        wizyty[int(line[0])][3].append(line[1])

alicja_kowalska = 'X55'
_6_1 = 0
for id_wizyty, [data, nr_wizyty, id_klienta, zabiegi_dane] in wizyty.items():
    if id_klienta == alicja_kowalska:
        for zabieg in zabiegi_dane:
            _6_1 += zabiegi[zabieg][2]
print(_6_1, "zł")

_6_2 = defaultdict(int)
for id_wizyty, [data, nr_wizyty, id_klienta, zabiegi_dane] in wizyty.items():
    _6_2[id_klienta] += 1
_6_2 = sorted(_6_2.items(), key=lambda x: x[1], reverse=True)[0]
print(*klienci[_6_2[0]], _6_2[1])

magia_hawajow = 'FCR16'
_6_3_daty = []
for id_wizyty, [data, nr_wizyty, id_klienta, zabiegi_dane] in wizyty.items():
    if magia_hawajow in zabiegi_dane:
        _6_3_daty.append(data)
print(len(_6_3_daty))
print(*_6_3_daty[::-1], sep='\n')

kody_makijazy = ['MKZ1', 'MKZ2', 'MKZ3']
_6_4_ceny = []
for id_wizyty, [data, nr_wizyty, id_klienta, zabiegi_dane] in wizyty.items():
    if datetime_format('2017-12-6') <= data <= datetime_format('2018-1-15'):
        if id_klienta[0] == 'X':
            suma = 0
            for zabieg in zabiegi_dane:
                if zabieg in kody_makijazy:
                    suma += zabiegi[zabieg][2] * 0.8
            if suma > 0:
                _6_4_ceny.append(suma)
print(fsum(_6_4_ceny))
print(len(_6_4_ceny))

kody_fryzjera_meskiego = ['FRM1', 'FRM2', 'FRM3', 'FRM4', 'FRM5', 'FRM6', 'FRM7', 'FRM8']
for zabieg in kody_fryzjera_meskiego:
    uzytkownik = False

    for id_wizyty, [data, nr_wizyty, id_klienta, zabiegi_dane] in wizyty.items():
        if zabieg in zabiegi_dane:
            uzytkownik = True
            break

    if not uzytkownik:
        print(zabiegi[zabieg][1])
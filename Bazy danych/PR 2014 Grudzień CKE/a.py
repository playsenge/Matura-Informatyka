import datetime
import math
from collections import defaultdict

dane_osobowe = {}
transakcje = {}
asortyment = {}
us = {}

def koszt(x):
    return str("{:.2f}".format(round(x, 4))).replace('.', ',') + " zł"

def formatuj_date(x) -> datetime.date:
    [year, month, day] = [int(y) for y in x.split(' ')[0].split('-')]
    return datetime.date(year=year, month=month, day=day)


with open('DANE/us.txt') as f:
    for line in f.readlines()[1:]:
        line = [x.strip('"') for x in line.strip().split('\t')]
        us[int(line[0])] = line[1]

with open('DANE/asortyment.txt') as f:
    for line in f.readlines()[1:]:
        line = [x.strip('"') for x in line.strip().split('\t')]
        line[2] = float(line[2].strip(" zł").replace(',', '.'))
        asortyment[line[0]] = line[1:]

with open('DANE/dane_osobowe.txt') as f:
    for line in f.readlines()[1:]:
        line = [x.strip('"') for x in line.strip().split('\t')]
        line[3] = int(line[3])
        line[9] = int(line[9])
        dane_osobowe[line[0]] = line[1:]

with open('DANE/transakcje.txt') as f:
    for line in f.readlines()[1:]:
        line = [x.strip('"') for x in line.strip().split('\t')]
        line[3] = float(line[3].replace(',', '.'))
        line[4] = formatuj_date(line[4])
        transakcje[line[0]] = line[1:]

_6_1 = defaultdict(float)
for id_transakcji, [id_klienta, id_asortymentu, ilosc, data_transakcji] in transakcje.items():
    nazwisko = dane_osobowe[id_klienta][1]
    if (data_transakcji.year, data_transakcji.month, data_transakcji.day) == (2013, 1, 4) and (
            nazwisko[0] in ['O', 'o'] or nazwisko[-1] in ['O', 'o']):
        _6_1[nazwisko] += ilosc * asortyment[id_asortymentu][1]

print('Zadanie 6.1.')
_6_1 = sorted(_6_1.items(), key=lambda x: x[0])
for x in _6_1:
    print(x[0], koszt(x[1]))

_6_2 = defaultdict(float)
for id_transakcji, [id_klienta, id_asortymentu, ilosc, data_transakcji] in transakcje.items():
    if id_asortymentu == 'OO' and formatuj_date('2013-8-1') <= data_transakcji <= formatuj_date(
            '2014-1-31'):  # Olej opałowy
        klucz = f"{str(data_transakcji.month).zfill(2)}.{data_transakcji.year}"
        _6_2[klucz] = math.fsum([_6_2[klucz], ilosc * asortyment[id_asortymentu][1]])

_6_2_sortowanie = ['08.2013', '09.2013', '10.2013', '11.2013', '12.2013', '01.2014']

print('\nZadanie 6.2.')
for x in _6_2_sortowanie:
    print(x, koszt(_6_2[x]))

print('\nZadanie 6.3.')
_6_3 = defaultdict(float)
for id_transakcji, [id_klienta, id_asortymentu, ilosc, data_transakcji] in transakcje.items():
    if id_asortymentu == 'K':  # ID koksu
        _6_3[id_klienta] += ilosc
_6_3 = sorted(_6_3.items(), key=lambda x: x[1], reverse=True)[0]
print(dane_osobowe[_6_3[0]][0], dane_osobowe[_6_3[0]][1], _6_3[1])

print('\nZadanie 6.4.')
_6_4 = set()
for id_klienta, [imie, nazwisko, prefix_nip, nip, wojewodztwo, kod, miejscowosc, ulica,
                 nr_domu] in dane_osobowe.items():
    if wojewodztwo == 'podlaskie':
        zakup = False
        for id_transakcji, [id_klienta_2, id_asortymentu, ilosc, data_transakcji] in transakcje.items():
            if id_klienta_2 == id_klienta:
                zakup = True
                break

        if not zakup:
            _6_4.add(id_klienta)

for id_klienta in _6_4:
    print(id_klienta, dane_osobowe[id_klienta][0], dane_osobowe[id_klienta][1])


def default_6_5():
    return [0, 0]


print('\nZadanie 6.5.')
_6_5 = defaultdict(default_6_5)
for id_transakcji, [id_klienta, id_asortymentu, ilosc, data_transakcji] in transakcje.items():
    if id_asortymentu in ['K', 'M']:  # Koks lub miał
        nazwa_us = us[dane_osobowe[id_klienta][2]]
        dotychczasowe = _6_5[nazwa_us]
        if id_asortymentu == 'K':
            dotychczasowe[0] += ilosc * asortyment[id_asortymentu][1]
        else:
            dotychczasowe[1] += ilosc * asortyment[id_asortymentu][1]
        _6_5[nazwa_us] = dotychczasowe

for x, y in _6_5.items():
    if 'warsz' in x.lower():
        print(x, *[koszt(z) for z in y])
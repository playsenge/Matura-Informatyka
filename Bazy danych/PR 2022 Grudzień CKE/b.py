from collections import defaultdict
import datetime


def date_format(x: str) -> datetime.date:
    [year, month, day] = [int(y) for y in x.split('-')]
    return datetime.date(year=year, month=month, day=day)


klienci = {}
pokoje = {}
noclegi = {}

with open('DANE/klienci.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split('\t')
        klienci[line[0]] = line[1:]

with open('DANE/pokoje.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split('\t')
        pokoje[int(line[0])] = [line[1], int(line[2])]

with open('DANE/noclegi.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split('\t')
        noclegi[int(line[0])] = [date_format(line[1]), date_format(line[2]), line[3], int(line[4])]

#################################################

_5_1 = defaultdict(int)
for id_pobytu, [data_przyjazdu, data_wyjazdu, nr_dowodu, nr_pokoju] in noclegi.items():
    doby = (data_wyjazdu - data_przyjazdu).days
    _5_1[nr_dowodu] += doby

_5_1 = sorted(_5_1.items(), key=lambda x: x[1], reverse=True)
print(*klienci[_5_1[0][0]][:2], _5_1[0][1])

#################################################

_5_2 = defaultdict(int)
for id_pobytu, [data_przyjazdu, data_wyjazdu, nr_dowodu, nr_pokoju] in noclegi.items():
    doby = (data_wyjazdu - data_przyjazdu).days
    cena = doby * pokoje[nr_pokoju][1]
    _5_2[nr_dowodu] += cena

for x, y in _5_2.items():
    if y > 2000:
        print(*klienci[x][:2], y)

#################################################

for nr_pokoju, [standard, cena] in pokoje.items():
    if standard == 'N':
        warunek = True

        for id_pobytu, [data_przyjazdu, data_wyjazdu, nr_dowodu, nr_pokoju_2] in noclegi.items():
            if nr_pokoju == nr_pokoju_2:
                miasto = klienci[nr_dowodu][2]
                if miasto in ['Opole', 'Katowice'] and date_format('2022-07-01') <= data_przyjazdu <= date_format('2022-09-30'):
                    warunek = False
                    break

        if warunek:
            print(nr_pokoju)

#################################################

"""
SELECT rodzaj, count(*)
FROM uslugi_dodatkowe
GROUP BY rodzaj;
"""

"""
SELECT klienci.imie, klienci.nazwisko, SUM(uslugi_dodatkowe.cena_uslugi) FROM klienci
INNER JOIN noclegi ON klienci.nr_dowodu = noclegi.nr_dowodu
INNER JOIN uslugi_dodatkowe ON noclegi.id_pobytu = uslugi_dodatkowe.id_pobytu
GROUP BY klienci.nr_dowodu;
"""
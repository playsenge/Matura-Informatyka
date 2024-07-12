import datetime
import sys

sys.stdout = open('wyniki5.txt', 'w', encoding='UTF-8')

druzyny = {}
sedziowie = {}
wyniki = {}


def formatuj_date(x):
    [year, month, day] = [int(y) for y in x.strip().split('-')]
    return datetime.date(year=year, month=month, day=day)


with open('DANE/druzyny.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split('\t')
        line[0] = int(line[0])
        druzyny[line[0]] = line[1:]

with open('DANE/sedziowie.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split('\t')
        sedziowie[line[0]] = line[1:]

with open('DANE/wyniki.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split('\t')
        line[0] = formatuj_date(line[0])
        line[3] = int(line[3])
        line[5] = int(line[5])
        line[6] = int(line[6])
        wyniki[line[0]] = line[1:]

_5_1a = {}
_5_1b = {}
for data_meczu, [rodzaj_meczu, gdzie, id_druzyny, nr_licencji, bramki_zdobyte, bramki_stracone] in wyniki.items():
    miasto_przeciwnika = druzyny[id_druzyny][1]
    if miasto_przeciwnika == 'Kucykowo':
        if rodzaj_meczu not in _5_1a.keys():
            _5_1a[rodzaj_meczu] = 0
        _5_1a[rodzaj_meczu] += 1

        rok = data_meczu.year
        if rok not in _5_1b.keys():
            _5_1b[rok] = 0
        _5_1b[rok] += 1

print('Zadanie 5.1.')
print('a)')
for x, y in _5_1a.items():
    print(x, y)

print('b)')
_5_1b = sorted(_5_1b.items(), key=lambda x: x[1], reverse=True)
print(*_5_1b[0])

_5_2 = {}
print()
print('Zadanie 5.2.')
for data_meczu, [rodzaj_meczu, gdzie, id_druzyny, nr_licencji, bramki_zdobyte, bramki_stracone] in wyniki.items():
    if id_druzyny not in _5_2.keys():
        _5_2[id_druzyny] = 0
    _5_2[id_druzyny] += bramki_zdobyte
    _5_2[id_druzyny] -= bramki_stracone
for x, y in _5_2.items():
    if y == 0:  # Zerowy bilans
        print(druzyny[x][0])

print()
print('Zadanie 5.3.')
_5_3_wygrane = 0
_5_3_przegrane = 0
_5_3_zremisowane = 0
for data_meczu, [rodzaj_meczu, gdzie, id_druzyny, nr_licencji, bramki_zdobyte, bramki_stracone] in wyniki.items():
    if gdzie == 'W':
        if bramki_stracone == bramki_zdobyte:
            _5_3_zremisowane += 1
        elif bramki_stracone > bramki_zdobyte:
            _5_3_przegrane += 1
        else:
            _5_3_wygrane += 1
print('Wygrane:', _5_3_wygrane)
print('Przegrane:', _5_3_przegrane)
print('Zremisowane:', _5_3_zremisowane)

_5_4 = 0
print()
print('Zadanie 5.4.')
for nr_licencji, [imie, nazwisko] in sedziowie.items():
    sedziowal = False

    for data_meczu, [rodzaj_meczu, gdzie, id_druzyny, nr_licencji_2, bramki_zdobyte, bramki_stracone] in wyniki.items():
        if nr_licencji_2 == nr_licencji and rodzaj_meczu == 'P':
            sedziowal = True
            break

    if not sedziowal:
        _5_4 += 1
print(_5_4)
jablka = []
cennik = {}

import datetime

miesiace = [
    'styczen',
    'luty',
    'marzec',
    'kwiecien',
    'maj',
    'czerwiec',
    'lipiec',
    'sierpien',
    'wrzesien',
    'pazdziernik',
    'listopad',
    'grudzien'
]

def data_format(x) -> datetime.date:
    [year, month, day] = [int(y) for y in x.strip().split('-')]
    return datetime.date(year=year, month=month, day=day)

with open('DANE/cennik.txt') as plik:
    for line in plik.readlines():
        line = line.strip().split('\t')
        cennik[line[0]] = float(line[1].replace(',','.'))

with open('DANE/jablka.txt') as plik:
    for line in plik.readlines():
        line = line.strip().split('\t')
        line[0] = data_format(line[0])
        line[4] = int(line[4])
        line.append(cennik[line[1]]*line[4])

        jablka.append(line)

_7_1 = {}
_7_2 = {}
_7_3 = {}
for x in jablka:
    [data, nazwa, kod, nip, kilogramy, koszt] = x

    if kod == 'Z':
        if nip not in _7_1.keys():
            _7_1[nip] = 0
        _7_1[nip] += kilogramy

    if nazwa not in _7_2.keys():
        _7_2[nazwa] = 0

    miesiac = miesiace[data.month-1]
    if miesiac not in _7_3.keys():
        _7_3[miesiac] = {}
    if nazwa not in _7_3[miesiac].keys():
        _7_3[miesiac][nazwa] = 0
    _7_3[miesiac][nazwa] += kilogramy

    _7_2[nazwa] += koszt

_7_1 = sorted(_7_1.items(), key=lambda x: x[1], reverse=True)
for x in _7_1[:3]:
    print(*x)
print("=" * 25)

_7_2 = sorted(_7_2.items(), key=lambda x: x[1], reverse=True)
print(sum([x[1] for x in _7_2]))
print(_7_2[0][0], _7_2[0][1])
print("=" * 25)

for x, y in _7_3.items():
    y = sorted(y.items(), key=lambda x: x[1], reverse=True)
    print(x + ' - ' + str(y[0][0]), y[0][1], sep='\t')
print("=" * 25)

jablka_po_nipie = {}
for x in jablka:
    [data, nazwa, kod, nip, kilogramy, koszt] = x

    if nip not in jablka_po_nipie.keys():
        jablka_po_nipie[nip] = []

    jablka_po_nipie[nip].append(x)

transakcje_rabat = 0
suma_rabat = 0

for nip in jablka_po_nipie.keys():
    dotychczasowe = 0
    for x in jablka_po_nipie[nip]:
        [data, nazwa, kod, nip, kilogramy, koszt] = x
        dotychczasowe += kilogramy

        if dotychczasowe in range(15000, 20000):
            suma_rabat += kilogramy * 0.05
            transakcje_rabat += 1
        elif dotychczasowe >= 20000:
            suma_rabat += kilogramy * 0.10
            transakcje_rabat += 1

print(transakcje_rabat)
print(round(suma_rabat, 5))

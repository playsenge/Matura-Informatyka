import datetime
from collections import defaultdict

podpunkt = 1
def KOLEJNE():
    global podpunkt
    if podpunkt != 1:
        print()
    print(f'{"="*5} Zadanie 8.{podpunkt}. {"="*5}')
    podpunkt += 1


def datetime_format(x: str) -> datetime.date:
    [year, month, day] = [int(y) for y in x.strip().split('-')]
    return datetime.date(year=year, month=month, day=day)


kierowcy = {}
taryfikator = {}
rejestr = {}

with open('DANE/kierowcy.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split(';')
        line[0] = int(line[0])
        kierowcy[line[0]] = line[1:]

with open('DANE/taryfikator.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split(';')
        line[0] = int(line[0])
        line[2] = int(line[2])
        line[3] = int(line[3])
        taryfikator[line[0]] = line[1:]

with open('DANE/rejestr.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split(';')
        line[0] = int(line[0])
        line[1] = datetime_format(line[1])
        line[2] = int(line[2])
        line[3] = int(line[3])
        rejestr[line[0]] = line[1:]

KOLEJNE()
_8_1 = defaultdict(int)
for idzdarzenia, [data, idosoby, idwykroczenia] in rejestr.items():
    _8_1[idosoby] += taryfikator[idwykroczenia][2]

_8_1 = sorted(_8_1.items(), key=lambda x: x[1], reverse=True)[0]
print(kierowcy[_8_1[0]][0], kierowcy[_8_1[0]][1], _8_1[1])

KOLEJNE()
_8_2 = defaultdict(int)
for idzdarzenia, [data, idosoby, idwykroczenia] in rejestr.items():
    miesiac = data.month
    if 3 <= idwykroczenia <= 6:
        _8_2[miesiac] += taryfikator[idwykroczenia][1]

miesiac_nazwy = [
    'styczen', 'luty', 'marzec', 'kwiecien', 'maj', 'czerwiec', 'lipiec', 'sierpien', 'wrzesien', 'pazdziernik',
    'listopad', 'grudzien'
]
_8_2 = sorted(_8_2.items(), key=lambda x: x[1], reverse=False)[0]
print(miesiac_nazwy[_8_2[0] - 1], _8_2[1])

KOLEJNE()
_8_3 = []
for idosoby, [imie, nazwisko, nrrejestracyjny] in kierowcy.items():
    przestepca = False

    for idzdarzenia, [data, idosoby2, idwykroczenia] in rejestr.items():
        if idosoby2 == idosoby:
            przestepca = True
            break

    if not przestepca:
        _8_3.append((imie, nazwisko, nrrejestracyjny))

_8_3 = sorted(_8_3, key=lambda x: x[2])
for x in _8_3:
    print(*x)
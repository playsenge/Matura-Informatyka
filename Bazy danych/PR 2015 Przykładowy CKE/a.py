import sys
import datetime
from collections import defaultdict

sys.stdout = open('wyniki_serwis.txt', 'w')

def datetime_format(x: str) -> datetime.date:
    [year, month, day] = [int(y) for y in x.strip().split('-')]
    return datetime.date(year=year, month=month, day=day)


def datetime_str(x: datetime.date) -> str:
    return f"{x.year}-{str(x.month).zfill(2)}-{str(x.day).zfill(2)}"


pojazd = {}
usluga = {}
firma = {}
naprawa = {}

with open('DANE/pojazd.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split('\t')
        pojazd[line[0]] = [line[1], int(line[2]), line[3]]

with open('DANE/usluga.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split('\t')
        usluga[int(line[0])] = [line[1], int(line[2])]

with open('DANE/firma.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split('\t')
        firma[line[0]] = line[1]

with open('DANE/naprawa.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split('\t')
        naprawa[int(line[0])] = [datetime_format(line[1]), line[2], int(line[3])]

wymiana_opon = 19
daty = set()
for id, [data, nr_rejestr, usluga_id] in naprawa.items():
    if usluga_id == wymiana_opon and nr_rejestr == 'PO 3631H':
        daty.add(data)

print('a)')
print(*[datetime_str(x) for x in daty], sep='\n')

floty = defaultdict(int)
for nr_rejestr, [marka, rok_prod, firma_id] in pojazd.items():
    floty[firma[firma_id]] += 1
floty = sorted(floty.items(), key=lambda x: x[1], reverse=True)

print()
print('b)')
for x in floty:
    print(*x)

lubex_koszty = {}
lubex_id = 'LU1'
for i in range(1, 13):
    lubex_koszty[i] = 0
for id, [data, nr_rejestr, usluga_id] in naprawa.items():
    firma_id = pojazd[nr_rejestr][2]
    if firma_id == lubex_id:
        lubex_koszty[data.month] += usluga[usluga_id][1]

print()
print('c)')
for x, y in lubex_koszty.items():
    print(x, y)

wykorzystanie = defaultdict(int)
for id, [data, nr_rejestr, usluga_id] in naprawa.items():
    wykorzystanie[nr_rejestr] += 1
wykorzystanie = sorted(wykorzystanie.items(), key=lambda x: x[1], reverse=True)[0][0]

print()
print('d)')
print(wykorzystanie, pojazd[wykorzystanie][0], firma[pojazd[wykorzystanie][2]])

firmy_plyn = set()
wymiana_plynu = 3
for id, [data, nr_rejestr, usluga_id] in naprawa.items():
    if usluga_id == wymiana_plynu:
        if pojazd[nr_rejestr][1] < 2009:
            firma_id = pojazd[nr_rejestr][2]
            firma_nazwa = firma[firma_id]
            firmy_plyn.add(firma_nazwa)

print()
print('e)')
print(*firmy_plyn, sep='\n')

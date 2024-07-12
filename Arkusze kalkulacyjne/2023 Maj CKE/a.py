owoce = []

import datetime

nazwymsc = [
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
    'grudzien',
]

def data_z(x):
    x = x.strip().split('.')
    [day, month, year] = [int(y) for y in x]
    return datetime.date(day=day, month=month, year=year)

with open('DANE/owoce.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split('\t')
        line[0] = data_z(line[0])
        line[1], line[2], line[3] = int(line[1]), int(line[2]), int(line[3])
        owoce.append(line)

_6_1 = {}
_6_2 = 0
for x in owoce:
    [data, dostawa_malin, dostawa_truskawek, dostawa_porzeczek] = x

    miesiac = nazwymsc[data.month-1]
    if miesiac not in _6_1.keys():
        _6_1[miesiac] = [0, 0, 0]

    _6_1[miesiac][0] += dostawa_malin
    _6_1[miesiac][1] += dostawa_truskawek
    _6_1[miesiac][2] += dostawa_porzeczek

    if dostawa_porzeczek == max(dostawa_malin, dostawa_truskawek, dostawa_porzeczek):
        _6_2 += 1

for x, y in _6_1.items():
    print(x, *y)

print(_6_2)

for _ in range(3):
    owoce[0].append(0)

mt = 0
mp = 0
tp = 0

wyprodukowano = {'mt':0,'mp':0,'tp':0}

for i, x in enumerate(owoce):
    [data, dostawa_malin, dostawa_truskawek, dostawa_porzeczek, chlodnia_malin, chlodnia_truskawek, chlodnia_porzeczek] = x

    maliny = dostawa_malin + chlodnia_malin
    truskawki = dostawa_truskawek + chlodnia_truskawek
    porzeczki = dostawa_porzeczek + chlodnia_porzeczek

    posortowane = sorted([maliny, truskawki, porzeczki], reverse=True)[:2]

    ilosc = 0
    pozostawione_m = 0
    pozostawione_t = 0
    pozostawione_p = 0

    if posortowane == [maliny, truskawki] or posortowane == [truskawki, maliny]:
        # Malinowo-truskawkowa
        ilosc = min(maliny, truskawki)
        pozostawione_m = maliny - ilosc
        pozostawione_t = truskawki - ilosc
        pozostawione_p = porzeczki
        mt += 1
        wyprodukowano['mt'] += ilosc
    elif posortowane == [maliny, porzeczki] or posortowane == [porzeczki, maliny]:
        # Malinowo-porzeczkowe
        ilosc = min(maliny, porzeczki)
        pozostawione_m = maliny - ilosc
        pozostawione_t = truskawki
        pozostawione_p = porzeczki - ilosc
        mp += 1
        wyprodukowano['mp'] += ilosc
    elif posortowane == [porzeczki, truskawki] or posortowane == [truskawki, porzeczki]:
        # Truskawkowo-porzeczkowa
        ilosc = min(porzeczki, truskawki)
        pozostawione_m = maliny
        pozostawione_t = truskawki - ilosc
        pozostawione_p = porzeczki - ilosc
        tp += 1
        wyprodukowano['tp'] += ilosc

    if i != len(owoce) - 1:
        owoce[i+1].append(pozostawione_m)
        owoce[i+1].append(pozostawione_t)
        owoce[i+1].append(pozostawione_p)

print('mt', mt)
print('mp', mp)
print('mt', tp)
for x, y in wyprodukowano.items():
    print(x, y)
print('suma', sum(wyprodukowano.values()))
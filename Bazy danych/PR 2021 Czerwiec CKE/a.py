import datetime


def data_konwertuj(x) -> datetime.date:
    [year, month, day] = [int(y) for y in x.strip().split('-')]
    return datetime.date(year=year, month=month, day=day)


zespoly = {}
miasta = {}
koncerty = {}

with open('DANE/zespoly.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split(';')
        zespoly[int(line[0])] = [line[1], int(line[2])]

with open('DANE/miasta.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split(';')
        miasta[line[0]] = [line[1], line[2]]

with open('DANE/koncerty.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split(';')
        koncerty[int(line[0])] = [int(line[1]), line[2], data_konwertuj(line[3])]

_6_1 = 0
for id, [id_zespolu, kod_miasta, data] in koncerty.items():
    if data.month == 7:
        _6_1 += 1

print('Zadanie 6.1.')
print(_6_1)

_6_2 = {}
for id, [id_zespolu, kod_miasta, data] in koncerty.items():
    if kod_miasta not in _6_2.keys():
        _6_2[kod_miasta] = []

    if id_zespolu not in _6_2[kod_miasta]:
        _6_2[kod_miasta].append(id_zespolu)

_6_2b = {}
for x, y in _6_2.items():
    num = 0
    for i in y:
        num += zespoly[i][1]
    _6_2b[x] = num

print()
print('Zadanie 6.2.')
print('Miasto\tLiczba artystów')
_6_2b = _6_2b.items()
_6_2b_num = max(_6_2b, key=lambda x: x[1])[1]
for element in _6_2b:
    [kod_miasta, wystepienia] = element
    if wystepienia == _6_2b_num:
        print(miasta[kod_miasta][0], wystepienia, sep='\t')

_6_3a = {}
_6_3b = {}
for kod, [miasto, wojewodztwo] in miasta.items():
    if wojewodztwo not in _6_3a.keys():
        _6_3a[wojewodztwo] = 0
    _6_3a[wojewodztwo] += 1

for id, [id_zespolu, kod_miasta, data] in koncerty.items():
    wojewodztwo = miasta[kod_miasta][1]
    if wojewodztwo not in _6_3b.keys():
        _6_3b[wojewodztwo] = 0
    _6_3b[wojewodztwo] += 1

srednie = {}
for wojewodztwo in _6_3a.keys():
    srednie[wojewodztwo] = _6_3b[wojewodztwo] / _6_3a[wojewodztwo]

print()
print('Zadanie 6.3.')
print('Miasto\tŚrednia liczba koncertów')
srednie = sorted(srednie.items(), key=lambda x: x[1], reverse=True)
for i in srednie:
    print(i[0], '{:.2f}'.format(round(i[1], 2)), sep='\t')

print()
print('Zadanie 6.4.')
for id_zespolu, [nazwa, liczba_artystow] in zespoly.items():
    wystepowali = False

    for id, [id_zespolu_2, kod_miasta, data] in koncerty.items():
        if id_zespolu_2 == id_zespolu:
            if data_konwertuj('2017-7-20') <= data <= data_konwertuj('2017-7-25'):
                wystepowali = True
                break

    if not wystepowali:
        print(nazwa)

_6_5_weekendy = {}
_6_5_powszednie = {}

for id, [id_zespolu, kod_miasta, data] in koncerty.items():
    dzien_tygodnia = data.weekday() + 1

    if dzien_tygodnia in [6, 7]:
        if id_zespolu not in _6_5_weekendy.keys():
            _6_5_weekendy[id_zespolu] = 0
        _6_5_weekendy[id_zespolu] += 1
    else:
        if id_zespolu not in _6_5_powszednie.keys():
            _6_5_powszednie[id_zespolu] = 0
        _6_5_powszednie[id_zespolu] += 1

print()
print('Zadanie 6.5.')
print('Nazwa\tKoncerty w weekendy\tKoncerty w dni powszednie')
for zespol in _6_5_weekendy.keys():
    weekendy = _6_5_weekendy[zespol]
    powszednie = _6_5_powszednie[zespol]

    if weekendy > powszednie:
        print(zespoly[zespol][0], weekendy, powszednie, sep='\t')

import datetime


def datetime_format(x) -> datetime.date:
    [year, month, day] = [int(y) for y in x.strip().split('-')]
    return datetime.date(year=year, month=month, day=day)


maturzysci = {}
przedmioty = {}
zdaje = {}

with open('DANE/maturzysta.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split(';')
        line[0] = int(line[0])
        line[4] = datetime_format(line[4])
        maturzysci[line[0]] = line[1:]

with open('DANE/przedmioty.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split(';')
        line[0] = int(line[0])
        line[2] = datetime_format(line[2])
        przedmioty[line[0]] = line[1:]

with open('DANE/zdaje.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split(';')
        line[0] = int(line[0])
        line[1] = int(line[1])
        if line[0] not in zdaje.keys():
            zdaje[line[0]] = []
        zdaje[line[0]].append(line[1])

print('Zadanie 5.1.')
id_informatyka = 15
_5_1 = []
for id_zdajacego, [nazwisko, imie, pesel, data_urodzenia] in maturzysci.items():
    if id_informatyka in zdaje[id_zdajacego]:
        _5_1.append([nazwisko, imie])
_5_1 = sorted(_5_1, key=lambda x: x[0])
for x in _5_1:
    print(*x)

print('\nZadanie 5.2.')
_5_2 = {}
for id_zdajacego, x in zdaje.items():
    for przedmiot in x:
        if przedmioty[przedmiot][3] == 'dodatkowy':
            if przedmiot not in _5_2.keys():
                _5_2[przedmiot] = 0
            _5_2[przedmiot] += 1
_5_2 = sorted(_5_2.items(), key=lambda x: x[1], reverse=True)
print(przedmioty[_5_2[0][0]][0], _5_2[0][1])

_5_3 = {}
for id_zdajacego, x in zdaje.items():
    dodatkowe = []
    for przedmiot in x:
        if przedmioty[przedmiot][3] == 'dodatkowy':
            dodatkowe.append(przedmiot)
    _5_3[id_zdajacego] = dodatkowe

print('\nZadanie 5.3.')
_5_3_max = len(max(_5_3.items(), key=lambda x: len(x[1]))[1])
for i, j in _5_3.items():
    if len(j) == _5_3_max:
        print(maturzysci[i][0], maturzysci[i][1], len(j))

print('\nZadanie 5.4.')
for id_przedmiotu, [nazwa_przedmiotu, data, godzina, typ] in przedmioty.items():
    if typ == 'dodatkowy':
        wybrany = False
        for id_zdajacego, x in zdaje.items():
            for przedmiot in x:
                if przedmiot == id_przedmiotu:
                    wybrany = True
                    break

        if not wybrany:
            print(nazwa_przedmiotu)

print('\nZadanie 5.5.')
_5_5 = max(maturzysci.items(), key=lambda x: x[1][3])
print(_5_5[1][0], _5_5[1][1])
for id_przedmiotu, [nazwa_przedmiotu, data, godzina, typ] in przedmioty.items():
    if typ == 'dodatkowy' and id_przedmiotu in zdaje[_5_5[0]]:  # W kluczu jest błąd, podają tam wszystkie
        # przedmioty, a nie tylko dodatkowe
        print(nazwa_przedmiotu)

print('\nZadanie 5.6.')
print(sum(int(pesel[-2]) % 2 != 0 for id_zdajacego, [nazwisko, imie, pesel, data_urodzenia] in maturzysci.items()))

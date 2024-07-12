import datetime

statki = {}
przybycia = {}
kody = {}


def data_formatuj(x):
    [day, month, year] = [int(y) for y in x.strip().split('.')]
    return datetime.date(day=day, month=month, year=year)


with open('DANE/statki.txt', encoding='UTF-8') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split(';')
        statki[int(line[0])] = [line[1], int(line[2])]

with open('DANE/przybycia.txt', encoding='UTF-8') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split(';')
        przybycia[int(line[0])] = [data_formatuj(line[1]), int(line[2]), line[3], line[4]]

with open('DANE/kody.txt', encoding='UTF-8') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split(';')
        kody[line[0]] = [line[1], line[2]]

_5_1 = {}
for lp, [data_przybycia, nr_imo, bandera, nabrzeze] in przybycia.items():
    rok = data_przybycia.year
    if rok not in _5_1.keys():
        _5_1[rok] = 0

    _5_1[rok] += 1
_5_1 = sorted(_5_1.items(), key=lambda x: x[0])

print('Zadanie 5.1.')
for x in _5_1:
    print(*x)

_5_2 = {}
for lp, [data_przybycia, nr_imo, bandera, nabrzeze] in przybycia.items():
    if nabrzeze not in _5_2.keys():
        _5_2[nabrzeze] = []

    [nazwa_statku, ladownosc] = statki[nr_imo]
    if _5_2[nabrzeze] == [] or _5_2[nabrzeze][1] < ladownosc:
        _5_2[nabrzeze] = [nazwa_statku, ladownosc]

print()
print('Zadanie 5.2.')
for x, y in _5_2.items():
    print(x, *y)

_5_3 = {}
for lp, [data_przybycia, nr_imo, bandera, nabrzeze] in przybycia.items():
    if nabrzeze not in _5_3.keys():
        _5_3[nabrzeze] = False

    if kody[bandera][1] == 'EUROPA':
        _5_3[nabrzeze] = True

print()
print('Zadanie 5.3.')
for x, y in _5_3.items():
    if not y:
        print(x)

# SELECT Typ_dzialalnosci, Count(*)
# FROM Armator
# GROUP BY Typ_dzialalnosci
# ORDER BY Count(*) DESC;

# SELECT Statki.Nazwa_statku
# FROM (Statki INNER JOIN Przybycia ON Statki.Nr_IMO = Przybycia.Nr_IMO) INNER JOIN Armator ON Przybycia.Id_armatora = Armator.Id_armatora
# GROUP BY Statki.Nazwa_statku, Armator.Armator
# HAVING Armator.Armator = "XYZ";

# 6 FPP btw
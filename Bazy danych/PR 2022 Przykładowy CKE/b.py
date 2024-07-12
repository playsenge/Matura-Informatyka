import datetime

statki = {}
kody = {}
przybycia = {}


def data_format(x: str) -> datetime.date:
    [day, month, year] = [int(y) for y in x.split('.')]
    return datetime.date(year=year, month=month, day=day)

with open('wyniki5.txt', 'w', encoding='UTF-8') as main_f:
    with open('DANE/statki.txt', encoding='UTF-8') as f:
        for line in f.readlines()[1:]:
            line = line.strip().split(';')
            statki[int(line[0])] = [line[1], int(line[2])]

    with open('DANE/kody.txt', encoding='UTF-8') as f:
        for line in f.readlines()[1:]:
            line = line.strip().split(';')
            kody[line[0]] = [line[1], line[2]]

    with open('DANE/przybycia.txt', encoding='UTF-8') as f:
        for line in f.readlines()[1:]:
            line = line.strip().split(';')
            przybycia[int(line[0])] = [data_format(line[1]), int(line[2]), line[3], line[4]]

    print("Zadanie 5.1.", file=main_f)
    _5_1 = {}
    for rok in [2016, 2017, 2018, 2019]:
        _5_1[rok] = 0

    for lp, [data_przybycia, nr_imo, bandera, nabrzeze] in przybycia.items():
        _5_1[data_przybycia.year] += 1

    for x, y in _5_1.items():
        print(x, y, file=main_f)

    print(file=main_f)
    print("Zadanie 5.2.", file=main_f)
    _5_2_klucze = set()
    for lp, [data_przybycia, nr_imo, bandera, nabrzeze] in przybycia.items():
        _5_2_klucze.add(nabrzeze)
    _5_2_klucze = list(_5_2_klucze)
    for nabrzeze in _5_2_klucze:
        najw = ()

        for lp, [data_przybycia, nr_imo, bandera, nabrzeze_2] in przybycia.items():
            if nabrzeze_2 == nabrzeze:
                [nazwa, ladownosc] = statki[nr_imo]
                if najw == () or najw[0] < ladownosc:
                    najw = (ladownosc, nazwa)

        print(nabrzeze, *najw, file=main_f)

    print(file=main_f)
    print("Zadanie 5.3.", file=main_f)
    for nabrzeze in _5_2_klucze:
        cumowal = False

        for lp, [data_przybycia, nr_imo, bandera, nabrzeze_2] in przybycia.items():
            if nabrzeze == nabrzeze_2:
                if kody[bandera][1] == 'EUROPA':
                    cumowal = True
                    break

        if not cumowal:
            print(nabrzeze, file=main_f)

"""
SELECT Typ_dzialalnosci, COUNT(*) FROM Armator
GROUP BY Typ_dzialnosci
ORDER BY COUNT(*) DESC;
"""

"""
SELECT DISTINCT Statki.Nazwa_statku FROM Przybycia
LEFT JOIN Statki on Przybycia.Nr_IMO = Statki.Nr_IMO
LEFT JOIN Armator on Armator.Id_armatora = Przybycia.Id_armatora
WHERE Armator.Armator = "XYZ";
"""
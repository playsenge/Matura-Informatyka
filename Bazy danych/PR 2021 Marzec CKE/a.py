import datetime

obecne_zadanie = 1


def oglos_nastepne() -> None:
    global obecne_zadanie
    if obecne_zadanie != 1:
        print()
    print('=' * 5, f'Zadanie {obecne_zadanie}', '=' * 5)
    obecne_zadanie += 1


grupy = {}
zawodnicy = {}
startujacy = {}
czasy = {}


def data_od(x) -> datetime.date:
    [year, month, day] = [int(y) for y in x.strip().split('-')]
    return datetime.date(year=year, month=month, day=day)


def sekundy(x) -> float:
    x = [int(y) for y in x.strip().split(':')]
    czas = datetime.timedelta(milliseconds=x[2], seconds=x[1], minutes=x[0])
    return czas.total_seconds()


with open('DANE/grupy.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split('\t')
        grupy[line[0]] = line[1:]

with open('DANE/zawodnicy.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split('\t')
        line[0] = int(line[0])
        line[3] = data_od(line[3])
        zawodnicy[line[0]] = line[1:]

with open('DANE/startujacy.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split('\t')
        line[0] = int(line[0])
        line[1] = int(line[1])
        line[2] = int(line[2])
        startujacy[line[0]] = line[1:]

with open('DANE/czasy.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split('\t')
        line[0] = int(line[0])
        czasy[line[0]] = line[1]

_6_1 = []
for id_startu, [rok, id_zawodnika, kod_grupy, obywatel_kraju] in startujacy.items():
    if id_startu in czasy.keys():
        czas = czasy[id_startu]
        if _6_1 == [] or sekundy(czas) < sekundy(_6_1[2]):
            _6_1 = [zawodnicy[id_zawodnika][0], zawodnicy[id_zawodnika][1], czas]

oglos_nastepne()
print(*_6_1)

_6_2 = {}
for id_startu, [rok, id_zawodnika, kod_grupy, obywatel_kraju] in startujacy.items():
    if obywatel_kraju == 'Polska':
        if id_zawodnika not in _6_2.keys():
            _6_2[id_zawodnika] = 0
        _6_2[id_zawodnika] += 1

_6_2 = sorted(_6_2.items(), key=lambda x: x[1], reverse=True)
_6_2_id = _6_2[0][0]
_6_2_imie = zawodnicy[_6_2_id][0]
_6_2_nazwisko = zawodnicy[_6_2_id][1]
oglos_nastepne()
print(_6_2_imie, _6_2_nazwisko, _6_2[0][1])

lata = {}
for id_startu, [rok, id_zawodnika, kod_grupy, obywatel_kraju] in startujacy.items():
    wiek = rok - zawodnicy[id_zawodnika][2].year
    if rok not in lata.keys() or lata[rok] > wiek:
        lata[rok] = wiek

oglos_nastepne()
for rok, oczekiwany_wiek in lata.items():
    z = []
    for id_startu, [rok_2, id_zawodnika, kod_grupy, obywatel_kraju] in startujacy.items():
        if rok_2 == rok and (rok_2 - zawodnicy[id_zawodnika][2].year) == oczekiwany_wiek:
            z.append(zawodnicy[id_zawodnika][0] + " " + zawodnicy[id_zawodnika][1])

    print(rok, *z, sep='\t')

_6_4 = {}
for id_startu, [rok, id_zawodnika, kod_grupy, obywatel_kraju] in startujacy.items():
    if rok not in _6_4.keys():
        _6_4[rok] = 0

    if id_startu not in czasy.keys():
        _6_4[rok] += 1

_6_4 = sorted(_6_4.items(), key=lambda x: x[1], reverse=True)
oglos_nastepne()
print(*_6_4[0], sep='\t')

_6_5 = {}
for id_startu, [rok, id_zawodnika, kod_grupy, obywatel_kraju] in startujacy.items():
    if rok not in _6_5.keys():
        _6_5[rok] = []

    if kod_grupy not in _6_5[rok]:
        _6_5[rok].append(kod_grupy)

oglos_nastepne()
_6_5b = {}
for rok, startujace_grupy in _6_5.items():
    grup_nie_roznorodnych = []
    for grupa in startujace_grupy:
        panstwa_zawodnikow = []
        for id_startu, [rok_2, id_zawodnika, kod_grupy, obywatel_kraju] in startujacy.items():
            if rok == rok_2 and kod_grupy == grupa:
                panstwa_zawodnikow.append(obywatel_kraju)

        if len(panstwa_zawodnikow) == panstwa_zawodnikow.count(panstwa_zawodnikow[0]):
            grup_nie_roznorodnych.append(grupa)

    _6_5b[rok] = grup_nie_roznorodnych
    print(rok, len(grup_nie_roznorodnych), sep='\t')

_6_5b = sorted(_6_5b.items(), key=lambda x: len(x[1]), reverse=True)
rok2 = _6_5b[0][0]
grupy_id2 = _6_5b[0][1]
grupy_nazwy2 = [grupy[idd][0] for idd in grupy_id2]
print(rok2, *grupy_nazwy2, sep='\t')

oglos_nastepne()
for id_zawodnika, [imie, nazwisko, data] in zawodnicy.items():
    panstwa = []
    for id_startu, [rok, id_zawodnika_2, kod_grupy, obywatel_kraju] in startujacy.items():
        if id_zawodnika_2 == id_zawodnika:
            panstwa.append(obywatel_kraju)
    panstwa = list(set(panstwa))

    if len(panstwa) > 1:
        print(f"{imie} {nazwisko} -", ', '.join(panstwa))

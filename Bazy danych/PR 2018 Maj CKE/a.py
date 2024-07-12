import datetime
import sys

sys.stdout = open('wyniki6.txt', 'w', encoding='UTF-8')

zadanko = 1
def nastepne():
    global zadanko
    if zadanko != 1:
        print()
    print(f'Zadanie 6.{zadanko}.')
    zadanko += 1

def datetime_creator(x):
    [date, time] = x.strip().split(' ')
    [year, month, day] = [int(y) for y in date.split('-')]
    [hour, minute, second] = [int(y) for y in time.split(':')]
    return datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second)

def datetime_format(x: datetime.datetime):
    return f"{str(x.day).zfill(2)}.{str(x.month).zfill(2)}.{str(x.year).zfill(4)}r. {str(x.hour).zfill(2)}:{str(x.minute).zfill(2)}:{str(x.second).zfill(2)}"

komputery = {}
awarie = {}
naprawy = {}

with open('DANE/komputery.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split('\t')
        komputery[int(line[0])] = [line[1], int(line[2])]

with open('DANE/awarie.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split('\t')
        awarie[int(line[0])] = [int(line[1]), datetime_creator(line[2]), int(line[3])]

with open('DANE/naprawy.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split('\t')
        line[0] = int(line[0])
        if line[0] not in naprawy.keys():
            naprawy[line[0]] = []
        naprawy[line[0]].append([datetime_creator(line[1]), line[2]])

_6_1 = {}
for numer_komputera, [sekcja, pojemnosc_dysku] in komputery.items():
    if pojemnosc_dysku not in _6_1.keys():
        _6_1[pojemnosc_dysku] = 0
    _6_1[pojemnosc_dysku] += 1

nastepne()
_6_1 = sorted(_6_1.items(), key=lambda _: (_[1], _[0]), reverse=True)
print("Pojemność;Ilość komputerów")
for x in _6_1[:10]:
    print(*x, sep=';')

_6_2 = {}
for numer_komputera, [sekcja, pojemnosc_dysku] in komputery.items():
    if sekcja == 'A':
        wymiany = 0
        for numer_zgloszenia, lista_napraw in naprawy.items():
            for [czas_naprawy, rodzaj] in lista_napraw:
                numer_komputera_2 = awarie[numer_zgloszenia][0]
                if numer_komputera_2 == numer_komputera and rodzaj == 'wymiana':
                    wymiany += 1

        _6_2[numer_komputera] = wymiany

nastepne()
_6_2 = sorted(_6_2.items(), key=lambda x: (x[1], x[0]), reverse=True)
print('Numer komputera;Wymiany podzespołów')
for x in _6_2:
    if x[1] >= 10:
        print(*x, sep=';')

komputery_sekcji = {}
for numer_komputera, [sekcja, pojemnosc_dysku] in komputery.items():
    if sekcja not in komputery_sekcji.keys():
        komputery_sekcji[sekcja] = []
    komputery_sekcji[sekcja].append(numer_komputera)

nastepne()
dzien_skan = datetime.datetime(year=2015, month=1, day=1, hour=23, minute=59, second=59)
while dzien_skan <= datetime.datetime(year=2015, month=12, day=31, hour=23, minute=59, second=59):
    awarie_dnia = []
    for numer_zgloszenia, [numer_komputera, czas_awarii, priorytet] in awarie.items():
        if czas_awarii > dzien_skan:
            break
        if czas_awarii.year == dzien_skan.year and czas_awarii.day == dzien_skan.day and czas_awarii.month == dzien_skan.month:
            awarie_dnia.append(numer_komputera)
    awarie_dnia = list(set(awarie_dnia))

    for sekcja, jej_komputery in komputery_sekcji.items():
        pasuje = True
        for element in list(set(jej_komputery)):
            if element not in awarie_dnia:
                pasuje = False
        if pasuje:
            print('Sekcja', sekcja, '-', f"{dzien_skan.day}.{dzien_skan.month}.{dzien_skan.year}r.")
            dzien_skan = datetime.datetime(year=2017, month=1, day=1)
            break

    dzien_skan += datetime.timedelta(hours=24)

nastepne()
_6_4 = []
for numer_zgloszenia, [numer_komputera, czas_awarii, priorytet] in awarie.items():
    daty_napraw = [x[0] for x in naprawy[numer_zgloszenia]]
    najpozniejsza_naprawa = max(daty_napraw)
    zajelo = najpozniejsza_naprawa - czas_awarii

    if _6_4 == [] or zajelo > _6_4[3]:
        _6_4 = [numer_zgloszenia, czas_awarii, najpozniejsza_naprawa, zajelo]

print("Numer zgłoszenia:", _6_4[0])
print("Czas wystąpienia awarii:", datetime_format(_6_4[1]))
print("Czas zakończenia ostatniej naprawy:", datetime_format(_6_4[2]))

nastepne()
_6_5 = 0
for numer_komputera, [sekcja, pojemnosc_dysku] in komputery.items():
    znaleziono_osemke = False
    for numer_zgloszenia, [numer_komputera_2, czas_awarii, priorytet] in awarie.items():
        if numer_komputera == numer_komputera_2 and priorytet >= 8:
            znaleziono_osemke = True

    if not znaleziono_osemke:
        _6_5 += 1
print(_6_5)
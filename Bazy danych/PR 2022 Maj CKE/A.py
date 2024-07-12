from collections import defaultdict
import datetime

def data(x: str) -> datetime.datetime:
    [year, month, day] = [int(y) for y in x.strip().split(' ')[0].split('-')]
    [hour, minute, second] = [int(y) for y in x.strip().split(' ')[1].split(':')]
    return datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second)

def main():
    klasa = {}
    uczen = {}
    ewidencja = {}

    with open('DANE/klasa.txt') as f:
        for line in f.readlines()[1:]:
            line = line.strip().split(';')
            klasa[line[0]] = line[1]

    with open('DANE/uczen.txt') as f:
        for line in f.readlines()[1:]:
            line = line.strip().split(';')
            uczen[int(line[0])] = line[1:]

    with open('DANE/ewidencja.txt') as f:
        for line in f.readlines()[1:]:
            line = line.strip().split(';')
            line[0] = int(line[0])
            line[1] = int(line[1])
            line[2] = data(line[2])
            line[3] = data(line[3])
            ewidencja[line[0]] = line[1:]

    _6_1 = 0
    for idewidencji, [iducznia, wejscie, wyjscie] in ewidencja.items():
        imie = uczen[iducznia][0]
        klasa_id = uczen[iducznia][2]
        klasa_nazwa = klasa[klasa_id]

        if imie[-1] == 'a' and klasa_nazwa == 'biologiczno-chemiczny':
            _6_1 += 1
    # print(_6_1)

    _6_2 = defaultdict(int)
    for idewidencji, [iducznia, wejscie, wyjscie] in ewidencja.items():
        if wejscie <= datetime.datetime(wejscie.year, wejscie.month, wejscie.day, 8, 0, 0):
            data_tekst = f"{wejscie.year}-{str(wejscie.month).zfill(2)}-{str(wejscie.day).zfill(2)}"
            _6_2[data_tekst] += 1

    for x, y in _6_2.items():
        # print(x, y)
        ''

    _6_3 = defaultdict(datetime.timedelta)
    for idewidencji, [iducznia, wejscie, wyjscie] in ewidencja.items():
        _6_3[iducznia] += wyjscie - wejscie

    _6_3 = sorted(_6_3.items(), key=lambda x: x[1], reverse=True)
    for i in range(3):
        i_osoba = _6_3[i][0]
        # print(i_osoba, uczen[i_osoba][0], uczen[i_osoba][1])

    for iducznia, [imie, nazwisko, idklasy] in uczen.items():
        obecnosc = False
        for idewidencji, [iducznia2, wejscie, wyjscie] in ewidencja.items():
            if iducznia2 == iducznia and wejscie.year == 2022 and wejscie.month == 4 and wejscie.day == 6:
                obecnosc = True
                break
        if not obecnosc:
            ''
            # print(imie, nazwisko)

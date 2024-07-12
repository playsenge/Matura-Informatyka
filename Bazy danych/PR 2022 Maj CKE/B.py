import datetime

def main():
    klasa = {}
    uczen = {}
    ewidencja = []

    with open('DANE/klasa.txt') as f:
        tablica = [x.strip().split(';') for x in f.readlines()][1:]
        for element in tablica:
            klasa[element[0]] = element[1]
    with open('DANE/uczen.txt') as f:
        tablica = [x.strip().split(';') for x in f.readlines()][1:]
        for element in tablica:
            element[0] = int(element[0])
        for element in tablica:
            uczen[element[0]] = [element[1], element[2], element[3]]
    with open('DANE/ewidencja.txt') as f:
        ewidencja = [x.strip().split(';') for x in f.readlines()][1:]
        for element in ewidencja:
            element[0] = int(element[0])
            element[1] = int(element[1])

            [year, month, day] = element[2].split(" ")[0].split("-")
            [hour, minute, second] = element[2].split(" ")[1].split(":")
            year, month, day, hour, minute, second = int(year), int(month), int(day), int(hour), int(minute), int(second)

            element[2] = datetime.datetime(year, month, day, hour, minute, second)

            [year, month, day] = element[3].split(" ")[0].split("-")
            [hour, minute, second] = element[3].split(" ")[1].split(":")
            year, month, day, hour, minute, second = int(year), int(month), int(day), int(hour), int(minute), int(second)

            element[3] = datetime.datetime(year, month, day, hour, minute, second)

    _6_1 = 0

    for wpis in ewidencja:
        [id_ewidencji, id_ucznia, wejscie, wyjscie] = wpis
        znaleziony_uczen = uczen[id_ucznia]
        klasa_ucznia = klasa[znaleziony_uczen[2]]
        czy_dziewczyna = znaleziony_uczen[0][-1] == 'a'

        if czy_dziewczyna and klasa_ucznia == 'biologiczno-chemiczny':
            _6_1 += 1

    # print(_6_1)

    dni = []
    for wpis in ewidencja:
        data = wpis[2]
        year, month, day = data.year, data.month, data.day
        data = '.'.join([str(day).zfill(2), str(month).zfill(2), str(year).zfill(4)])
        if data not in dni:
            dni.append(data)

    _6_2 = {}
    for dzien in dni:
        _6_2[dzien] = 0

    for wpis in ewidencja:
        data = wpis[2]
        year, month, day, hour, minute, second = data.year, data.month, data.day, data.hour, data.minute, data.second
        data = '.'.join([str(day).zfill(2), str(month).zfill(2), str(year).zfill(4)])
        czas = hour * 3600 + minute * 60 + second

        if czas <= (8 * 3600):
            _6_2[data] += 1

    for x, y in _6_2.items():
        # print(x, y)
        ''

    pobyt_osob = {}
    for osoba in uczen.keys():
        pobyt_osob[osoba] = 0

    for wpis in ewidencja:
        pobyt: datetime.timedelta = wpis[3] - wpis[2]
        pobyt_osob[wpis[1]] += pobyt.total_seconds()

    pobyt_osob = sorted(pobyt_osob.items(), key=lambda x: x[1], reverse=True)
    for i in range(3):
        id = pobyt_osob[i][0]
        [imie, nazwisko, klasa] = uczen[id]
        # print(id, imie, nazwisko)

    uczniowie_obecni = []
    for wpis in ewidencja:
        data = wpis[2]
        year, month, day, hour, minute, second = data.year, data.month, data.day, data.hour, data.minute, data.second
        data = '-'.join([str(year), str(month), str(day)])

        if data == '2022-4-6':
            uczniowie_obecni.append(wpis[1])

    for i, osoba in uczen.items():
        if i not in uczniowie_obecni:
            ''
            # print(osoba[0], osoba[1])

from collections import defaultdict
import datetime

def main():
    klasa = {}
    uczen = {}
    ewidencja = []

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
            id_ewidencji = int(line[0])
            id_ucznia = int(line[1])
            wejscie = datetime.datetime.strptime(line[2], '%Y-%m-%d %H:%M:%S')
            wyjscie = datetime.datetime.strptime(line[3], '%Y-%m-%d %H:%M:%S')
            ewidencja.append([id_ewidencji, id_ucznia, wejscie, wyjscie])

    # First task
    _6_1 = sum(
        1 for _, id_ucznia, _, _ in ewidencja
        if uczen[id_ucznia][0].endswith('a') and klasa[uczen[id_ucznia][2]] == 'biologiczno-chemiczny'
    )
    '' #_6_1)

    # Second task
    _6_2 = defaultdict(int)
    for _, _, wejscie, _ in ewidencja:
        if wejscie.hour < 8 or (wejscie.hour == 8 and wejscie.minute == 0):
            data_tekst = f"{wejscie.year}-{str(wejscie.month).zfill(2)}-{str(wejscie.day).zfill(2)}"
            _6_2[data_tekst] += 1

    for x, y in _6_2.items():
        '' #x, y)

    # Third task
    _6_3 = defaultdict(datetime.timedelta)
    for _, id_ucznia, wejscie, wyjscie in ewidencja:
        _6_3[id_ucznia] += wyjscie - wejscie

    _6_3_sorted = sorted(_6_3.items(), key=lambda x: x[1], reverse=True)
    for i in range(3):
        i_osoba = _6_3_sorted[i][0]
        '' #i_osoba, uczen[i_osoba][0], uczen[i_osoba][1])

    # Fourth task
    uczniowie_obecni = set()
    for _, id_ucznia, wejscie, _ in ewidencja:
        if wejscie.year == 2022 and wejscie.month == 4 and wejscie.day == 6:
            uczniowie_obecni.add(id_ucznia)

    for id_ucznia, (imie, nazwisko, _) in uczen.items():
        if id_ucznia not in uczniowie_obecni:
            '' #imie, nazwisko)

if __name__ == "__main__":
    main()

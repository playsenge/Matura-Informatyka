from collections import defaultdict
import datetime

def main():
    klasa = {}
    uczen = {}
    ewidencja = []

    # Load klasa.txt
    with open('DANE/klasa.txt') as f:
        for line in f.readlines()[1:]:
            class_id, class_name = line.strip().split(';')
            klasa[class_id] = class_name

    # Load uczen.txt
    with open('DANE/uczen.txt') as f:
        for line in f.readlines()[1:]:
            data = line.strip().split(';')
            uczen[int(data[0])] = data[1:]

    # Load ewidencja.txt
    with open('DANE/ewidencja.txt') as f:
        for line in f.readlines()[1:]:
            data = line.strip().split(';')
            id_ewidencji = int(data[0])
            id_ucznia = int(data[1])
            wejscie = datetime.datetime(int(data[2][:4]), int(data[2][5:7]), int(data[2][8:10]),
                                        int(data[2][11:13]), int(data[2][14:16]), int(data[2][17:19]))
            wyjscie = datetime.datetime(int(data[3][:4]), int(data[3][5:7]), int(data[3][8:10]),
                                        int(data[3][11:13]), int(data[3][14:16]), int(data[3][17:19]))
            ewidencja.append((id_ewidencji, id_ucznia, wejscie, wyjscie))

    # Task 1
    _6_1 = sum(
        1 for _, id_ucznia, _, _ in ewidencja
        if uczen[id_ucznia][0].endswith('a') and klasa[uczen[id_ucznia][2]] == 'biologiczno-chemiczny'
    )
    '' #_6_1)

    # Task 2
    _6_2 = defaultdict(int)
    for _, _, wejscie, _ in ewidencja:
        if wejscie.hour < 8 or (wejscie.hour == 8 and wejscie.minute == 0):
            date_text = f"{wejscie.year}-{wejscie.month:02}-{wejscie.day:02}"
            _6_2[date_text] += 1

    for date_text, count in _6_2.items():
        '' #date_text, count)

    # Task 3
    _6_3 = defaultdict(datetime.timedelta)
    for _, id_ucznia, wejscie, wyjscie in ewidencja:
        _6_3[id_ucznia] += wyjscie - wejscie

    _6_3_sorted = sorted(_6_3.items(), key=lambda x: x[1], reverse=True)
    for i in range(3):
        i_osoba = _6_3_sorted[i][0]
        '' #i_osoba, uczen[i_osoba][0], uczen[i_osoba][1])

    # Task 4
    present_students = set()
    for _, id_ucznia, wejscie, _ in ewidencja:
        if wejscie.year == 2022 and wejscie.month == 4 and wejscie.day == 6:
            present_students.add(id_ucznia)

    for id_ucznia, (imie, nazwisko, _) in uczen.items():
        if id_ucznia not in present_students:
            '' #imie, nazwisko)

if __name__ == "__main__":
    main()

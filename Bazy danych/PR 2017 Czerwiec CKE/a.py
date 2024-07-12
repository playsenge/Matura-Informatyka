import sys

sys.stdout = open('wyniki6.txt', 'w', encoding='UTF-8')

zadanie_obecne = 1
def kolejne():
    global zadanie_obecne
    if zadanie_obecne != 1:
        print()
    print(f"{'=' * 5} Zadanie 6.{zadanie_obecne}. {'=' * 5}")
    zadanie_obecne += 1

programy = {}
pakiety = {}
zestawy = {}

with open('DANE/programy.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split('\t')
        line[0] = int(line[0])
        line[3] = int(line[3])
        programy[line[0]] = line[1:]

with open('DANE/pakiety.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split('\t')
        line[0] = int(line[0])
        pakiety[line[0]] = line[1:]

with open('DANE/zestawy.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split('\t')
        line[0] = int(line[0])
        line[1] = int(line[1])
        if line[0] not in zestawy.keys():
            zestawy[line[0]] = []
        zestawy[line[0]].append(line[1])

_6_1 = {}
for zestaw, zawartosc in zestawy.items():
    for program in zawartosc:
        program_info = programy[program]
        program_kategoria = program_info[1]
        if program_kategoria == 'edytor dokumentow tekstowych':
            if program not in _6_1.keys():
                _6_1[program] = 0
            _6_1[program] += 1

kolejne()
_6_1 = _6_1.items()
for x in _6_1:
    program = x[0]
    ilosc = x[1]
    if ilosc >= 2:
        program_info = programy[program]
        print(program_info[0], program_info[2], ilosc)

kolejne()
for id_pakietu, [nazwa_pakietu, firma] in pakiety.items():
    zawiera = False
    for program in zestawy[id_pakietu]:
        program_info = programy[program]
        if 'zarzadzanie' in program_info[1]:
            zawiera = True
            break
    if zawiera:
        print(nazwa_pakietu)

kolejne()
_6_3 = {}
for id_pakietu, [nazwa_pakietu, firma] in pakiety.items():
    wartosc = 0
    for program in zestawy[id_pakietu]:
        program_info = programy[program]
        wartosc += program_info[2]
    _6_3[id_pakietu] = wartosc
_6_3 = sorted(_6_3.items(), key=lambda x: (x[1], x[0]), reverse=True)
for x in _6_3[:3]:
    print(*pakiety[x[0]], x[1])

kolejne()
for id_programu, [program, rodzaj, cena] in programy.items():
    znaleziono = False
    for id_pakietu, [nazwa_pakietu, firma] in pakiety.items():
        if id_programu in zestawy[id_pakietu]:
            znaleziono = True
            break
    if not znaleziono:
        print(program)

kolejne()
for id_pakietu, [nazwa_pakietu, firma] in pakiety.items():
    zawarte_programy = zestawy[id_pakietu]
    komercyjne = 0
    darmowe = 0

    for id_programu in zawarte_programy:
        if programy[id_programu][2] == 0:
            darmowe += 1
        else:
            komercyjne += 1

    if komercyjne > 0 and darmowe > 0:
        print(nazwa_pakietu, komercyjne, darmowe)
gry = []
gracze = []
oceny = []

with open("DANE/gry.txt") as f:
    gry = [x.strip().split("\t") for x in f.readlines()]
with open("DANE/gracze.txt") as f:
    gracze = [x.strip().split("\t") for x in f.readlines()]
with open("DANE/oceny.txt") as f:
    oceny = [x.strip().split("\t") for x in f.readlines()]

gry = gry[1:]
gracze = gracze[1:]
oceny = oceny[1:]

_7_1 = {}
_7_2 = {}

for gra in gry:
    licznik = 0
    oceny_s = 0
    for ocena in oceny:
        if ocena[0] == gra[0]:
            licznik += 1
            oceny_s += float(ocena[3])

    _7_1[gra[1]] = licznik
    if gra[2] == 'imprezowa':
        _7_2[gra[1]] = oceny_s / licznik

print("Zadanie 7.1.")
print(list(_7_1.keys())[list(_7_1.values()).index(max(_7_1.values()))])
print()

print("Zadanie 7.2.")
for i,j in _7_2.items():
    print(i, round(j, 2))
print()

_7_3 = 0
for gracz in gracze:
    gracz_zalicza = 0
    gracz_zalicza_2 = 0
    [id, imie, nazwisko, wiek] = gracz
    for ocena in oceny:
        [id_gry, id_gracza, stan, stopien] = ocena
        if id_gracza == id:
            gracz_zalicza += 1
            if stan != 'posiada':
                gracz_zalicza_2 += 1

    if gracz_zalicza == gracz_zalicza_2 and gracz_zalicza >= 1:
        _7_3 += 1

print("Zadanie 7.3.")
print(_7_3)
print()

oceny_juniorow = {}
oceny_seniorow = {}
oceny_weteran = {}

for gra in gry:
    for x in [oceny_juniorow, oceny_seniorow, oceny_weteran]:
        x[gra[1]] = 0

for ocena in oceny:
    [id_gry, id_gracza, stan, stopien] = ocena
    znaleziony_gracz = []
    for gracz in gracze:
        if gracz[0] == id_gracza:
            znaleziony_gracz = gracz
            break

    znaleziona_gra = []
    for gra in gry:
        if gra[0] == id_gry:
            znaleziona_gra = gra
            break

    [id_gracza, imie, nazwisko, wiek] = gracz
    [id_gry, nazwa, kategoria] = gra

    wiek = int(wiek)

    if wiek <= 19: # Junior
        oceny_juniorow[nazwa] += 1
    elif wiek <= 49:
        oceny_seniorow[nazwa] += 1
    else:
        oceny_weteran[nazwa] += 1

max_juniorzy = max(oceny_juniorow.values())
max_seniorzy = max(oceny_seniorow.values())
max_weteranie = max(oceny_weteran.values())

print("Zadanie 7.4.")

print()
print("Juniorzy:")
for element, wartosc in oceny_juniorow.items():
    if wartosc == max_juniorzy:
        print(element, wartosc)
print()

print("Seniorzy:")
for element, wartosc in oceny_seniorow.items():
    if wartosc == max_seniorzy:
        print(element, wartosc)
print()

print("Weteranie:")
for element, wartosc in oceny_weteran.items():
    if wartosc == max_weteranie:
        print(element, wartosc)
print()
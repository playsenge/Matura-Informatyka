pracownicy = {}
dzieci = []
zatrudnienie = []

with open('DANE/pracownik.txt', 'r') as f:
    for line in f.readlines()[1:]:
        tablica = line.strip().split(";")
        pracownicy[str(tablica[0])] = [tablica[1], tablica[2], tablica[3]]

with open('DANE/dziecko.txt', 'r') as f:
    for line in f.readlines()[1:]:
        tablica = line.strip().split(";")
        dzieci.append(tablica)

with open('DANE/zatrudnienie.txt', 'r') as f:
    for line in f.readlines()[1:]:
        tablica = line.strip().split(";")
        zatrudnienie.append(tablica)

_6_1 = {}

for zat in zatrudnienie:
    [pesel, rodzaj_umowy, kwota_wyn, data] = zat

    if rodzaj_umowy not in _6_1.keys():
        _6_1[rodzaj_umowy] = 0

    _6_1[rodzaj_umowy] += 1

print(_6_1)

_6_2 = {}

for zat in zatrudnienie:
    if zat[0] not in _6_2:
        _6_2[zat[0]] = 0

    _6_2[zat[0]] += 1

_6_2y = []
for i, j in _6_2.items():
    _6_2y.append([i, j])

_6_2y = sorted(_6_2y, key=lambda x: x[1], reverse=True)

print(pracownicy[_6_2y[0][0]][1], pracownicy[_6_2y[0][0]][0])

_6_3 = {}
_6_4 = {}

for pesel, dane in pracownicy.items():
    [nazwisko, imie, stan_rodzinny] = dane

    ile_dzieci = 0
    wychowuje_samotnie = 0
    for dziecko in dzieci:
        [pesel_rodzica, pesel_dziecka, imie_dziecka, nauka] = dziecko
        if pesel_rodzica == pesel:
            # print([pesel, *dane], dziecko)
            if stan_rodzinny == 'S':
                wychowuje_samotnie += 1
            ile_dzieci += 1

    _6_3[pesel] = wychowuje_samotnie
    _6_4[pesel] = ile_dzieci

_6_3y = []
for i, j in _6_3.items():
    _6_3y.append([i, j])

_6_3y = sorted(_6_3y, key=lambda x: x[1], reverse=True)
print(pracownicy[_6_3y[0][0]][1], pracownicy[_6_3y[0][0]][0])

_6_4y = []
for i, j in _6_4.items():
    if j == 0:
        _6_4y.append([pracownicy[i][1], pracownicy[i][0]])


def asciified(x):
    x = x.lower()
    a = 'aąbcćdeęfghijklłmnoóprqstuvwxyzżź'
    res = ''
    for ch in x:
        res += chr(a.index(ch))
    return res


_6_4y = sorted(_6_4y, key=lambda x: asciified(x[1]))
for i in _6_4y:
    print(*i)

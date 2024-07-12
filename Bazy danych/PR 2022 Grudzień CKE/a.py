import datetime

klienci = {}
pokoje = {}
noclegi = {}


def data(tekst):
    tekst = [int(x) for x in tekst.split("-")]
    return datetime.date(tekst[0], tekst[1], tekst[2])


with open('DANE/klienci.txt') as f:
    for x in f.readlines()[1:]:
        elementy = x.strip().split()
        klienci[elementy[0]] = elementy[1:]

with open('DANE/pokoje.txt') as f:
    for x in f.readlines()[1:]:
        elementy = x.strip().split()
        pokoje[int(elementy[0])] = [elementy[1], int(elementy[2])]

with open('DANE/noclegi.txt') as f:
    for x in f.readlines()[1:]:
        elementy = x.strip().split()
        noclegi[int(elementy[0])] = [data(elementy[1]), data(elementy[2]), elementy[3], int(elementy[4])]


_5_1 = {}
_5_2 = {}

for id_pobytu, [data_przyjazdu, data_wyjazdu, nr_dowodu, nr_pokoju] in noclegi.items():
    if nr_dowodu not in _5_1.keys():
        _5_1[nr_dowodu] = 0
    if nr_dowodu not in _5_2.keys():
        _5_2[nr_dowodu] = 0

    dni = (data_wyjazdu - data_przyjazdu).days
    _5_1[nr_dowodu] += dni
    _5_2[nr_dowodu] += pokoje[nr_pokoju][1] * dni

_5_1 = sorted(_5_1.items(), key=lambda x: x[1], reverse=True)[0]
print(klienci[_5_1[0]][1], klienci[_5_1[0]][0], _5_1[1])

for nr_dowodu, koszt in _5_2.items():
    if koszt > 2000:
        print(klienci[nr_dowodu][1], klienci[nr_dowodu][0])

for nr_pokoju, [standard, cena] in pokoje.items():
    if standard == 'N':
        pobyty = 0

        for id_pobytu, [data_przyjazdu, data_wyjazdu, nr_dowodu, nr_pokoju_2] in noclegi.items():
            if nr_pokoju == nr_pokoju_2:
                miasto = klienci[nr_dowodu][2]
                if miasto == "Opole" or miasto == "Katowice":
                    if data_przyjazdu >= data('2022-07-01') and data_wyjazdu <= data('2022-09-30'):
                        pobyty += 1

        if pobyty == 0:
            print(nr_pokoju)

# SELECT rodzaj, Count(*)
# FROM uslugi_dodatkowe
# GROUP BY rodzaj;

# SELECT Klienci.imie, Klienci.nazwisko, Sum(uslugi_dodatkowe.cena_uslugi)
# FROM ((Klienci INNER JOIN Noclegi ON Klienci.nr_dowodu = Noclegi.nr_dowodu) INNER JOIN Pokoje ON Noclegi.nr_pokoju = Pokoje.nr_pokoju) INNER JOIN uslugi_dodatkowe ON Noclegi.id_pobytu = uslugi_dodatkowe.id_pobytu
# GROUP BY Klienci.imie, Klienci.nazwisko, Noclegi.id_pobytu;

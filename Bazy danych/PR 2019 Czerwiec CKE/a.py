import datetime

agenci = {}
oferty = {}
klienci = {}
zainteresowanie = []

def data(x):
    x = [int(y) for y in x.split('-')]
    return datetime.date(x[0], x[1], x[2])

with open('DANE/agenci.txt') as f:
    for x in f.readlines()[1:]:
        tablica = x.strip().split('\t')
        agenci[int(tablica[0])] = [tablica[1].strip(), tablica[2].strip()]

with open('DANE/oferty.txt', encoding='WINDOWS-1250') as f:
    for x in f.readlines()[1:]:
        tablica = x.strip().split()
        #print(tablica)
        oferty[tablica[0]] = [tablica[1], tablica[2], int(tablica[3]), int(tablica[4]), int(tablica[5]), int(tablica[6]), data(tablica[7]), int(tablica[8])]

with open('DANE/klienci.txt') as f:
    for x in f.readlines()[1:]:
        tablica = x.strip().split()
        klienci[int(tablica[0])] = tablica[1:]

with open('DANE/zainteresowanie.txt') as f:
    for x in f.readlines()[1:]:
        tablica = x.strip().split()
        zainteresowanie.append([tablica[0], int(tablica[1])])

_6_1 = {}

for zain in zainteresowanie:
    [oferta, klient] = zain
    if oferta not in _6_1.keys():
        _6_1[oferta] = 0
    _6_1[oferta] += 1

_6_1 = sorted(_6_1.items(), key=lambda x: x[1], reverse=True)
_6_1_oferta = _6_1[0][0]
_6_1_id = oferty[_6_1_oferta][7]
_6_1_imie = agenci[_6_1_id][0]
_6_1_nazwisko = agenci[_6_1_id][1]
print('Zadanie 6.1.')
print('Id Oferty\tImie\tNazwisko')
print(_6_1_oferta, _6_1_imie, _6_1_nazwisko, sep='\t')

_6_2 = {}

for id_oferty, [wojewodztwo, status, powierzchnia, pokoje, lazienki, cena, data_zgloszenia, id_agenta] in oferty.items():
    if wojewodztwo not in _6_2.keys():
     _6_2[wojewodztwo] = []

    _6_2[wojewodztwo].append(cena)

for i, j in _6_2.items():
    _6_2[i] = sum(j)/len(j)

print('\nZadanie 6.2.')
print('Wojewodztwo\tSredni koszt')
_6_2 = sorted(_6_2.items(), key=lambda x: x[0])
for i in _6_2:
    print(i[0], str("{:.2f}".format(round(i[1], 2))).replace('.',',')+"zł", sep='\t')

print('\nZadanie 6.3.')
print('Imię\tNazwisko\tId Oferty\tWojewodztwo\tPowierzchnia\tCena')
for id_oferty, [wojewodztwo, status, powierzchnia, pokoje, lazienki, cena, data_zgloszenia, id_agenta] in oferty.items():
    basen = id_oferty[-1] == 'T'
    mieszkanie = id_oferty[-2] == 'M'
    if basen and mieszkanie and status == "A":
        print(*agenci[id_agenta], id_oferty, wojewodztwo, powierzchnia, cena, sep="\t")

print('\nZadanie 6.4.')
print('Imię\tNazwisko')
for id_agenta, [imie, nazwisko] in agenci.items():
    sprzedane = 0
    for id_oferty, [wojewodztwo, status, powierzchnia, pokoje, lazienki, cena, data_zgloszenia, id_agenta_m] in oferty.items():
        if id_agenta_m == id_agenta and data_zgloszenia.year == 2017:
            if status == 'S':
                sprzedane += 1
    if sprzedane == 0:
        print(imie, nazwisko, sep='\t')

print('\nZadanie 6.5.')
print('Id Oferty\tPowierzchnia\tIlosc pokoi\tIlosc lazienek\tCena\tImie\tNazwisko')
for id_oferty, [wojewodztwo, status, powierzchnia, pokoje, lazienki, cena, data_zgloszenia, id_agenta] in oferty.items():
    if status == 'A' and powierzchnia > 180 and lazienki >= 2:
        print(id_oferty, powierzchnia, pokoje, lazienki, cena, *agenci[id_agenta], sep='\t')
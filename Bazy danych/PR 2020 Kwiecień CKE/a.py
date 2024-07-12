import datetime, math

def data_generuj(x):
    x = [int(y) for y in x.strip().split('-')]
    return datetime.date(*x)

def data_odwroc(x: datetime.date):
    return str(x.year) + '-' + str(x.month).zfill(2) + '-' + str(x.day).zfill(2)

klienci = {}
zabiegi = {}

with open('DANE/klienci.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split('\t')
        klienci[line[0]] = [line[1], line[2]]

with open('DANE/zabiegi.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split('\t')
        zabiegi[line[0]] = [line[1], line[2], int(line[3])]

wizyty = {}
with open('DANE/wizytydane.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split('\t')
        wizyty[int(line[0])] = [data_generuj(line[1]), int(line[2]), line[3], []]
with open('DANE/wizytyzabiegi.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split('\t')
        wizyty[int(line[0])][3].append(line[1])

alicja_kowalska_id = ''
for id_klienta, [imie, nazwisko] in klienci.items():
    if imie == 'Alicja' and nazwisko == 'Kowalska':
        alicja_kowalska_id = id_klienta
        break

_6_1 = 0
for id_wizyty, [data, nr_wizyty, id_klienta, kody_zabiegu] in wizyty.items():
    if id_klienta == alicja_kowalska_id:
        for kod in kody_zabiegu:
            _6_1 += zabiegi[kod][2]

print('Zadanie 6.1.')
print(_6_1)

print()
print('Zadanie 6.2.')
_6_2 = {}
for id_wizyty, [data, nr_wizyty, id_klienta, kody_zabiegu] in wizyty.items():
    for id_klienta_2, [imie, nazwisko] in klienci.items():
        if id_klienta_2 == id_klienta:
            if id_klienta not in _6_2.keys():
                _6_2[id_klienta] = 0
            _6_2[id_klienta] += 1
_6_2 = sorted(_6_2.items(), key=lambda x: x[1], reverse=True)
print(*klienci[_6_2[0][0]], _6_2[0][1])

magia_hawajow_kod = ''
for kod_zabiegu, [dzial, zabieg, cena] in zabiegi.items():
    if zabieg == 'Magia Hawajow':
        magia_hawajow_kod = kod_zabiegu
        break

_6_3_liczba = 0
_6_3_daty = []
for id_wizyty, [data, nr_wizyty, id_klienta, kody_zabiegu] in wizyty.items():
    if magia_hawajow_kod in kody_zabiegu:
        _6_3_liczba += 1
        if data not in _6_3_daty:
            _6_3_daty.append(data)

print()
print('Zadanie 6.3.')
print('Wizyty:', _6_3_liczba)
print('Daty:')
_6_3_daty = sorted(_6_3_daty, reverse=True)
for data in _6_3_daty:
    print(data_odwroc(data))

_6_4_liczba = []
_6_4_koszt = []
for id_wizyty, [data, nr_wizyty, id_klienta, kody_zabiegu] in wizyty.items():
    if id_klienta[0] == 'X': # kobiety, wykluczane osoby niebinarne, cringe
        if data_generuj('2017-12-6') <= data <= data_generuj('2018-1-15'):
            for makijaz in kody_zabiegu:
                if 'Makijaz' in zabiegi[makijaz][1]:
                    _6_4_liczba.append(id_klienta)
                    _6_4_koszt.append(zabiegi[makijaz][2] * 0.8)

print()
print('Zadanie 6.4.')
print('Kobiety, które skorzystały z promocji:', len(set(_6_4_liczba)))
print('Łączny koszt zapłaty kobiet:', "{:.2f}".format(math.fsum(_6_4_koszt)), "zł")

print()
print('Zadanie 6.5.')
for kod_zabiegu, [dzial, zabieg, cena] in zabiegi.items():
    if dzial == 'FRYZJER MESKI':
        skorzystal = False
        for id_wizyty, [data, nr_wizyty, id_klienta, kody_zabiegu] in wizyty.items():
            if kod_zabiegu in kody_zabiegu:
                skorzystal = True
                break
        if not skorzystal:
            print(zabieg)
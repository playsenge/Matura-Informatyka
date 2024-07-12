osoby = {}
with open('DANE/dane_ankiet.txt') as plik:
    for line in plik.readlines()[1:]:
        tablica = line.strip().split('\t')
        tablica[0] = int(tablica[0])
        tablica[3] = int(tablica[3])
        tablica[5] = int(tablica[5])

        osoby[tablica[0]] = tablica[1:]

zainteresowania = {}
with open('DANE/zain.txt') as plik:
    for line in plik.readlines()[1:]:
        tablica = line.strip().split('\t')

        if int(tablica[0]) not in zainteresowania.keys():
            zainteresowania[int(tablica[0])] = []

        zainteresowania[int(tablica[0])].append(tablica[1])

lokomocja = {}
with open('DANE/lok.txt') as plik:
    for line in plik.readlines()[1:]:
        tablica = line.strip().split('\t')

        if int(tablica[0]) not in lokomocja.keys():
            lokomocja[int(tablica[0])] = []

        lokomocja[int(tablica[0])].append([tablica[1], tablica[2]])

kobiet = 0
mezczyzn = 0

for id, [nazwisko, imie, wiek, wyksztalcenie, dochod, wojewodztwo] in osoby.items():
    if imie[-1] == 'a':
        kobiet += 1
    else:
        mezczyzn += 1

print('Zadanie 6.1.')
print('Kobiet: ', kobiet)
print('Mezczyzn: ', mezczyzn)

_6_2 = {}

for id, tablica in lokomocja.items():
    osoba = osoby[id]
    if osoba[5] == 'Mazowieckie':
        for srodek, pora in tablica:
            if srodek not in _6_2.keys():
                _6_2[srodek] = 0

            if pora == 'lato':
                _6_2[srodek] += 1

print()
print('Zadanie 6.2.')
for x, y in _6_2.items():
    print(x, y)

_6_3 = {}

for id, [nazwisko, imie, wiek, wyksztalcenie, dochod, wojewodztwo] in osoby.items():
    if wojewodztwo not in _6_3.keys():
        _6_3[wojewodztwo] = 0

    _6_3[wojewodztwo] += 1

print()
print('Zadanie 6.3.')
for x, y in _6_3.items():
    if y > 20:
        print(x, y)

_6_4 = []

for id, [nazwisko, imie, wiek, wyksztalcenie, dochod, wojewodztwo] in osoby.items():
    if wiek > 50 and wyksztalcenie in ['wyzsze', 'srednie'] and 'informatyka' not in zainteresowania[id] and 'gry komputerowe' not in zainteresowania[id]:
        _6_4.append([imie, nazwisko, wojewodztwo])

_6_4 = sorted(_6_4, key=lambda x: x[1])
print()
print('Zadanie 6.4.')
for i in _6_4:
    print(*i)

_6_5 = []
for id, [nazwisko, imie, wiek, wyksztalcenie, dochod, wojewodztwo] in osoby.items():
    srodki = [x[0] for x in lokomocja[int(id)]]
    if imie[-1] == 'a' and wojewodztwo == 'Zachodniopomorskie' and 'rower' in srodki:
        _6_5.append(dochod)

print()
print('Zadanie 6.5.')
print(str(sum(_6_5) / len(_6_5)).replace('.',','))
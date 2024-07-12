from statistics import mean

studenci = {}
meldunek = {}
wypozyczenia = {}

with open('DANE/studenci.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split('\t')
        studenci[line[0]] = line[1:]

with open('DANE/meldunek.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split('\t')
        meldunek[line[0]] = int(line[1])

with open('DANE/wypozyczenia.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split('\t')
        wypozyczenia[int(line[0])] = line[1:]

_5_1 = {}
for lp, [pesel, tytul] in wypozyczenia.items():
    if pesel not in _5_1.keys():
        _5_1[pesel] = []
    _5_1[pesel].append(tytul)
_5_1 = sorted(_5_1.items(), key=lambda x: len(x[1]), reverse=True)[0]
print('Zadanie 5.1.')
print(*studenci[_5_1[0]][:2])
for x in _5_1[1]:
    print(x)

_5_2 = {}
for pesel, id_pok in meldunek.items():
    if id_pok not in _5_2.keys():
        _5_2[id_pok] = 0
    _5_2[id_pok] += 1

_5_2_ilosc = 0
_5_2_suma = 0
for i, j in _5_2.items():
    _5_2_ilosc += 1
    _5_2_suma += j

print('\nZadanie 5.2.')
print(round(_5_2_suma / _5_2_ilosc, 4))

print('\nZadanie 5.3.')
XX = 0
XY = 0
for pesel, [nazwisko, imie] in studenci.items():
    if int(pesel[-2]) % 2 == 0:
        XY += 1
    else:
        XX += 1
print(f"Kobiety: {XY}\nMezczyzni: {XX}")

print('\nZadanie 5.4.')
_5_4 = []
for pesel, [nazwisko, imie] in studenci.items():
    if pesel not in meldunek.keys():
        _5_4.append([nazwisko, imie])
_5_4 = sorted(_5_4, key=lambda x: x[0])
for x in _5_4:
    print(*x)

_5_5_pokoje_podreczniki = {}
for lp, [pesel, tytul] in wypozyczenia.items():
    if pesel in meldunek.keys():
        pokoj = meldunek[pesel]
    else:
        pokoj = 'gdzies indziej nie wiem gdzie i mam to gdzies'

    if pokoj not in _5_5_pokoje_podreczniki.keys():
        _5_5_pokoje_podreczniki[pokoj] = []
    _5_5_pokoje_podreczniki[pokoj].append(tytul)

_5_5_suma = 0
for y in _5_5_pokoje_podreczniki.values():
    _5_5_suma += len(set(y))
print('\nZadanie 5.5.')
print(_5_5_suma)
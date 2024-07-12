from collections import defaultdict

podpunkt = 1
def kolejny_podpunkt() -> None:
    global podpunkt
    if podpunkt != 1:
        print()
    print(f'Zadanie 6.{podpunkt}.')
    podpunkt += 1

dane_ankiet = {}
zain = defaultdict(list)
lok = defaultdict(list)

with open('DANE/dane_ankiet.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split('\t')
        line[0] = int(line[0])
        line[3] = int(line[3])
        line[5] = int(line[5])
        dane_ankiet[line[0]] = line[1:]

with open('DANE/zain.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split('\t')
        line[0] = int(line[0])
        zain[line[0]].append(line[1])

with open('DANE/lok.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip().split('\t')
        line[0] = int(line[0])
        lok[line[0]].append([line[1], line[2]])

kobiety = sum(x[1][-1] == 'a' for x in dane_ankiet.values())
mezczyzni = sum(x[1][-1] != 'a' for x in dane_ankiet.values())

kolejny_podpunkt()
print('Kobiety:', kobiety)
print('Mezczyzni:', mezczyzni)

kolejny_podpunkt()
_6_2 = defaultdict(int)
for id, x in lok.items():
    if dane_ankiet[id][5] == 'Mazowieckie':
        for [srod_lok, pora_roku] in x:
            if pora_roku == 'lato':
                _6_2[srod_lok] += 1

for x, y in _6_2.items():
    print(x, y)

kolejny_podpunkt()
_6_3 = defaultdict(int)
for id, [nazwisko, imie, wiek, wyksztalcenie, dochod, wojewodztwo] in dane_ankiet.items():
    _6_3[wojewodztwo] += 1

for x, y in _6_3.items():
    if y > 20:
        print(x, y)

kolejny_podpunkt()
_6_4 = {}
]
for id, [nazwisko, imie, wiek, wyksztalcenie, dochod, wojewodztwo] in dane_ankiet.items():
    if wiek > 50 and wyksztalcenie in ['wyzsze', 'srednie'] and 'informatyka' not in zain[
        id] and 'gry komputerowe' not in zain[id]:
        _6_4[id] = [imie, nazwisko, wojewodztwo
_6_4 = sorted(_6_4.values(), key=lambda x: x[1])
for y in _6_4:
    print(*y)

kolejny_podpunkt()
_6_5 = []
for id, [nazwisko, imie, wiek, wyksztalcenie, dochod, wojewodztwo] in dane_ankiet.items():
    if imie[-1] == 'a' and wojewodztwo == 'Zachodniopomorskie' and 'rower' in [x[0] for x in lok[id]]:
        _6_5.append(dochod)

print(sum(_6_5) / len(_6_5))

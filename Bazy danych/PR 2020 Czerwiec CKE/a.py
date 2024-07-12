panstwa = {}
jezyki = {}
uzytkownicy = []

with open('DANE/panstwa.txt') as f:
    for x in f.readlines()[1:]:
        tablica = x.strip().split('\t')
        panstwa[tablica[0]] = [tablica[1], float(tablica[2].replace(',','.'))]

with open('DANE/jezyki.txt') as f:
    for x in f.readlines()[1:]:
        tablica = x.strip().split('\t')
        jezyki[tablica[0]] = tablica[1]

with open('DANE/uzytkownicy.txt') as f:
    for x in f.readlines()[1:]:
        uzytkownicy.append(x.strip().split('\t'))
        uzytkownicy[len(uzytkownicy)-1][2] = float(uzytkownicy[len(uzytkownicy)-1][2].replace(',','.'))

rodziny = {}
for jezyk, rodzina in jezyki.items():
    if rodzina not in rodziny.keys():
        rodziny[rodzina] = 0

    rodziny[rodzina] += 1

rodziny = sorted(rodziny.items(), key=lambda x: x[1], reverse=True)
for rodzina in rodziny:
    print(*rodzina)

drugie = 0
for jezyk, rodzina in jezyki.items():
    uzywany = False

    for x in uzytkownicy:
        [xpanstwo, xjezyk, xuzytkownicy, xurzedowy] = x
        if xjezyk == jezyk and xurzedowy == 'tak':
            uzywany = True
            break

    if not uzywany:
        drugie += 1

print(drugie)

for jezyk, rodzina in jezyki.items():
    kontynenty = []

    for x in uzytkownicy:
        [xpanstwo, xjezyk, xuzytkownicy, xurzedowy] = x
        xkontynent = panstwa[xpanstwo][0]

        if jezyk == xjezyk:
            if xkontynent not in kontynenty:
                kontynenty.append(xkontynent)

    if len(kontynenty) >= 4:
        print(jezyk)

czwarte = []

for jezyk, rodzina in jezyki.items():
    if rodzina != 'indoeuropejska':
        uzytkownicy_suma = 0

        for x in uzytkownicy:
            [xpanstwo, xjezyk, xuzytkownicy, xurzedowy] = x
            xkontynent = panstwa[xpanstwo][0]

            if xjezyk == jezyk:
                if xkontynent == 'Ameryka Polnocna' or xkontynent == 'Ameryka Poludniowa':
                    uzytkownicy_suma += xuzytkownicy

        czwarte.append([jezyk, rodzina, uzytkownicy_suma])

czwarte = sorted(czwarte, key=lambda x: x[2], reverse=True)
for element in czwarte[:6]:
    [x, y, z] = element
    z = str(round(z, 2)).replace('.', ',')
    print(x, y, z)

for panstwo, [kontynent, populacja] in panstwa.items():
    for x in uzytkownicy:
        [xpanstwo, xjezyk, xuzytkownicy, xurzedowy] = x

        if xpanstwo == panstwo and xurzedowy == 'nie':
            if xuzytkownicy/populacja >= 0.3:
                print(panstwo, xjezyk, str(round((xuzytkownicy/populacja)*100,2)).replace('.', ',') + "%")
marki = {}
perfumy = {}
sklad = {}

with open('DANE/marki.txt') as f:
    for line in f.readlines()[1:]:
        tablica = line.strip().split('\t')
        marki[tablica[0]] = tablica[1]

with open('DANE/perfumy.txt') as f:
    for line in f.readlines()[1:]:
        tablica = line.strip().split('\t')
        tablica[4] = int(tablica[4])
        perfumy[tablica[0]] = tablica[1:]

with open('DANE/sklad.txt') as f:
    for line in f.readlines()[1:]:
        tablica = line.strip().split('\t')
        if tablica[0] not in sklad.keys():
            sklad[tablica[0]] = []
        sklad[tablica[0]].append(tablica[1])

print('Zadanie 6.1.')
for id, skladniki in sklad.items():
    if 'absolut jasminu' in skladniki:
        print(perfumy[id][0])

_6_2 = {}
for id, [nazwa_p, id_marki, rodzina_zapachow, cena] in perfumy.items():
    if rodzina_zapachow not in _6_2.keys():
        _6_2[rodzina_zapachow] = []

    replace = False
    if len(_6_2[rodzina_zapachow]) == 0:
        replace = True
    elif _6_2[rodzina_zapachow][0] > cena:
        replace = True

    if replace:
        _6_2[rodzina_zapachow] = [cena, nazwa_p]

print('')
print('Zadanie 6.2.')
for x, y in _6_2.items():
    print(x, *y)

_6_3 = []
for id_marki, nazwa_m in marki.items():
    ma_paczula = False
    for id, [nazwa_p, id_marki_p, rodzina_zapachow, cena] in perfumy.items():
        if id_marki_p == id_marki:
            for id_s, skladniki in sklad.items():
                if id_s == id:
                    for skladnik in skladniki:
                        if 'paczula' in skladnik:
                            ma_paczula = True
                            break

    if not ma_paczula:
        _6_3.append(nazwa_m)

_6_3 = sorted(_6_3)
print()
print('Zadanie 6.3.')
for x in _6_3:
    print(x)

id_mouderosine = 0
for id_marki, n_marki in marki.items():
    if n_marki == 'Mou De Rosine':
        id_mouderosine = id_marki
        break

_6_4 = {}
for id, [nazwa_p, id_marki, rodzina_zapachow, cena] in perfumy.items():
    if id_marki == id_mouderosine and rodzina_zapachow == 'orientalno-drzewna':
        _6_4[nazwa_p] = cena*0.85

print()
print('Zadanie 6.4.')
_6_4 = sorted(_6_4.items(), key=lambda x: x[1])
for x in _6_4:
    print(x[0], str(round(x[1], 2)).replace('.',','))

print()
print('Zadanie 6.5.')
for id_marki, n_marki in marki.items():
    rodziny = []
    for id, [nazwa_p, id_marki_p, rodzina_zapachow, cena] in perfumy.items():
        if id_marki_p == id_marki:
            if rodzina_zapachow not in rodziny:
                rodziny.append(rodzina_zapachow)

    if len(rodziny) == 1:
        print(n_marki, rodziny[0])
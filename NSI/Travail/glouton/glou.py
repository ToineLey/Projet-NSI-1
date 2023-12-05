from travdata_py import *

euros = [1, 2, 5, 10, 20, 50, 100, 200]

villes = ["Nancy", "Metz", "Paris", "Reims", "Troyes"]

dist = [
    [0, 55, 303, 188, 183],
    [55, 0, 306, 176, 203],
    [303, 306, 0, 142, 153],
    [188, 176, 142, 0, 123],
    [183, 203, 153, 123, 0]
]


def plus_proche(ville, dist, visitees):
    """renvoie le numéro de la ville non encore visitée la plus proche de la ville courante, en supposant qu'il en existe au moins une"""
    pp = None
    for i in range(len(visitees)):
        if visitees[i]:
            continue
        if pp == None or dist[ville][i] < dist[ville][pp]:
            pp = i
    return pp


def voyageur_org(villes, dist, depart):
    n = len(villes)
    visitees = [False] * n
    courante = depart
    for _ in range(n-1):
        visitees[courante] = True
        suivante = plus_proche(courante, dist, visitees)
        print("trajet de", villes[courante],
              "à", villes[suivante],
              "en", dist[courante][suivante], "km")
        courante = suivante

    print("retour depuis", villes[courante],
          "à la ville de départ", villes[depart],
          "en", dist[courante][depart], "km")


def voyageur(villes, dist, depart):
    t1 = [villes[depart]]
    n1 = 0
    n = len(villes)
    visitees = [False] * n
    courante = depart
    for _ in range(n-1):
        visitees[courante] = True
        suivante = plus_proche(courante, dist, visitees)

        t1.append(villes[suivante])
        n1 += dist[courante][suivante]
        courante = suivante
    t1.append(villes[depart])
    n1 += dist[courante][depart]
    return t1, n1


def monaie(s):
    i = len(euros) - 1
    p = 0
    while s > 0:
        if s >= euros[i]:
            s -= euros[i]
            p += 1
        else:
            i -= 1
    return p


def monaye(a):
    tab = []
    for i in range(a):
        tab.append(monaie(i))
    x=max(tab)
    y=[]
    for j in range(len(tab)):
        if tab[j]==x:
            y.append(j)
    return y


print(monaye(200))


#exo4
"""
a. 7500 = D+C+B
b. 7800 = C+A
c. 11200 = D+B
d. 12000 = C+B
"""

#exo5

"""
stratégie 1: 
    
    A+D = 5300
    A+C = 7800
    A = 8100
    A+D = 11800


stratégie 2:

    D+C+B = 7500
    D+C+B = 7000
    E+D+C = 10300
    F+E+D+C = 10300

stratégie 3:

    D+C+B = 7500
    A+C=7800
    B+D=11200
    A+E+F=11900
"""

#exo7
"""
1.
    1+2+2+5,
    6+4,
    3+3+4
2. 
    il en faut trois :
    6
    6
    8
"""


#exo6

"""
A+D -> stratégies 1
D+C+B -> stratégie 2
A -> stratégie 1
F+E+D+C -> stratégie 2
"""
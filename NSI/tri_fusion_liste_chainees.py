from Liste import Cellule, str_liste

def divise(lst):
    """sépare une liste en 2 listes ayant 
        le même nombre d'éléments (à un près)"""
    l1, l2 = None, None
    while lst is not None:
        l1, l2 = Cellule(lst.valeur, l2), l1
        lst = lst.suivante
    return l1, l2

def fusion(l1, l2):
    """fusionne 2 listes chaînées triées
       par défaut limité à des listes de taille 1000"""
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    if l1.valeur < l2.valeur:
        return Cellule(l1.valeur, fusion(l1.suivante, l2))
    else:
        return Cellule(l2.valeur, fusion(l1, l2.suivante))

def fusion2(l1, l2):
    """fusionne 2 listes triées avec une boucle while"""
    lst = None
    while l1 is not None or l2 is not None:
        if (l1 is not None and (l2 is None or l1.valeur <= l2.valeur)):
            lst, l1 = Cellule(l1.valeur, lst), l1.suivante
        else:
            lst, l2 = Cellule(l2.valeur, lst), l2.suivante
    # renversement de lst
    r = None
    while lst is not None:
        r = Cellule(lst.valeur, r)
        lst = lst.suivante
    return r


def tri_fusion(lst):
    if lst is None or lst.suivante is None:
        return lst
    l1, l2 = divise(lst)
    return fusion(tri_fusion(l1), tri_fusion(l2))

# Exercice 5
lst = Cellule(8, Cellule(1, Cellule(3, Cellule(0, Cellule(1, Cellule(2, Cellule(5, None)))))))
l1, l2 = divise(lst)
print("l1 :", str_liste(l1))
print("l2 :", str_liste(l2))


from Arbre_binaire.arbre import Noeud

def parcours_largeur(arbre):
    p = ""
    courant = {arbre}
    suivant = set()
    while len(courant) > 0:
        s = courant.pop()
        suivants.add(s.gauche)
        suivants.add(s.droite)
        p+=str(s.valeur)
        if len(courant)==0:
            courant, suivant = suivant, set()
    return p

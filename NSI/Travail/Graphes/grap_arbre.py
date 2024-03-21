from Arbre_binaire.arbre import Noeud

def parcours_largeur(arbre):
    p = ""
    courant = {arbre}
    suivant = set()
    while len(courant) > 0:
        s = courant.pop()
        suivants.add(s.gauche) if s.guauche is not None
        suivants.add(s.droite) if s.droite is not None
        p+=str(s.valeur)
        if len(courant)==0:
            courant, suivant = suivant, set()
    return p

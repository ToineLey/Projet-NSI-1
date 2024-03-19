from Arbre_binaire.arbre import Noeud

def parcours_largeur(arbre, racine):
    dist = {racine: 0}
    courant = {racine}
    droite = arbre.droit
    gauche = arbre.gauche
    suivant = set
    while gauche is not None:
        s = courant.pop()
        for v in gauche:
            if v not in dist:
                suivant.add(v)
                dist[v] = dist[s]+1
        if gauche is None:
            courant, suivant = suivant, set()
    return dist


def distance(g, u, v):
    dist = parcours_largeur(g, u)
    return dist[v] if v in dist else None
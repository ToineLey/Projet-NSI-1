class Noeud:
    def __init__(self, v, f):
        self.valeur, self.fils = v, f


def taille(a):
    t = 1
    for f in a.fils:
        t += taille(f)
    return taille


def parcour_prefixe(a):
    ch = str(a.valeur)
    for f in a.fils:
        ch += parcour_prefixe(f)
    return ch


def affiche(a):
    ch =str(a.valeur)+"\n"
    for f in a.fils:
        ch+=affiche(f)
        
    return ch

def affiche2(a):    
    ch =str(a.valeur)
    print(ch+" ")
    for f in a.fils:
        affiche2(f)
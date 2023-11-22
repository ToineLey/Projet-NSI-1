from math import pi


def egal(a, b):
    if a is None and b is None:
        return True
    else:
        g1 = egal(a.gauche)
        d1 = egal(a.droit)
        g2 = egal(b.gauche)
        d2 = egal(b.droit)
        return egal(g1, g2) and egal(d1, d2)


class Noeud:
    def __init__(self, g, v, d):
        self.gauche = g
        self.droit = d
        self.valeur = v

    def __eq__(self, other):
        egal(self, other)


def str_arbre(a):
    if a is None:
        return ''
    else:
        g = str_arbre(a.gauche)
        d = str_arbre(a.droit)
        return "(" + g + str(a.valeur) + d + ")"


assert str_arbre(Noeud(Noeud(None, "B", Noeud(None, "C", None)),
                 "A", Noeud(None, "D", None))) == "((B(C))A(D))"




def parfait(h):
    if h == 0:
        return Noeud(None,pi**(h+1),None)
    else:
        return Noeud(parfait(h-1),pi**(h+1),parfait(h-1))
    
a = parfait(5)
print(str_arbre(a))




"""
    (1)
    /  \
  (0)  (0)
  / \  / \
(a)(a)(a)(a)



"""

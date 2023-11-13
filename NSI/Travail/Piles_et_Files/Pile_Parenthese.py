from Travail.Piles_et_Files.Pile import *

def parenthese(chaine,f):
    c = creer_pile()
    for i in range(len(chaine)):
        if chaine[i] == "(":
            c.empiler(i)
        elif chaine[i] == ")":
            if i == f:
                return c.depiler()
            else:
                c.depiler()
            


def parenthese_correspondante(a):
    r = creer_pile()
    c = creer_pile()
    for i in range(len(a)):
        if a[i] == "[":
            c.empiler(i)
        elif a[i] == "(":
            r.empiler(i)
        elif a[i] == ")":
            if r.est_vide():
                return False
            r.depiler()
        elif a[i] == "]":
            if c.est_vide():
                return False
            c.depiler()
    return (c.est_vide() and r.est_vide())
import xml.dom.minidom as dom
import os


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


def affiche2(a, ch=""):

    print(ch+str(a.valeur))
    for f in a.fils:
        affiche2(f, " "+ch)


"""def repertoire(r: str) -> Noeud:
    assert os.path.isdir(r)
    if not os.listdir(r)==[]:
        return Noeud(r,[])
    else:
        return Noeud(r,)"""


def repertoires(r: str) -> Noeud:
    assert os.path.isdir(r)
    fils = []
    for elt in os.listdir(r):
        if os.path.isdir(os.path.join(r, elt)):
            fils.append(repertoires(os.path.join(r, elt)))
        else:
            fils.append(Noeud(os.path.join(r, elt), []))
    return Noeud(r, fils)


"""def compte_balise(d: DOM, n) -> int:
    if d.childNodes == []:
        return 0
    elif d.parentNode is None:
        return compte_balise(d.childNode[0],n)
    else:
        for el in d.childNodes:
            if d.nodeName == n:
                return 1+compte_balise(el, n)
            else:
                return 0+compte_balise(el, n)"""
def compte_balise(d: DOM, n) -> int:
    nb=0
    if d.nodeName==n:
        nb+=1
    for el in d.childNodes:
        nb+=compte_balise(el,n)
    return nb




def stat_xml(d: DOM):
    e,a,t=0,0,0
    if d.nodeType==dom.Node.ELEMENT_NODE:
        e+=1
        a+=len(d.attributes)
    elif d.nodeType==dom.Node.TEXT:
        t+=1
    for elt in d.childNodes:
        e1,a1,t1=stat_xml(elt)
        e,a,t=e1,a1,t1
    return e,a,t






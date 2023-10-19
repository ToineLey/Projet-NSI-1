class Cellule:

    def __init__(self,v,s):
        self.valeu = v
        self.suivante = s

def longueur(lst):
    if lst is None:
        return 0
    else:
        return 1 + longueur(lst.suivante)
        
def nieme_element(n,lst):
    if lst is None:
        raise IndexError("indice invalide")
    elif n==0:
        return lst.valeur
    else:
        return nieme_element(n-1, lst.suivante)
        
def concatener(l1,l2):
    if l1 is None:
        return l2
    else:
        return Cellule(l1.valeur, concatener(l1.suivante, l2))
        
def renverser(lst):
    if lst is None: 
        return None
    else:
        return concatener(renverser(lst.suivante),Cellule(lst.valeur,None))

class Liste:

    def __init__(self):
        self._tete = None

    def est_vide(self):
        return self._tete is None

    def ajoute(self,x):
        self._tete = Cellule(x,self._tete)

    def __len__(self):
        n=0
        c = self._tete
        while c is not None:
            n += 1
            c = c.suivante
        return n
    
    def __getitem(self, n):
        return nieme_element(n,self._tete)
    
    def renverser(self):
        self._tete = renverser(self._tete)

    def __ad__(self, lst):
        r = Liste()
        r._tete = concatener(self._tete, lst._tete)
        return r
    
def str_liste(lst):
    if lst is None:
        return ""
    else:
        return str(str_liste(lst)) + "->" + str_liste(lst.suivante)

def nieme_element(lst,n):
    i = 0
    while lst is not None and i != n:
        i+=1
        lst = lst.suivante
    if lst is None:
        raise IndexError()
    else:
        return lst.valeur

def ocurences(x,lst):
    if lst is None:
        return 0
    else:
        if x==lst.valeur:
            return 1 + ocurences(x,lst.suivante)
        else:
            return ocurences(x,lst.suivante)

def ocurences2(x,lst):
    a=0
    c=lst
    while c is not None:
        if c.valeur == x:
            a+=1
        c=c.suivante
    return a

def trouve(x,lst):
        
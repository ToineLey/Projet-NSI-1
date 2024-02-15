from NSI.Travail.Liste_Chaine.Liste import Cellule

class Pile:
    def __init__(self):
        self._contenu = None

    def est_vide(self):
        return self._contenu is None

    def empiler(self, e):
        self._contenu = Cellule(e, self._contenu)

    def depiler(self):
        if self.est_vide():
            raise IndexError("dépile une pile vide")
        v = self._contenu.valeur
        self._contenu = self._contenu.suivante
        return v

def creer_pile():
  return Pile()

class File:
    def __init__(self):
        self._tete = None
        self._queue = None

    def est_vide(self):
        return self._tete is None

    def ajouter(self, e):
        c = Cellule(e, None)
        if self.est_vide():
            self._tete = c
        else:
            self._queue.suivante = c
        self._queue = c

    def retirer(self):
        if self.est_vide():
            raise IndexError("retire un file vide")
        v = self._tete.valeur
        self._tete = self._tete.suivante
        if self._tete is None:
            self._queue = None
        return v

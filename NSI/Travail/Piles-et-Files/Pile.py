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


class File:
    def __init__(self):
        self.tete = None
        self.queue = None

    def est_vide(self):
        return self.tete is None

    def ajouter(self, e):
        c = Cellule(e, None)
        if self.est_vide():
            self.tete = c
        else:
            self.queue.suivante = c
        self.queue = c

    def retirer(self):
        if self.est_vide():
            raise IndexError("retire un file vide")
        v = self.tete.valeur
        self.tete = self.tete.suivante
        if self.tete is None:
            self.queue = None
        return v

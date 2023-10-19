class DbTab:
    def __init__(self, g, d):
        self.gauche = g.copy()[::-1]
        self.droite = d.copy()

    def imin(self):
        if not self.gauche:
            return 0
        return -len(self.gauche)

    def imax(self):
        if not self.droite:
            return -1
        return len(self.droite) - 1

    def append(self, elt):
        self.droite.append(elt)

    def prepend(self, elt):
        self.gauche.append(elt)

    def __getitem__(self, i):
        if i < self.imin() or i > self.imax():
            raise IndexError("Index out of range")
        if i < 0:
            return self.gauche[self.imin() - i]
        return self.droite[i]

    def __setitem__(self, i, elt):
        if i < self.imin() or i > self.imax():
            raise IndexError("Index out of range")
        if i < 0:
            self.gauche[self.imin() - i] = elt
        else:
            self.droite[i] = elt

    def __str__(self):
        return str(self.gauche[::-1] + self.droite)

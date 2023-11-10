from NSI.Travail.Piles_et_Files.Pile import *

class Historique:
    def __init__(self):
        self.adresse_courante = None
        self._adresses_precedentes = creer_pile()

    def aller_a(self, adr):
        if not self.adresse_courante is None:
            self._adresses_precedentes.empiler(self.adresse_courante)
        self.adresse_courante = adr

    def retour(self):
        if not self._adresses_precedentes.est_vide():
            self.adresse_courante = self._adresses_precedentes.depiler()
        else:
            self.adresse_courante = None

# ****************** TESTS ******************
 h = Historique()
 assert h.adresse_courante is None
 h.aller_a("www.stackoverflow.com")
 assert h.adresse_courante == "www.stackoverflow.com"
 h.aller_a("www.developper.com")
 h.retour()
 assert h.adresse_courante == "www.stackoverflow.com"
 h.aller_a("www.w3schools.com")
 h.aller_a("openclassroom.com")
 h.retour()
 assert h.adresse_courante == "www.w3schools.com"
 h.retour()
 assert h.adresse_courante == "www.stackoverflow.com"
 # on teste "retour" lorsqu'il n'y plus d'adresse antérieure
 h.retour()
 assert h.adresse_courante is None
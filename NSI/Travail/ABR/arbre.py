from math import log

class Noeud:
    def __init__(self, g, v, d):
        self.gauche = g
        self.droit = d
        self.valeur = v
    def __str__(self):
      return str_arbre(self)
    def __contains__(self, x):
      return appartient(self,x)
    def ajouter(self, x):
      ajoute(self, x)
    def taille():
      pass
    def hauteur(self):
      return log(self.taille(),2)
    def supp(self, x):
      if not appartient(self, x):
        print("rien n'a été supprimé")
      elif x == self.valeur:
        

def appartient(x, a):
 if a is None:
  return False
 elif x < a.valeur:
  return appartient(x,a.gauche)
 elif x > a. valeur:
  return appartient (x, a.droit) 
 else: #cas d'égalité 
  return True

def ajoute(x, a):
 if a is None:
  return Noeud (None, x, None)
 elif x < a.valeur:
  return Noeud(ajoute(x, a.gauche), a.valeur,:a.droit)
 else:
  return Noeud(a.gauche, a.valeur, ajoute(x, a.droit))

def str_arbre(a):
  if a is None:
      return ''
  else:
      g = str_arbre(a.gauche)
      d = str_arbre(a.droit)
      return "(" + g + str(a.valeur) + d + ")"





def minimum(a):
  if a is None:
    return None
  elif a.gauche is None:
    return a
  else:
    return(minimum(a.gauche))


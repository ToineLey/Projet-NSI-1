from dates-1 import cree, contient, ajoute
def contient_doublon(t):
  s = cree()
  for x in t:
    if contient(s, x) :
     ajoute (s, x)
  return s

contient_doublon([15,2,76,54,15,9,40,67,72,8])
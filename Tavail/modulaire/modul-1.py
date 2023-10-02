from dates import cree, contient, ajoute
def contient_doublon(t):
  s = cree()
  for x in t:
    if contient(s, x) :
      return True
    ajoute (s, x)
  return False
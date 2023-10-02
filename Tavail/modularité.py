from dates import cree, contient, ajoute
from random import randint
def annivSansFin ( ):
  cpt = 0
  nbDates = 0
  s = cree ()
  while nbDates < 366:
    cpt += 1
    x = randint (1, 366)
    if not contient(s, x):
      nbDates += 1
      ajoute (s, X)
    return cpt
  n = 0
  for in range (1000):
  n += annivSansFin ()
  print(f"En moyenne, il faut {n/1000} élèves")
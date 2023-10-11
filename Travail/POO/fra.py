from Travail.POO.divi import *


class Fraction:

  def __init__(self, num, den):
    self.numerateur = num // pgcd(num, den)
    if den <= 0:
      raise ValueError("Fraction avec dénominateur à 0")
    else:
      self.denominateur = den // pgcd(num, den)

  def __str__(self):
    n = str(self.numerateur)
    if self.denominateur == 1:
      d = ""
    else:
      d = " / " + str(self.denominateur)
    return n + d

  def __eq__(self, autre):
    return ((self.numerateur * autre.denominateur) == (self.denominateur * autre.numerateur))

  def __lt__(self, autre):
    return (self.numerateur * autre.denominateur <
            self.denominateur * autre.numerateur)

  def __add__(self, autre):
    return Fraction(
        self.numerateur * autre.denominateur +
        self.denominateur * autre.numerateur,
        self.denominateur * autre.denominateur)

  def __mul__(self, autre):
    return Fraction(self.numerateur * autre.numerateur,
                    self.denominateur * autre.denominateur)

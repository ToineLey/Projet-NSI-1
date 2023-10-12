class Intervalle:

  def __init__(self, inf, sup):
    if inf > sup:
      self.borne_inf = 0
      self.borne_sup = 0
    else:
      self.borne_inf = inf
      self.borne_sup = sup

  def est_vide(self):
    return self.borne_inf == 0 and self.borne_sup == 0
  
  def __str__(self):
    if self.borne_inf == 0 and self.borne_sup == 0 and self.est_vide == True:
      return "∅"
    else:
      return "[self.borne_inf,self.borne_sup]"

  def __len__(self):
    a = self.borne_sup - self.borne_inf + 1
    return a

  def __contains__(self, x):
    return self.borne_inf <= x <= self.borne_sup

  def __eq__(self, x):
    if isinstance(x, Intervalle):
      if self.borne_inf == 0 or self.borne_sup == 0:
        return self.borne_inf == x.borne_inf and self.borne_sup == x.borne_sup
      return self.borne_inf == x.borne_inf and self.borne_sup == x.borne_sup
    return False

  def __le__(self, x):
    if isinstance(x, Intervalle):
      if self.borne_inf == 0 or self.borne_sup == 0:
        return True
      else:
        return self.borne_inf <= x.borne_sup and self.borne_sup >= x.borne_inf
    return False


  def intersection(self, x):
    if self.borne_sup < x.borne_sup:
      if x.borne_inf <= self.borne_sup:
        return Intervalle(x.borne_inf, self.borne_sup)
      else:
        return Intervalle(0, 0)
    else:
      if self.borne_inf <= x.borne_sup:
        return Intervalle(self.borne_inf, x.borne_sup)
      else:
        return Intervalle(0, 0)

  def union(self, x):
    if self.borne_sup < x.borne_sup:
      return Intervalle(self.borne_inf, x.borne_sup)
    else:
      return Intervalle(x.borne_inf, self.borne_sup)

  def intersection_2(self, x):
    inf = max(self.borne_inf, x.borne_inf)
    sup = min(self.borne_sup, x.borne_sup)
    return Intervalle(inf, sup)

  def union_2(self, x):
    inf = min(self.borne_inf, x.borne_inf)
    sup = max(self.borne_sup, x.borne_sup)
    return Intervalle(inf, sup)

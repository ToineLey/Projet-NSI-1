class Intervalle:
    def __init__(self,inf,sup):
      if inf > sup:
        self.borne_inf = 0
        self.borne_sup = 0
      else:
        self.borne_inf = inf
        self.borne_sup = sup
    def __str__(self):
      if self.borne_inf ==0 or self.borne_sup == 0:
        return "∅"
      else:
        return "[{},{}]".format(self.borne_inf,self.borne_sup)
    def __len__(self):
      a = self.borne_sup - self.borne_inf
      return a
    def __contains__(self,x):
      return x.borne_inf >= self.borne_inf and x.borne_sup <= self.borne_sup
    def __eq__(self,x):
      if len(self) == 0 and len(x)== 0:
        return True
      else:
        if len(self) == 0 or len(x)== 0:
         return False
        else:
          return self.borne_inf == x.borne_inf and self.borne_sup == x.borne_sup
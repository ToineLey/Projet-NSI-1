def cree():
    return [0]*6


def contient(s, x):
    iEntier = x // 64
    bit = x % 64
    return (s[iEntier] & (1 << bit) != 0)


def ajoute(s, x):
    iEntier = x // 64
    bit = x % 64
    s[iEntier] = s[iEntier] | 1 << bit
    return


def enumere(s):
    tab = []
    for ientier in range(len(s)):
      for bit in range(64):
          if s[ientier] & (1<<bit) != 0:
              tab.append(ientier*64+bit)
    return tab


def union(s4,s5):
    return 

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
          if ientier & (1<<bit) != 0:
              tab.append(ientier*64+bit)
    return tab


def union(s1, s2):
    s4=[]
    for elem in s1:
        if elem not in s2:
            s4.append(elem)
    return s4


def intersection(s3, s4):
    s5 = []
    for elem in s3:
        if elem in s4:
            s5.append(elem)
    return s5

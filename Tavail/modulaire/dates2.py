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
    ientier = 0
    
    
    return 


def union(s1, s2):
    s4=[]
    s3 = intersection(s1, s2)
    for elem in s1:
        if s3 not in s2:
            s4.append(elem)
    return s4


def intersection(s3, s4):
    s5 = []
    for elem in s3:
        if elem in s4:
            s5.append(elem)
    return s5

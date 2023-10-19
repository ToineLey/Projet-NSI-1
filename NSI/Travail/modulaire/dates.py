def cree():
    return list()

def contient(s,x):
    return x in s

def ajoute(s,x):
    return s.append(x)

def union(s1, s2):
    s4=[]
    for elem in range(len(s1)):
        if elem not in s2:
            s4.append(s1[elem])
    for el in range(len(s2)):
        s4.append(s2[el])
    return s4


def intersection(s3, s4):
    s5 = []
    for elem in range(len(s3)):
        if s3[elem] in s4:
            s5.append(s3[elem])
    return s5

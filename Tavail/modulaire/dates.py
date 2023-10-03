def cree():
    return list()

def contient(s,x):
    return x in s

def ajoute(s,x):
    return s.append(x)






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

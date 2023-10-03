def cree():
    return 0

def contient(s,x):
    return s[0] & (1 << x) != 0

def ajoute(s,x):
    s[0] = s[0] | (1<<x)
    return

def enumere():
    
    return


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

def cree():
    return 0

def contient(s,x):
    return s[0] & (1 << x) != 0

def ajoute(s,x):
    s[0] = s[0] | (1<<x)
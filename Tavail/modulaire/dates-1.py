def cree():
    return 0

def contient(s,x):
    if s &(1<<x)!=0:
        return True
    else: 
        return False

def ajoute(s,x):
    return s | (1<<x)
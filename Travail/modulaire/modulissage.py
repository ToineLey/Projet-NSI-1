from dates2 import *


def contient_doublon(t):
    s = cree()
    for x in t:
        if contient(s, x):
            return True
        ajoute(s, x)
    return False


#print(contient_doublon([15, 2, 76, 54, 15, 9, 40, 67, 72, 8]))
print(enumere([15, 2, 76, 54, 15, 9, 40, 67, 72, 8]))
a = [15,45,84,20,12,56,45,85,32,42]
b = [20,15,68,12,56,88,85,31,32]

#print(union(a,b))
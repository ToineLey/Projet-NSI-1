from Pile import *


def deplace(a, b, c, k):
    if k == 1:
        print("déplace", str(a), "vers", str(b), '\n')
    else:
        deplace(a, c, b, k-1)
        deplace(a, b, c, 1)
        deplace(c, b, a, k-1)


def hanoi(n):
    deplace(1, 3, 2, n)


def deplace_pile(a: Pile, b: Pile, c: Pile, k: int):
    if k == 1:
        b.empiler(a.depiler())
    else:
        deplace(a, c, b, k-1)
        deplace(a, b, c, 1)
        deplace(c, b, a, k-1)


def hanoi_pile(n):
    p1,p2,p3 = creer_pile(),creer_pile(),creer_pile()
    for i in range(n,0,-1):
        p1.empiler(i)
    deplace_pile(p1,p3,p2,n)
    for i in range(4):
        print(p3.depiler)


hanoi_pile(5)


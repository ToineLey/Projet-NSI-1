from plan import *
from random import choice

def trouve(p, t: list):
    for tout in t:
        if p(tout):
            return tout


def applique(f, t: list):
    d=choice("a","b","c")
    if d == "a":
        a = [None]*len(t)
        for elem in range(len(t)):
            a[elem] = f(t[elem])
        return a
    elif d == "b":
        return [f(t[i]) for i in range(len(t))]
    else:
        return [f(el) for el in t]
    


def calcule(op: function, t: list, f: function):
    v = f(t[0])
    for i in range(1, len(t)):
        v = op(v, f(t[i]))
    return v


def compose(f: function, g: function):
    return f(g)


def feplacer_triangle(t, dx, dy):
    return triangle(
        deplacer(triangle[0], dx, dy),
        deplacer(triangle[1], dx, dy),
        deplacer(triangle[2], dx, dy)
    )

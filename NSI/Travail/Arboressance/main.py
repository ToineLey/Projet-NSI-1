from arbre import *

a = Noeud("A", [Noeud("B", [Noeud("D", [])]),
                Noeud("C", [
                    Noeud("E", []),
                    Noeud("F", [Noeud("H", [])]),
                    Noeud("G", [])
                ])])

print(affiche2(a))
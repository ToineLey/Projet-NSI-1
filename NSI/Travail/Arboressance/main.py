from arbre import *

a = Noeud("A", [Noeud("B", [Noeud("D", [])]),
                Noeud("C", [
                    Noeud("E", []),
                    Noeud("F", [Noeud("H", [])]),
                    Noeud("G", [])
                ])])
domm=dom.parse("/home/tnsi-eleve5/projets/Projets-NSI/NSI/Travail/Arboressance/recette.xml")
print(compte_balise(domm,"e"))
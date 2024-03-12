class Graphe1:
    def __init__(self, n):
        self.n = n
        self.adj = [[False]*n for _ in range(n)]

    def ajouter_arc(self, s1, s2):
        self.adj[s1][s2] = True

    def arc(self, s1, s2):
        return self.adj[s1][s2]

    def voisins(self, s):
        v = []
        for i in range(self.n):
            if self.adj[s][i]:
                v.append(i)
        return v

class Graphe2:
    def __init__(self):
        self.adj = {}

    def ajouter_sommet(self, s):
        if s not in self.adj:
            self.adj[s] = set()

    def ajouter_arc(self, s1, s2):
        self.ajouter_sommet(s1)
        self.ajouter_sommet(s2)
        self.adj[s1].add(s2)

    def arc(self, s1, s2):
        return s2 in self.adj[s1]

    def sommets(self):
        return list(self.adj)

    def voisins(self, s):
        return self.adj[s]
    
    def __str__(self):
        a=""
        for i in range(len(self.adj)):
            a+=str(i)+":"+str(self.adj[i])+"\n"
        return a
    def nombre_sommets(self):
        a=0
        for i in range(len(self.adj)):
            if self.adj[i]!=set():
                a+=1
        return a

g=Graphe1(4)
g.ajouter_arc(0,1)
g.ajouter_arc(0,3)
g.ajouter_arc(1,2)
g.ajouter_arc(1,3)
g.ajouter_arc(2,3)

print(g.adj)
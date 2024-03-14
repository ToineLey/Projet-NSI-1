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

    def __str__(self):
        a = ""
        for i in range(self.n):
            a += "->"
            for j in range(self.n):
                if self.adj[i][j]:
                    a += str(j)
            a += "\n"
        return a

    def degre(self, s):
        d = 0
        for i in range(self.n):
            if self.adj[s][i]:
                d += 1
        return d

    def nb_arc(self):
        a = 0
        for i in range(self.n):
            for j in range(self.n):
                if self.adj[i][j]:
                    a += 1
        return a

    def supprimer_arc(self, s1, s2):
        self[s1][s2] = False


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
    
    def ajouter_arc_no(self, s1, s2):
        self.ajouter_sommet(s1)
        self.ajouter_sommet(s2)
        self.adj[s1].add(s2)
        self.adj[s2].add(s1)

    def arc(self, s1, s2):
        return s2 in self.adj[s1]

    def sommets(self):
        return list(self.adj)

    def voisins(self, s):
        return self.adj[s]

    def __str__(self):
        a = ""
        for key in self.adj:
            a += str(key)+":"+str(self.adj[key])+"\n"
        return a

    def nombre_sommets(self):
        a = 0
        for key in self.adj:
            if self.adj[key] != set():
                a += 1
        return a

    def degre(self, s):
        return len(self.adj[s])

    def nb_arc(self):
        a = 0
        for key in self.adj:
            a += len(self.adj[key])
        return a

    def supprimer_arc(self, s1, s2):
        a = set()
        for val in self.adj[s1]:
            if val != s2:
                a.append(val)
        self.adj[s1] = a


def mex(voisins, couleur):
    n = len(voisins)
    d = [True]*(n+1)
    for v in voisins:
        if v in couleur and couleur[v] <= n:
            d[couleur[v]] = False
    for c in range(n+1):
        if d[c]:
            return c
    assert False


def coloriage(g):
    couleur = {}
    n = 0
    for s in g.sommets():
        c = mex(g.voisins(s), couleur)
        couleur[s] = c
        n = max(n, c+1)
    return couleur, n


g = Graphe1(4)
g.ajouter_arc(0, 1)
g.ajouter_arc(0, 3)
g.ajouter_arc(1, 2)
g.ajouter_arc(1, 3)
g.ajouter_arc(2, 3)

print(g.adj)

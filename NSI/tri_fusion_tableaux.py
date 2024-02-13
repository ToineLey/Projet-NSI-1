def fusion(t, g, m, d):
    
    # initialisations
    n1, n2 = m - g + 1, d - m
    lg, ld = t[g:m+1], t[m + 1: d + 1]
    
    # Ajout d'une "sentinelle" en fin des 2 tableaux
    if lg[-1] > ld[-1]:
        max = lg[-1] + 1
    else:
        max = ld[-1] + 1
    lg.append(max)
    ld.append(max)

    # On peut identifier les 2 listes à 2 piles de cartes triées:
    # On compare les 2 cartes en haut de chaque pile et on prend la plus petite
    i, j = 0, 0
    for k in range(g, d + 1):
        if lg[i] <= ld[j]:
            t[k] = lg[i]
            i += 1
        else:
            t[k] = ld[j]
            j += 1
    # après n itérations, il doit rester un seul élément dans chaque liste lg et ld : la sentinelle (max)

def triFusion(t, g, d):
    if g < d:
        m = (g + d) // 2
        triFusion(t, g, m)
        triFusion(t, m+1, d)
        fusion(t, g, m, d)

# Jeu d'essai
t = [1,5,7,9,2,6,14]
fusion(t, 0, 3, 6)
assert t == [1,2,5,6,7,9,14]
t = [1,5,20,2,7,9,14,5]
triFusion(t, 0, len(t) - 1)
assert t == [1,2,5,5,7,9,14,20]

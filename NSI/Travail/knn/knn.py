def hamming(a, b):
    n = 0
    if len(a) != len(b):
        n += max(len(b), len(a))-min(len(b), len(a))
        for i in range(min(len(b), len(a))):
            if a[i] != b[i]:
                n += 1
    else:
        for i in range(len(a)):
            if a[i] != b[i]:
                n += 1

    return n


assert hamming('arbre', 'art') == 3
assert hamming("si je ne m'abuse", "si je ne m'amuse") == 1
assert hamming('canard', 'cannard') == 4
assert hamming('amer', 'ramer') == 5


# exo 2

lexique = ['oui', 'non', 'yes', 'no', 'ok']

def exii(m: str, d: int) -> None:
    for trucs in lexique:
        if hamming(trucs, m) <= d:
            print(trucs)

# exo 3
            
def exiii(m: str) -> None:
    t=[]
    for trucs in lexique:
        t.append(hamming(trucs, m))
    exii(m,min(t))
    

def possible_retirer(c,d):
    if len(d)!=len(c)+1:
        return False
    for i in range(len(d)-1):
        if d[i]!=c[i]:
            return c[i:]==d[i+1:]
    return True

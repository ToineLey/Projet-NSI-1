def aligne(mot1: str, mot2: str):
    """le score du meilleur alignement de mot1 et mot2"""
    n1, n2 = len(mot1), len(mot2)
    sc = [[0]*(n2+1) for _ in range(n1 + 1)]
    ma=[[["",""] for _ in range(n2+1)] for _ in range(n1+1)]
    # 1ère ligne et 1ère colonne
    for i in range(1, n1 + 1):
        sc[i][0] = -i
        ma[i][0] = [ma[i-1][0][0]+mot1[i],ma[i-1][0][1]+"-"]
    for j in range(1, n2 + 1):
        sc[0][j] = -j
        ma[0][j] = [ma[0][j-1][0]+"-",ma[0][j-1][1]+mot2[j-1]]
    # le reste de sc
    for i in range(1, n1 + 1):
        for j in range(1, n2+1):
            """s = max(-1+sc[i-1][j], -1 + sc[i][j-1])"""
            if (-1+sc[i-1][j][0])<-1 + sc[i][j-1][0]:
                s=-1 + sc[i][j-1][0]
                ma[i][j]=[ma[
            else:
                s=-1+sc[i-1][j][0]
            if mot1[i-1] == mot2[j-1]:
                if sc[i-1][j-1][0]+1>s[0]:
                    s=[sc[i-1][j-1],'diag']
            elif sc[i-1][j-1][0]-1>s[0]:
                s=[sc[i-1][j-1],'diag']
            sc[i][j]=s.copy()
    return sc[n1][n2]


print(aligne('GENOME', 'ENORME'))

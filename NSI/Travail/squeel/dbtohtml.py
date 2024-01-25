import sqlite3 as sgbd

cnx = sgbd.connect(
    '/home/tnsi-eleve5/projets/Projets-NSI/NSI/Travail/squeel/mediatheque.db')

c = cnx.cursor()

motif1 = str(input("Date numéro 1 : \n"))
motif2 = str(input("Date numéro 2 : \n"))

c.execute('SELECT * FROM livre WHERE annee >= ?',
          [motif1])

livres = []

for l in c.fetchall():
    livres.append([l[1],l[2], {'annee':l[3]},l[4]])

print(livres)

for j in range(len(livres)):
    if livres[j]['annee']<=motif2:
        del(livres[j])

print(livres)
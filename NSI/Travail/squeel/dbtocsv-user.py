import csv
import sqlite3 as sgbd

cnx = sgbd.connect(
    '/home/tnsi-eleve5/projets/Projets-NSI/NSI/Travail/squeel/mediatheque.db')

c = cnx.cursor()
c.execute('SELECT * FROM usager')

users = []

for l in c.fetchall():
    users.append({'nom': l[1], 'adresse': l[2],
                 'ville': l[3], 'email': l[4], 'code_barre': l[5]})


with open('usager.csv', 'w') as f:
    w = csv.DictWriter(f, ["nom", "adresse", "ville", "email", "code_barre"])
    w.writeheader()
    w.writerows(users)

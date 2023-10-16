from Travail.Poo.table import Table


db_tab = DbTab([1, 2, 3], [4, 5, 6])
assert db_tab.imin() == -3
assert db_tab.imax() == 2
assert str(db_tab) == '[-3, -2, -1, 0, 1, 2]'
db_tab.append(7)
assert str(db_tab) == '[-3, -2, -1, 0, 1, 2, 7]'
db_tab.prepend(0)
assert str(db_tab) == '[-3, -2, -1, 0, 1, 2, 7]'
db_tab[3] = 42
assert db_tab[3] == 42
db_tab[0] = 8
assert str(db_tab) == '[-3, -2, -1, 0, 8, 2, 7]'

from Travail.POO.inter import Intervalle

intervalle1 = Intervalle(1, 5)
intervalle2 = Intervalle(2, 7)
intervalle3 = Intervalle(4, 9)

assert str(intervalle1) == "[1,5]"
assert str(intervalle2) == "[2,7]"
assert str(intervalle3) == "[4,9]"

assert len(intervalle1) == 5
assert len(intervalle2) == 6
assert len(intervalle3) == 6

assert (3 in intervalle1)
assert (5 in intervalle2)

assert (intervalle1 == intervalle2) == False
assert (intervalle2 == intervalle3) == False

assert intervalle1 <= intervalle2
assert intervalle2 <= intervalle3

intersection1 = intervalle1.intersection(intervalle2)
assert str(intersection1) == "[2,5]"

intersection2 = intervalle1.intersection(intervalle3)
assert str(intersection2) == "[4,5]"

union1 = intervalle1.union(intervalle2)
assert str(union1) == "[1,7]"

union2 = intervalle1.union(intervalle3)
assert str(union2) == "[1,9]"

intersection_2 = intervalle1.intersection_2(intervalle2)
assert str(intersection_2) == "[2,5]"

union_2 = intervalle1.union_2(intervalle2)
assert str(union_2) == "[1,7]"

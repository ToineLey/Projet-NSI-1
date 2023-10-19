from Travail.POO.fra import Fraction


fraction1 = Fraction(4, 2)
fraction2 = Fraction(6, 3)
fraction3 = Fraction(5, 8)


assert str(fraction1) == "2"
assert str(fraction2) == "2"
assert str(fraction3) == "5 / 8"


assert (fraction1 == fraction2) == True
assert (fraction1 == fraction3) == False


assert (fraction1 < fraction2) == False
assert (fraction2 < fraction3) == False


result1 = fraction1 + fraction2
assert str(result1) == "4"
result2 = fraction2 + fraction3
assert str(result2) == "21 / 8"


result3 = fraction1 * fraction2
assert str(result3) == "4"
result4 = fraction2 * fraction3
assert str(result4) == "5 / 4"
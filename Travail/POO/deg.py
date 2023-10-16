from math import pi, cos, sin


class Angle:
    def __init__(self, an):
        if isinstance(an, int):
            if 0 <= an <= 360:
                self.angle = an
            else:
                self.angle = an % 360
        else:
            raise TypeError("Le nombre doit être un entier")

    def __str__(self):
        return str(self.angle) + " degrés"

    def ajoute(self, x):
        self.angle += x.angle

    def cos(self):
        return cos(self.angle) * (pi/180)

    def sin(self):
        return sin(self.angle) * (pi/180)

        
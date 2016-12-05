from math import pi

class Circle:
    def __init__(self):
        self.radius = 0

    def area (self):
        return (self.radius ** 2) * pi

    def circumference (self):
        return self.radius * 2 * pi
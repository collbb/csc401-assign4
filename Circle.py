from math import pi

# ClassCircle
# Write class called circle, with an instance variable, for the radius
# and methods to calculate the area and circumference of the circle.
class Circle:
    def __init__(self):
        self.radius = 0

    def area (self):
        return (self.radius ** 2) * pi

    def circumference (self):
        return self.radius * 2 * pi
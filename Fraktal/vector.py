import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def length(self):
        return math.sqrt(self.x**2 + self.y**2)

    def __rmul__(self, other):
        return Vector(self.x*other, self.y*other)

    def __truediv__(self, other):
        return (1/other) * self

    def __neg__(self):
        return -1 * self

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def normalized(self):
        return self / self.length()

    def coordinates(self):
        return (self.x, self.y)

    def rotated(self, angle):
        return Vector(self.x*math.cos(angle) - self.y*math.sin(angle), self.x*math.sin(angle) + self.x*math.cos(angle))

    @classmethod
    def from_polar(cls, r, theta):
        return r * cls(math.cos(theta), math.sin(theta))
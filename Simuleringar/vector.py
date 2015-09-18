import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2)

    def __rmul__(self, other):
        return Vector(self.x*other, self.y*other)

    def __mul__(self, other):
        if type(other) == Vector:
            return self.x*other.x + self.y*other.y
        else:
            raise ValueError("Multiplication with vector.Vector and " + str(type(other)) + " is not supported")

    def __truediv__(self, other):
        return 1/other * self

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y

    def __neg__(self):
        return -1*self

    def __iter__(self):
        return iter((self.x, self.y))

    def normalized(self):
        return self / abs(self)
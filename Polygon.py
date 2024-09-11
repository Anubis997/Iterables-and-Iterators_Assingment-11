import math

class Convex_Polygon:
    def __init__(self, sides, radius):
        self.sides = sides
        self.radius = radius
        # Initialize cached values
        self._interior_angle = None
        self._side_length = None
        self._apothem = None
        self._area = None
        self._perimeter = None

    def __repr__(self):
        return f"Polygon(n={self.sides}, R={self.radius})"

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.sides == other.sides and
                    self.radius == other.radius)
        else:
            return NotImplemented

    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self.sides > other.sides
        else:
            return NotImplemented

    @property
    def interior_angle(self):
        if self._interior_angle is None:
            self._interior_angle = (self.sides - 2) * 180 / self.sides
        return self._interior_angle

    @property
    def side_length(self):
        if self._side_length is None:
            self._side_length = 2 * self.radius * math.sin(math.pi / self.sides)
        return self._side_length

    @property
    def apothem(self):
        if self._apothem is None:
            self._apothem = self.radius * math.cos(math.pi / self.sides)
        return self._apothem

    @property
    def area(self):
        if self._area is None:
            self._area = self.sides * self.side_length * self.apothem / 2
        return self._area

    @property
    def perimeter(self):
        if self._perimeter is None:
            self._perimeter = self.sides * self.side_length
        return self._perimeter

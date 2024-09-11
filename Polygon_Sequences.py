import math
from polygon_class import Convex_Polygon

class custom_Polygon_sequence:
    def __init__(self, max_sides, circumradius):
        self.max_sides = max_sides
        self.circumradius = circumradius

    def __len__(self):
        return self.max_sides - 2

    def __iter__(self):
        return self.PolygonIterator(self.max_sides, self.circumradius)

    def __next__(self):
        if self.current_sides > self.max_sides:
            raise StopIteration
        polygon = Convex_Polygon(self.current_sides, self.circumradius)
        self.current_sides += 1
        return polygon

    def max_efficiency_polygon(self):
        best_polygon = None
        best_efficiency = -float('inf')
        
        for sides in range(3, self.max_sides + 1):
            polygon = Convex_Polygon(sides, self.circumradius)
            efficiency = polygon.area() / polygon.perimeter()
            if efficiency > best_efficiency:
                best_efficiency = efficiency
                best_polygon = polygon
        
        return best_polygon, best_efficiency

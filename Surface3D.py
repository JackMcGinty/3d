from Point3D import *
from Surface2D import *

class Surface3D:
    def __init__(self, points: list[Point3D], color: tuple = (0, 0, 0)):
        self.points = points
        self.color = color

    def project(self) -> Surface2D:
        return Surface2D([Point2D(point.x, point.y) for point in self.points], self.color)
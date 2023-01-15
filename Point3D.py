from Point2D import Point2D

class Point3D:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def project(self) -> Point2D:
        return Point2D(self.x, self.y)


import pygame
if not pygame.get_init():
    pygame.init()

from Point2D import Point2D

class Surface2D:
    def __init__(self, points: list[Point2D], color: tuple = (0, 0, 0)):
        self.points = points
        self.color = color

def draw_surface(dest_surf: pygame.Surface, source_surf: Surface2D):
    pygame.draw.polygon(dest_surf, source_surf.color, [(point.x, point.y) for point in source_surf.points])

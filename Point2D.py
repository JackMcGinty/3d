import pygame
if not pygame.get_init():
    pygame.init()

class Point2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, 1, 1)
    
    # apply velocity and whatnot

    def draw(self, dest_surf: pygame.Surface):
        pygame.draw.rect(dest_surf, (0, 0, 0), self.rect)

def draw_line(dest_surf: pygame.Surface, start_point: Point2D, end_point: Point2D, color = (0, 0, 0), width = 1):
    pygame.draw.line(dest_surf, color, (start_point.x, start_point.y), (end_point.x, end_point.y), width)

def draw_polygon(dest_surf: pygame.Surface, points = list[Point2D], color = (0, 0, 0)):
    pygame.draw.polygon(dest_surf, color, [(point.x, point.y) for point in points])

import pygame
from physics import Gravity, Collision

class Rect:
    def __init__(self, x, y, width, height, color, list = []):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(x, y, width, height)
        self.gravity = Gravity(self, 1)
        self.collision = Collision()
        self.list = list

    def draw(self, surface):
        print("test")
        pygame.draw.rect(surface, self.color, self.rect)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.rect.move_ip(dx, dy)

    def set_position(self, x, y):
        self.x = x
        self.y = y
        self.rect.center = (x, y)

    def set_color(self, color):
        self.color = color

    def get_rect(self):
        return self.rect
    def update(self):
        self.gravity.update()
        from main import platform
        self.collision.checkCollision(self, platform)


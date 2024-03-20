import pygame
from physics import Gravity, Collision

class Rect:
    allRects = []
    def __init__(self, x, y, width, height, color, anchored = True):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(x, y, width, height)
        self.gravity = Gravity(self, 1)
        self.collision = Collision()
        self.anchored = anchored
        Rect.allRects.append(self)

    def draw(self, surface):
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

    def update(self, surface):
        if self.anchored == False:
            self.gravity.update()

        for rect in self.allRects:
            self.collision.checkCollision(self, rect)
        self.draw(surface)

    def seeObj(self):
        print(len(self.allRects))
        for rect in self.allRects:
            print(rect.x, rect.y)


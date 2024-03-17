import pygame
class Gravity:
    def __init__(self, rect, gravity):
        self.rect = rect
        self.gravity = gravity
        self.velocity_y = 0

    def apply_gravity(self):
        if self.velocity_y < 10:
            self.velocity_y += self.gravity
        self.rect.move(0, self.velocity_y)

    def update(self):
        self.apply_gravity()

class Collision:
    def checkCollision(self, rect1, rect2):
        if rect1.rect.colliderect(rect2.rect):
            self.checkXAxis(rect1,rect2)
            self.checkYAxis(rect1,rect2)
        else:
            return False
    def checkXAxis(self, rect1, rect2):
        if rect1.rect.right >= rect2.rect.left and rect1.rect.left <= rect2.rect.right:
            #print("Colliding along the X-axisv")
            return True
        else:
            return False

    def checkYAxis(self, rect1, rect2):
        if rect1.rect.bottom >= rect2.rect.top and rect1.rect.top <= rect2.rect.bottom:
            print("Colliding along the Y-axis")
            rect1.rect.bottom = rect2.rect.top
            #rect1.gravity.gravity = 1
        else:
            return False



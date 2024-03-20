import pygame
class Gravity:
    def __init__(self, rect, gravity):
        self.rect = rect
        self.gravity = gravity
        self.velocity_y = 0
        self.velocity_x = 0

    def apply_gravity(self):
        if self.velocity_y < 10:
            self.velocity_y += self.gravity
            # print(self.velocity_y)
        self.rect.move(0, self.velocity_y)

    def apply_gravityX(self):
        if self.velocity_x < 10:
            self.velocity_x += self.gravity
            # print(self.velocity_y)
        self.rect.move(self.velocity_x, 0)

    def update(self):
        self.apply_gravity()

class Collision:
    def checkCollision(self, rect1, rect2):
        if rect1 is not rect2:
            if rect1.rect.colliderect(rect2.rect):
                self.checkXAxis(rect1,rect2)
                self.checkYAxis(rect1,rect2)
    def checkXAxis(self, rect1, rect2):
        if rect1.rect.right >= rect2.rect.left:
            rect1.rect.right = rect2.rect.left
            #rect1.gravity.velocity_y = 0
            print(rect1.rect.x, rect2.rect.y)
        elif rect1.rect.left <= rect2.rect.right:
            rect1.rect.left = rect2.rect.right
            #rect1.gravity.velocity_y = 0
            print(rect1.rect.x, rect2.rect.y)

    def checkYAxis(self, rect1, rect2):
        if rect1.rect.bottom >= rect2.rect.top and rect1.rect.top <= rect2.rect.bottom:
            # print(rect1 ,"Colliding along the Y-axis with", rect2)
            rect1.rect.bottom = rect2.rect.top
            rect1.gravity.velocity_y = 0
            # rect1.enableGravity = False


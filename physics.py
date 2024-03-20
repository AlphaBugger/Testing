import pygame
class Gravity:
    def __init__(self, rect, gravity):
        self.rect = rect
        self.gravity = gravity
        self.velocity_y = 0
        self.velocity_x = 0
        self.gravity_direction = (0, 1)  # Initial gravity direction: down

    def apply_gravity(self):
        if self.velocity_y < 10:
            self.velocity_y += self.gravity * self.gravity_direction[1]
        self.rect.move_ip(0, self.velocity_y)

    def apply_gravityX(self):
        if self.velocity_x < 10:
            self.velocity_x += self.gravity * self.gravity_direction[0]
        self.rect.move_ip(self.velocity_x, 0)

    def update(self):
        if self.gravity_direction[1]:
            self.apply_gravity()
        else:
            self.apply_gravityX()

    def change_gravity_direction(self, direction):
        self.gravity_direction = direction

class Collision:
    def checkCollision(self, rect1, rect2):
        if rect1 is not rect2:
            if rect1.rect.colliderect(rect2.rect):
                self.checkXAxis(rect1, rect2)
                self.checkYAxis(rect1, rect2)

    def checkXAxis(self, rect1, rect2):
        if rect1.rect.right >= rect2.rect.left and rect1.rect.left <= rect2.rect.right:
            # Handle collision along X-axis
            overlap = min(rect1.rect.right - rect2.rect.left, rect2.rect.right - rect1.rect.left)
            if rect1.gravity.velocity_x > 0:
                # Moving right, adjust to the left
                rect1.rect.right -= overlap
            elif rect1.gravity.velocity_x < 0:
                # Moving left, adjust to the right
                rect1.rect.left += overlap
            rect1.gravity.velocity_x = 0  # Reset X velocity

    def checkYAxis(self, rect1, rect2):
        if rect1.rect.bottom >= rect2.rect.top and rect1.rect.top <= rect2.rect.bottom:
            # Handle collision along Y-axis
            overlap = min(rect1.rect.bottom - rect2.rect.top, rect2.rect.bottom - rect1.rect.top)
            if rect1.gravity.velocity_y > 0:
                # Moving down, adjust up
                rect1.rect.bottom -= overlap
            elif rect1.gravity.velocity_y < 0:
                # Moving up, adjust down
                rect1.rect.top += overlap
            rect1.gravity.velocity_y = 0  # Reset Y velocity

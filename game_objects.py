import random
import pygame

class GameObject():
    x_pos = 0
    y_pos = 0

    def __init__(self, x, y):
        self.x_pos = x
        self.y_pos = y

    def get_pos(self):
        return (self.x_pos, self.y_pos)

    def set_pos(self, x, y):
        self.x_pos = x
        self.y_pos = y

class Paddle(GameObject):  
    P_WIDTH = 25
    P_HEIGHT = 100

    controller = None

    def move(self, x_increment, y_increment):
        self.x_pos += x_increment
        self.y_pos += y_increment

    def set_controller(self, controller):
        self.controller = controller
        controller.set_paddle(self)

    def get_controller(self):
        return self.controller

    def get_rect(self):
        return pygame.Rect(self.x_pos, self.y_pos, self.P_WIDTH, self.P_HEIGHT)

    def draw(self, colour, surface):
        pygame.draw.rect(surface, colour, self.get_rect())

class Ball(GameObject):
    direction = [True, True]

    def __init__(self, x, y):
        GameObject.__init__(self, x, y)
        self.direction[0] = bool(random.getrandbits(1))
        self.direction[1] = bool(random.getrandbits(1))

    def bounce_horizontal(self):
        self.direction[0] = not self.direction[0]
    def bounce_vertical(self):
        self.direction[1] = not self.direction[1]

    def move(self, distance):
        if self.direction[0]:
            self.x_pos += distance
        else:
            self.x_pos -= distance

        if self.direction[1]:
            self.y_pos -= distance
        else:
            self.y_pos += distance

    def reset(self, x, y):
        self.set_pos(x, y)
        self.direction[0] = bool(random.getrandbits(1))
        self.direction[1] = bool(random.getrandbits(1))

    def draw(self, colour, surface):
        pygame.draw.circle(surface, colour, (self.x_pos, self.y_pos), 20, 0)

    def get_direction(self):
        return self.direction
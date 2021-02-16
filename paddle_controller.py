from game_objects import Paddle
import pygame

class PaddleController():
    paddle = None
    ball = None

    def __init__(self, ball):
        self.ball = ball

    def move_direction(self):
        return 0

    def set_paddle(self, paddle):
        self.paddle = paddle


class PlayerController(PaddleController):
    def move_direction(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_UP]:
            return 1
        elif keys[pygame.K_DOWN]:
            return -1
        else:
            return 0

class AIController(PaddleController):
    def move_direction(self):
        target = self.predict_ball_location()
        pos_y = self.paddle.get_pos()[1]

        if target > pos_y:
            return -1
        elif target < pos_y:
            return 1
        else:
            return 0

    def predict_ball_location(self):
        direction = self.ball.get_direction()
        x, y = self.ball.get_pos()

        if direction[0]:
            if direction[1]:
                return -(self.paddle.get_pos()[0] + (Paddle.P_HEIGHT / 2))  + y + x
            else:
                return (self.paddle.get_pos()[0] + (Paddle.P_HEIGHT / 2))  + y - x

        return self.paddle.get_pos()[1]



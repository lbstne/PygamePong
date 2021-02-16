from paddle_controller import AIController, PlayerController
from game_objects import Paddle, Ball
import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

FRAMERATE = 60

SPEED = 5

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_GRAY = (211, 211, 211)
DARK_GRAY = (64, 64, 64)

COLOUR_PRIMARY = BLACK
COLOUR_SECONDARY = LIGHT_GRAY
COLOUR_BKGD = WHITE

window = pygame.display.set_mode([WIDTH, HEIGHT])

player_score = 0
ai_score = 0

ball = Ball(WIDTH / 2, HEIGHT / 2)

player_paddle = Paddle(25, 0)
ai_paddle = Paddle(WIDTH - Paddle.P_WIDTH - 25, 0)

player_controller = PlayerController(ball)
ai_controller = AIController(ball)

player_paddle.set_controller(player_controller)
ai_paddle.set_controller(ai_controller)

paddles = [player_paddle, ai_paddle]

controllers = [player_controller, ai_controller]

game_clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    window.fill(COLOUR_BKGD)
    pygame.draw.rect(window, COLOUR_SECONDARY, (WIDTH / 2 + 3, 0, 6, HEIGHT))

    for paddle in paddles:
        controller = paddle.get_controller()
        move_direction = controller.move_direction()

        y_pos = paddle.get_pos()[1]

        if move_direction == 1 and y_pos >= 0:
            paddle.move(0, -SPEED)
        elif move_direction == -1 and y_pos <= HEIGHT - Paddle.P_HEIGHT:
            paddle.move(0, SPEED)

        if paddle.get_rect().collidepoint(ball.get_pos()):
            ball.bounce_horizontal()
        
        paddle.draw(COLOUR_PRIMARY, window)

    if ball.y_pos > HEIGHT or ball.y_pos < 0:
        ball.bounce_vertical()
            
    if ball.x_pos > WIDTH:
        ball.reset(WIDTH / 2, HEIGHT / 2)
        player_score += 1
    if ball.x_pos < 0:
        ball.reset(WIDTH / 2, HEIGHT / 2)
        ai_score += 1

    ball.move(SPEED * 1.2)
    ball.draw(COLOUR_PRIMARY,window)

    font = pygame.font.SysFont(None, 50)
    player_score_text = font.render("Score: " + str(player_score), True, COLOUR_SECONDARY)
    ai_score_text = font.render("Score: " + str(ai_score), True, COLOUR_SECONDARY)
    window.blit(player_score_text, (20, 20))
    window.blit(ai_score_text, (WIDTH - ai_score_text.get_width() - 20, 20))

    pygame.display.flip()

    game_clock.tick(FRAMERATE)
import pygame
import sys
pygame.init()
WIDTH = 800
HEIGHT = 600
DISPLAY_SURFACE = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball")
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

BALL_RADIUS = 20
ball_position = [WIDTH // 2, HEIGHT // 2]
ball_velocity = [5, 5]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    ball_position[0] += ball_velocity[0]
    ball_position[1] += ball_velocity[1]
    if ball_position[0] + BALL_RADIUS >= WIDTH or ball_position[0] - BALL_RADIUS <= 0:
        ball_velocity[0] *= -1
    if ball_position[1] + BALL_RADIUS >= HEIGHT or ball_position[1] - BALL_RADIUS <= 0:
        ball_velocity[1] *= -1
    DISPLAY_SURFACE.fill(BLACK)
    pygame.draw.circle(DISPLAY_SURFACE, WHITE, ball_position, BALL_RADIUS)
    pygame.display.update()

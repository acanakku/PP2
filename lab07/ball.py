import pygame


pygame.init()


WHITE = (255, 255, 255)
RED = (255, 0, 0)


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


pygame.display.set_caption("Moving Ball")


font = pygame.font.Font(None, 36)

ball_radius = 25
ball_x = (SCREEN_WIDTH - ball_radius) // 2
ball_y = (SCREEN_HEIGHT - ball_radius) // 2
velocity = 20


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if ball_y - velocity >= 0:
                    ball_y -= velocity
            elif event.key == pygame.K_DOWN:
                if ball_y + velocity <= SCREEN_HEIGHT - ball_radius:
                    ball_y += velocity
            elif event.key == pygame.K_LEFT:
                if ball_x - velocity >= 0:
                    ball_x -= velocity
            elif event.key == pygame.K_RIGHT:
                if ball_x + velocity <= SCREEN_WIDTH - ball_radius:
                    ball_x += velocity

 
    screen.fill(WHITE)

 
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

  
    pygame.display.flip()


pygame.quit()

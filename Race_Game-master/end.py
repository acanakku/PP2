import pygame
import sys
from pygame.locals import *

def end_game():
    screen = pygame.display.set_mode((1024, 768))
    win_image = pygame.image.load('images\end.png')  
    screen.blit(win_image, (0, 0))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()


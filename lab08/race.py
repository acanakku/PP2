import pygame
import random


pygame.init()


screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Racer")


white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)


player_width = 50
player_height = 50
player_x = (screen_width - player_width) / 2
player_y = screen_height - player_height - 10


coins = []
coin_width = 20
coin_height = 20


font = pygame.font.SysFont(None, 25)


score = 0


clock = pygame.time.Clock()


def draw_player(x, y):
    pygame.draw.rect(screen, white, [x, y, player_width, player_height])

def draw_coins():
    for coin in coins:
        pygame.draw.rect(screen, yellow, [coin[0], coin[1], coin_width, coin_height])

def collect_coin(player_rect):
    global score
    for coin in coins:
        coin_rect = pygame.Rect(coin[0], coin[1], coin_width, coin_height)
        if player_rect.colliderect(coin_rect):
            coins.remove(coin)
            score += 1

def show_score():
    score_text = font.render("Score: " + str(score), True, white)
    screen.blit(score_text, (screen_width - 100, 10))


running = True
while running:
    screen.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= 5
    if keys[pygame.K_RIGHT]:
        player_x += 5

  
    if player_x < 0:
        player_x = 0
    elif player_x > screen_width - player_width:
        player_x = screen_width - player_width

 
    if random.randint(0, 100) < 3:  
        coin_x = random.randint(0, screen_width - coin_width)
        coin_y = -coin_height
        coins.append([coin_x, coin_y])

   
    for coin in coins:
        coin[1] += 5  
        if coin[1] > screen_height:
            coins.remove(coin)

    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    collect_coin(player_rect)

    draw_player(player_x, player_y)
    draw_coins()
    show_score()

    pygame.display.update()
    clock.tick(60)

pygame.quit()

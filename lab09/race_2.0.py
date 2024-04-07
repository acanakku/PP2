import pygame
import random
import sys


pygame.init()


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Coin Collector")


background_img = pygame.image.load("lab09\images\og.jpg").convert()

player_img = pygame.image.load("lab09\images\orange-car-top-view-95750.png").convert_alpha()
player_img = pygame.transform.scale(player_img, (100, 50))
enemy_img = pygame.image.load("lab09\images\pngtree-top-view-png-image_6193567.png").convert_alpha()
enemy_img = pygame.transform.scale(enemy_img, (100, 50))


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)


player_rect = player_img.get_rect(midbottom=(WIDTH // 2, HEIGHT - 50))


enemy_rect = enemy_img.get_rect(midtop=(random.randint(50, WIDTH - 50), 0))
enemy_speed = 5


coins = []
COIN_SIZES = [(20, 20), (30, 30), (40, 40)]  
COIN_WEIGHTS = [1, 2, 3]  
COIN_SPEED = 5


player_speed = 7
score = 0
COINS_TO_INCREASE_SPEED = 5  


def create_coin():
    size = random.choice(COIN_SIZES)
    weight = random.choice(COIN_WEIGHTS)
    coin = {"rect": pygame.Rect(random.randint(0, WIDTH - size[0]), -size[1], size[0], size[1]), "weight": weight}
    coins.append(coin)


def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))


def check_collision():
    if player_rect.colliderect(enemy_rect):
        return True
    return False


running = True
clock = pygame.time.Clock()

while running:
    screen.blit(background_img, (0, 0))  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT] and player_rect.right < WIDTH:
        player_rect.x += player_speed


    enemy_rect.y += enemy_speed
    if enemy_rect.top > HEIGHT:
        enemy_rect.top = 0
        enemy_rect.centerx = random.randint(50, WIDTH - 50)
    screen.blit(enemy_img, enemy_rect)

   
    screen.blit(player_img, player_rect)

   
    for coin in coins[:]:
        coin["rect"].y += COIN_SPEED
        pygame.draw.rect(screen, YELLOW, coin["rect"])
        if player_rect.colliderect(coin["rect"]):
            score += coin["weight"]
            coins.remove(coin)
        if coin["rect"].top > HEIGHT:
            coins.remove(coin)

    if random.randint(1, 100) < 2:
        create_coin()

    if score >= COINS_TO_INCREASE_SPEED:
        COINS_TO_INCREASE_SPEED += 5  
        enemy_speed += 1


    draw_text(f"Score: {score}", pygame.font.Font(None, 36), WHITE, 10, 10)

 
    if check_collision():
        draw_text("Game Over", pygame.font.Font(None, 72), WHITE, WIDTH // 2 - 150, HEIGHT // 2 - 50)
        pygame.display.flip()
        pygame.time.delay(2000) 
        pygame.quit()
        sys.exit()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

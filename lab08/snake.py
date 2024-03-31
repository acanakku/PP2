import pygame
import random


pygame.init()


screen_width = 800
screen_height = 600
cell_size = 20
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake")


white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)


snake_pos = [random.randrange(1, (screen_width // cell_size)) * cell_size,
             random.randrange(1, (screen_height // cell_size)) * cell_size]
snake_body = [[snake_pos[0], snake_pos[1]],
              [snake_pos[0] - cell_size, snake_pos[1]],
              [snake_pos[0] - (2 * cell_size), snake_pos[1]]]
snake_direction = 'RIGHT'
change_to = snake_direction


food_pos = [random.randrange(1, (screen_width // cell_size)) * cell_size,
            random.randrange(1, (screen_height // cell_size)) * cell_size]


score = 0
level = 1


clock = pygame.time.Clock()


def draw_snake(snake_body):
    for block in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(block[0], block[1], cell_size, cell_size))

def draw_food(food_pos):
    pygame.draw.rect(screen, red, pygame.Rect(food_pos[0], food_pos[1], cell_size, cell_size))

def check_collision(snake_body):
    if snake_body[0][0] < 0 or snake_body[0][0] >= screen_width or \
            snake_body[0][1] < 0 or snake_body[0][1] >= screen_height:
        return True
    for block in snake_body[1:]:
        if snake_body[0][0] == block[0] and snake_body[0][1] == block[1]:
            return True
    return False

def generate_food():
    global food_pos
    food_pos = [random.randrange(1, (screen_width // cell_size)) * cell_size,
                random.randrange(1, (screen_height // cell_size)) * cell_size]
    for block in snake_body:
        if food_pos[0] == block[0] and food_pos[1] == block[1]:
            generate_food()

def display_stats(score, level):
    font = pygame.font.SysFont(None, 25)
    score_text = font.render("Score: " + str(score), True, white)
    level_text = font.render("Level: " + str(level), True, white)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 30))


running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != 'DOWN':
                change_to = 'UP'
            if event.key == pygame.K_DOWN and snake_direction != 'UP':
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT and snake_direction != 'RIGHT':
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT and snake_direction != 'LEFT':
                change_to = 'RIGHT'

    if change_to == 'UP' and snake_direction != 'DOWN':
        snake_direction = 'UP'
    if change_to == 'DOWN' and snake_direction != 'UP':
        snake_direction = 'DOWN'
    if change_to == 'LEFT' and snake_direction != 'RIGHT':
        snake_direction = 'LEFT'
    if change_to == 'RIGHT' and snake_direction != 'LEFT':
        snake_direction = 'RIGHT'

    if snake_direction == 'UP':
        snake_pos[1] -= cell_size
    if snake_direction == 'DOWN':
        snake_pos[1] += cell_size
    if snake_direction == 'LEFT':
        snake_pos[0] -= cell_size
    if snake_direction == 'RIGHT':
        snake_pos[0] += cell_size

    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        if score % 3 == 0:  
            level += 1
        generate_food()
    else:
        snake_body.pop()

    if check_collision(snake_body):
        running = False

    draw_snake(snake_body)
    draw_food(food_pos)
    display_stats(score, level)

    pygame.display.update()
    clock.tick(10 + (level * 2))  

pygame.quit()

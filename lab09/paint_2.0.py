import pygame
import sys
import math

pygame.init()

canvas_width = 800
canvas_height = 600
canvas = pygame.display.set_mode((canvas_width, canvas_height))
pygame.display.set_caption("Paint")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

drawing = False
tool = "pen"
color = BLACK
radius = 5
start_pos = None

# Function to draw different shapes
def draw(shape, color, start, end):
    global radius
    if shape == "pen":
        pygame.draw.line(canvas, color, start, end, radius)
    elif shape == "rectangle":
        pygame.draw.rect(canvas, color, (start[0], start[1], end[0] - start[0], end[1] - start[1]))
    elif shape == "circle":
        pygame.draw.circle(canvas, color, start, int(((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2) ** 0.5))
    elif shape == "square":
        side_length = min(abs(end[0] - start[0]), abs(end[1] - start[1]))
        rect = pygame.Rect(start[0], start[1], side_length, side_length)
        pygame.draw.rect(canvas, color, rect)
    elif shape == "right_triangle":
        width = abs(end[0] - start[0])
        height = abs(end[1] - start[1])
        points = [(start[0], start[1]), (start[0], start[1] + height), (start[0] + width, start[1] + height)]
        pygame.draw.polygon(canvas, color, points)
    elif shape == "equilateral_triangle":
        side_length = min(abs(end[0] - start[0]), abs(end[1] - start[1]))
        half_height = side_length * math.sqrt(3) / 2
        points = [(start[0], start[1]), (start[0] + side_length, start[1]), (start[0] + side_length / 2, start[1] - half_height)]
        pygame.draw.polygon(canvas, color, points)
    elif shape == "rhombus":
        width = abs(end[0] - start[0])
        height = abs(end[1] - start[1])
        points = [(start[0] + width // 2, start[1]), (start[0], start[1] + height // 2), (start[0] + width // 2, start[1] + height), (start[0] + width, start[1] + height // 2)]
        pygame.draw.polygon(canvas, color, points)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            start_pos = event.pos
            drawing = True
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            start_pos = None
        elif event.type == pygame.MOUSEMOTION and drawing:
            end_pos = event.pos
            canvas.fill(WHITE)
            draw(tool, color, start_pos, end_pos)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                tool = "rectangle"
            elif event.key == pygame.K_c:
                tool = "circle"
            elif event.key == pygame.K_e:
                tool = "pen"
            elif event.key == pygame.K_s:
                tool = "square"
            elif event.key == pygame.K_t:
                tool = "right_triangle"
            elif event.key == pygame.K_u:
                tool = "equilateral_triangle"
            elif event.key == pygame.K_d:
                tool = "rhombus"
            elif event.key == pygame.K_1:
                color = BLACK
            elif event.key == pygame.K_2:
                color = RED
            elif event.key == pygame.K_3:
                color = GREEN
            elif event.key == pygame.K_4:
                color = BLUE

    pygame.display.update()

pygame.quit()
sys.exit()

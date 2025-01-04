import numpy
import pygame
import pygame.time
import pygame.draw
import random

# Color codes
# 1 - Red
# 2 - Green
# 3 - Blue
# 4 - Orange
# 5 - Violet

pygame.init()
clock = pygame.time.Clock()
fps = 120

size_columns = 10
size_rows = 10
box_size = 50
screen_width = (size_columns + 2) * box_size
screen_height = (size_rows + 7) * box_size
screen = pygame.display.set_mode((screen_width, screen_height))

field = numpy.zeros((size_rows,size_columns), dtype=int)

# for row in range(size_rows):
#    for column in range(size_columns):
#        field[row][column] = random.randint(1,5)

def draw(field):
    offset_x = box_size
    offset_y = 2*box_size
    for row in range(size_rows):
        for column in range(size_columns):
            if field[row][column] == 0:
                color = (255, 255, 255)
                thickness = 1
            if field[row][column] == 1:
                color = (255, 0, 0)
                thickness = 0
            if field[row][column] == 2:
                color = (0, 255, 0)
                thickness = 0
            if field[row][column] == 3:
                color = (0, 0, 255)
                thickness = 0
            if field[row][column] == 4:
                color = (255, 125, 0)
                thickness = 0
            if field[row][column] == 5:
                color = (238, 130, 238)
                thickness = 0
            pygame.draw.rect(screen, color, (column*box_size + offset_x, 
            row*box_size + offset_y,box_size,box_size), thickness)
            pygame.draw.rect(screen, (255, 255, 255), (column*box_size + offset_x, 
            row*box_size + offset_y,box_size,box_size), 1)


while True:
    clock.tick(fps)
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    draw(field)
    pygame.display.update()

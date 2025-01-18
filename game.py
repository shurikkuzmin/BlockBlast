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

background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background, (screen_width, screen_height))

field = numpy.zeros((size_rows,size_columns), dtype=int)

figures = [
    #  00
    #  00
    [[-1,-1],[-1,0],
     [ 0,-1],[ 0,0]],
    #  000
    #  000
    #  000
    [[-1,-1],[-1,0],[-1,1],
     [ 0,-1],[ 0,0],[ 0,1],
     [ 1,-1],[ 1,0],[ 1,1]],
    #  00
    #  0
    [[-1,-1],[-1,0],[0,-1]],
    #  00
    #   0
    [[-1,0],[-1,1],[0,1]],
    #  0
    #  00
    [[0,-1],[1,-1],[1,0]],
    #   0
    #  00
    [[0,1],[1,0],[1,1]]
]

# for row in range(size_rows):
#    for column in range(size_columns):
#        field[row][column] = random.randint(1,5)

def draw(field):
    offset_x = box_size
    offset_y = 2*box_size
    pygame.draw.rect(screen,(0,0,0,100),(offset_x, offset_y, 
    size_columns*box_size, size_rows*box_size))
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

center_index = random.randint(0, 5)
center_figure = figures[center_index]

left_index = random.randint(0, 5)
left_figure = figures[left_index]

random_figures =[center_figure, left_figure]

def draw_figures():
    random_centers = [((1+size_columns/2)*box_size,
                        int((2+size_rows+2.5)*box_size)), 
                       (int(2.5*box_size),
                        int((2+size_rows+2.5)*box_size))]

    for i in range(2):
        figure = random_figures[i]
        figure_image = pygame.Surface((3*box_size,3*box_size))
        figure_rectangle = pygame.Rect(0,0,3*box_size,3*box_size)
        figure_rectangle.center = random_centers[i]

        for cell in figure:
            x = cell[1]
            y = cell[0]
            pygame.draw.rect(figure_image,(255,255,255),
            ((1+x)*box_size,(1+y)*box_size,box_size,box_size))

        screen.blit(figure_image, figure_rectangle)
    #    print(cell)

while True:
    clock.tick(fps)
    #screen.fill((0,0,0))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    draw(field)
    draw_figures()
    pygame.display.update()

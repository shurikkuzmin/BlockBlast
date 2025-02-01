import numpy
import pygame
import pygame.time
import pygame.draw
import random

# Color codes
# 0 - Black
# 1 - Red
# 2 - Green
# 3 - Blue
# 4 - Orange
# 5 - Violet

colors = [(0,0,0),(255,0,0),(0,255,0),(0,0,255),(255, 125, 0),(238, 130, 238)]

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
    [[0,1],[1,0],[1,1]],
    # 000 
    #  0
    #  0
    [[-1,-1],[-1,0],[-1,1],[0,0],[1,0]],
    #  0
    #  0
    # 000
    [[-1,0],[0,0],[1,-1],[1,0],[1,1]],
    # 0
    # 000
    # 0
    [[-1,-1],[0,-1],[1,-1],[0,0],[0,1]],
    #   0
    # 000
    #   0
    [[0,-1],[0,0],[0,1],[-1,1],[1,1]],
    #
    #000
    #
    [[0,-1],[0,0],[0,1]],
    #  0
    #  0
    #  0
    [[-1,0],[0,0],[1,0]],
    #  00
    # 00
    #
    [[0,-1],[0,0],[-1,0],[-1,1]],
    # 0
    # 00
    #  0
    [[-1,-1],[0,-1],[0,0],[1,0]],
    # 
    # 00
    #  00
    [[0,-1],[0,0],[1,0],[1,1]],
    #  0
    # 00
    # 0
    [[1,-1],[0,-1],[0,0],[1,0]],
    # 000
    # 0
    # 0
    [[-1,-1],[-1,0],[-1,1],[0,-1],[1,-1]],
    # 000
    #   0
    #   0
    [[-1,-1],[-1,0],[-1,1],[0,1],[1,1]],
    #   0
    #   0
    # 000
    [[-1,1],[0,1],[-1,1],[0,1],[1,1]],
    # 0
    # 0
    # 000
    [[-1,-1],[0,-1],[-1,1],[0,1],[1,1]],

]
num_figures = len(figures)

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
                thickness = 1
            else:
                thickness = 0
            color = colors[field[row][column]]
            pygame.draw.rect(screen, color, (column*box_size + offset_x, 
            row*box_size + offset_y,box_size,box_size), thickness)
            pygame.draw.rect(screen, (255, 255, 255), (column*box_size + offset_x, 
            row*box_size + offset_y,box_size,box_size), 1)

random_figures = []
random_centers = []
random_colors = random.sample(range(1,len(colors)),3)
random_indices = random.sample(range(num_figures),3)
offset = 4*box_size
for i in range(3):
    random_index = random_indices[i]
    random_figure = figures[random_index]
    random_figures.append(random_figure)
    y = int((2+size_rows+2.5)*box_size)
    x = (1+size_columns/2)*box_size + (i - 1)*offset
    random_centers.append((x,y))

def draw_figures():
    for i in range(3):
        figure = random_figures[i]
        figure_image = pygame.Surface((3*box_size,3*box_size))
        figure_rectangle = pygame.Rect(0,0,3*box_size,3*box_size)
        figure_rectangle.center = random_centers[i]

        for cell in figure:
            x = cell[1]
            y = cell[0]
            pygame.draw.rect(figure_image,colors[random_colors[i]],
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

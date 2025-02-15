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
    [[-1,1],[0,1],[1,1],[1,-1],[1,0]],
    # 0
    # 0
    # 000
    [[-1,-1],[0,-1],[1,-1],[1,0],[1,1]],
]
num_figures = len(figures)

random_figures = []
random_centers = []
random_rectangles = []
picked_figure = -1
random_colors = random.sample(range(1,len(colors)),3)
random_indices = random.sample(range(num_figures),3)

def draw(field):
    offset_x = box_size
    offset_y = 2*box_size
    pygame.draw.rect(screen,(0,0,0,100),(offset_x, offset_y, 
    size_columns*box_size, size_rows*box_size))
    
    mouse_x, mouse_y = pygame.mouse.get_pos()
    delta_x = mouse_x - offset_x
    delta_y = mouse_y - offset_y
    if delta_x < 0 or delta_x > size_columns * box_size or\
       delta_y < 0 or delta_y > size_rows * box_size:
       ind_x = -1
       ind_y = -1
    else:
        ind_x = int((mouse_x - offset_x) / box_size)
        ind_y = int((mouse_y - offset_y) / box_size)
     
    if ind_x != -1 and ind_y != -1:
        if picked_figure != -1:
            for cell in random_figures[picked_figure]:
                x = ind_x + cell[1]
                y = ind_y + cell[0]
                #if x < 0 or x > size_columns:
        pygame.draw.rect(screen, (255, 182, 193), (ind_x*box_size + offset_x, 
            ind_y*box_size + offset_y,box_size,box_size))

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
        random_rectangles.append(figure_rectangle)

        for cell in figure:
            x = cell[1]
            y = cell[0]
            pygame.draw.rect(figure_image,colors[random_colors[i]],
            ((1+x)*box_size,(1+y)*box_size,box_size,box_size))

        screen.blit(figure_image, figure_rectangle)
    #    print(cell)

def draw_picked_figure():
    if picked_figure == -1:
        return

    mouse_x, mouse_y = pygame.mouse.get_pos()
    for cell in random_figures[picked_figure]:
        x = cell[1]
        y = cell[0]
        little_rect = pygame.Rect((0,0,box_size,box_size))
        little_rect.centerx = mouse_x + x * box_size
        little_rect.centery = mouse_y + y * box_size
        pygame.draw.rect(screen,colors[random_colors[picked_figure]],little_rect)


def determine_figure():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for i in range(3):
        if random_rectangles[i].collidepoint((mouse_x, mouse_y)):
            return i
    return -1

while True:
    clock.tick(fps)
    #screen.fill((0,0,0))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                picked_figure = determine_figure() 

        if event.type == pygame.MOUSEBUTTONUP:
            picked_figure = -1

    draw(field)
    draw_figures()
    draw_picked_figure()
    pygame.display.update()

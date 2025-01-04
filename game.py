import numpy
import pygame
import pygame.time
import pygame.draw
import dis


pygame.init()
clock = pygame.time.Clock()
fps = 120

size_columns = 10
size_rows = 10
box_size = 50
screen_width = size_columns * box_size
screen_height = size_rows * box_size
screen = pygame.display.set_mode((screen_width, screen_height))

field = numpy.zeros((10,10), dtype=int)

def draw(field):
    for row in range(size_rows):
        for column in range(size_columns):
            if field[row][column] == 0:
                pygame.draw.rect(screen,(255,255,255),(column*box_size,row*box_size,box_size,box_size),2)

print(dis.dis(draw))
pass 
while True:
    clock.tick(fps)
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    draw(field)
    pygame.display.update()

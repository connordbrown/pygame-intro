import pygame
from sys import exit

# initialize pygame
pygame.init()
# create display surface (game window)
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
# create clock object to control frame rate
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() # more secure than break
    # draw all elements
    # update everything
    pygame.display.update()
    # set frame rate to 60 fps
    clock.tick(60)
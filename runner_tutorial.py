import pygame
from sys import exit

# initialize pygame
pygame.init()
# create display surface (width, height)
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
# create clock object to control frame rate
clock = pygame.time.Clock()
# create a font
test_font = pygame.font.Font('./font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('graphics/Sky.png')
ground_surface = pygame.image.load('graphics/ground.png')
text_surface = test_font.render('My game', False, 'Black')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() # more secure than break
    # add surfaces to screen
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 50))

    # draw all elements, update everything
    pygame.display.update()
    # set frame rate to 60 fps
    clock.tick(60)
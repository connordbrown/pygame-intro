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

sky_surface = pygame.image.load('graphics/Sky.png').convert() # convert to game pixel format - increase performance
ground_surface = pygame.image.load('graphics/ground.png').convert()
text_surface = test_font.render('My game', False, 'Black')

# snail
snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha() # remove background black and white
snail_x_pos = 800 # initial position

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() # more secure than break
    # add surfaces to screen
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 50))
    screen.blit(snail_surface, (snail_x_pos, 250))
    snail_x_pos -= 4
    if snail_x_pos < -100 : snail_x_pos = 800

    # draw all elements, update everything
    pygame.display.update()
    # set frame rate to 60 fps
    clock.tick(60)
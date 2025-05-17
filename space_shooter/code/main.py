import pygame
from random import randint
from os.path import join

# General set up
pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption('King of Space')

running = True

surface_main = pygame.Surface((100,200))
surface_main.fill('yellow')
xpos = 100
ypos = 200

# Import images
player_surface = pygame.image.load(join('..', 'images', 'player.png')).convert_alpha()
stars_surface = pygame.image.load(join('..', 'images', 'star.png')).convert_alpha()

star_positions = [(randint(0,WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for i in range(20)]


while running:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the game
    display_surface.fill('darkgray')
    xpos += 0.75

     # stars
    for position in star_positions:
        display_surface.blit(stars_surface, position)

    # ship
    display_surface.blit(player_surface,(xpos,150))
    
    pygame.display.update()

pygame.quit()

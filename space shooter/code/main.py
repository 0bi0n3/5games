import pygame
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

# Import image
player_surface = pygame.image.load(join('images', 'player.png')).convert_alpha()

while running:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the game
    display_surface.fill('darkgray')
    xpos += 0.25
    display_surface.blit(player_surface,(xpos,150))
    pygame.display.update()

pygame.quit()

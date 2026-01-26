import pygame, sys
from pygame.locals import *
from settings import *
from button import button

pygame.init()

# setup display
DISPLAYSURF = pygame.display.set_mode((W_WIDTH, W_HEIGHT), 0, 32)
pygame.display.set_caption(GAME_TITLE)

# image
deck_img = pygame.image.load('quiet_shuffle/ui/images/deck_image.png')

# display
DISPLAYSURF.fill(BLACK)
pygame.draw.rect(DISPLAYSURF, WHITE, (245, 70, 300, 442)) # border

def user_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

while True: # main game loop
    user_events()

    DISPLAYSURF.blit(deck_img, (250, 75))
    # button
    button(DISPLAYSURF, 525, "Determine today's vibe")
    button(DISPLAYSURF, 575, "Quit")
    
    pygame.display.update()
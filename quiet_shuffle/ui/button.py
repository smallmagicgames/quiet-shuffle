import pygame
from settings import *

def label(surface, text, pos):
    label = FONT.render(text, 1, BUTTON_TEXT)
    label_rect = label.get_rect()
    label_rect.center = pos
    surface.blit(label, label_rect) 

def button(surface, y_pos, text=None) -> bool:
    rect = pygame.Rect((W_WIDTH//2-BUTTON_SIZE[0]//2, y_pos), BUTTON_SIZE)
    on_button = False
    if rect.collidepoint(pygame.mouse.get_pos()):
        on_button = True
    pygame.draw.rect(surface, WHITE, rect)
    if text is not None:
        label(surface, text, rect.center)
    if on_button and pygame.mouse.get_pressed()[0]:
        return True
    return False
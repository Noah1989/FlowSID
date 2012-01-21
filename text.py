import pygame, palette

def init():
    global font
    pygame.font.init()
    font = pygame.font.Font('OptiSmallBP.fon', 0)

def render(text, color=0x3f, large=False):
    surface = font.render(text, False, palette.color(color))
    if large: surface = pygame.transform.scale2x(surface)    
    sprite = pygame.sprite.Sprite()
    sprite.image = surface
    sprite.rect = sprite.image.get_rect()
    return sprite

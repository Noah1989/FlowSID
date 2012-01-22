import pygame, graphics

class Component(graphics.SimpleSprite):
    
    def __init__(self, width, height):
        graphics.SimpleSprite.__init__(self, width, height)
        self.moving = True
    
    def update(self, frame):
        if self.moving:
            mouse_pos = tuple(x/graphics.scale for x in pygame.mouse.get_pos())
            self.rect.center = mouse_pos    
    
    def mouse_down(self, position, button):
        if button == 1:
            self.moving = False
        elif button == 3:
            self.moving = not self.moving
    
    def mouse_up(self, position, button):
        pass
        
       

import pygame, graphics, palette

class Cursor(graphics.SimpleSprite):
    
    def __init__(self):
        graphics.SimpleSprite.__init__(self, 6, 8)
        points = (0,0),(0,7),(2,5),(5,5)
        pygame.draw.polygon(self.image, palette.color(0x1d), points)
        pygame.draw.polygon(self.image, palette.color(0x00), points, 1)
        self.add(graphics.toplayer)
    
    def update(self, frame):
        if pygame.mouse.get_focused():            
            mouse_pos = tuple(x/graphics.scale for x in pygame.mouse.get_pos())   
            self.rect.topleft = mouse_pos
            self.remove(graphics.invisible)
            self.add(graphics.toplayer)
        else:
            self.remove(graphics.toplayer)
            self.add(graphics.invisible)    

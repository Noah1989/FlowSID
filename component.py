import pygame, graphics, math

class Component(graphics.SimpleSprite):
    
    def __init__(self, width, height):
        graphics.SimpleSprite.__init__(self, width, height)
        self.moving = True
        self.inputs = []
        self.outputs = []
    
    def update(self, frame):
        if self.moving:
            old_pos = self.rect.center
            mouse_pos = tuple(x/graphics.scale for x in pygame.mouse.get_pos())
            self.rect.center = mouse_pos
            while self.rect.center != old_pos and \
                  any(not item.moving for item in
                      pygame.sprite.spritecollide(self, graphics.mainlayer, False)):
                self.rect.center = tuple((sum(x) + math.copysign(1, x[1] - x[0]))/2 
                                          for x in zip(self.rect.center, old_pos))

    def mouse_down(self, position, button):
        if button == 1:
            self.moving = False
        elif button == 3:
            self.moving = not self.moving
    
    def mouse_up(self, position, button):
        pass
        
       

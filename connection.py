import pygame, graphics, palette, wire

class Connection(graphics.SimpleSprite):
    
    def __init__(self):
        graphics.SimpleSprite.__init__(self, 4, 4)
        self.image.fill(palette.color(0x00))
        self.image.fill(palette.color(0x3f), self.rect.inflate(0, -2))
        self.position = 0
        self.add(graphics.wirelayer)
        self._old_rect = None
        
    def mouse_down(self, position, button):
        pass
    
    def mouse_up(self, position, button):
        pass
        
    def update(self, frame):
        if self._old_rect != self.rect:
            self.move()
    
    def move(self):
        pass

class Output(Connection):

    def __init__(self):
        Connection.__init__(self)
        self.wire = wire.Wire()   
        self.wire.set_stop((250, 50))     
        
    def move(self):
        self.wire.set_start(self.rect.topright)
        

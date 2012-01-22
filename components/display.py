import pygame, palette, graphics, text, toolbar, pprint

bg_color = palette.color(0x04)    
text_color = palette.color(0x0c)
light_color = palette.color(0x2e)
dark_color = palette.color(0x19)

class Tool(toolbar.Tool):
    def __init__(self, board):
        toolbar.Tool.__init__(self)
        self.board = board
        pygame.draw.rect(self.image, bg_color, self.rect.inflate(-4, -4))
        symbol = text.render("x:", text_color)
        symbol.rect.topleft = (3, 3)
        self.image.blit(symbol.image, symbol.rect)
    
    def click(self):
        self.board.add_component(Component())
        pass
        
        
class Component(graphics.SimpleSprite):  
    
    def __init__(self):
        graphics.SimpleSprite.__init__(self, 64, 18)
        self.image.fill(bg_color)
        
        pygame.draw.rect(self.image, palette.color(0x00), self.rect)
        
        rect = self.rect.inflate(-3, -3)
        pygame.draw.lines(self.image, dark_color, False, 
                          (rect.topright, rect.bottomright, rect.bottomleft))        
        pygame.draw.lines(self.image, light_color, False, 
                          (rect.bottomleft, rect.topleft, rect.topright))
                          
        rect = self.rect.inflate(-5, -5)
        pygame.draw.lines(self.image, dark_color, False, 
                          (rect.bottomleft, rect.topleft, rect.topright))        
        pygame.draw.lines(self.image, light_color, False, 
                          (rect.topright, rect.bottomright, rect.bottomleft))
        self.image.set_clip(self.rect.inflate(-6, -6))
        
        self.inp(None)
        
        self.moving = True
            
            
    def mouse_down(self, position, button):
        if button == 1:
            self.moving = False
        elif button == 3:
            self.moving = not self.moving
    
    def mouse_up(self, position, button):
        pass
        
    def update(self, frame):
        if self.moving:
            mouse_pos = tuple(x/graphics.scale for x in pygame.mouse.get_pos())
            self.rect.center = mouse_pos            
        
        if self.scroll:
            if self.text.rect.width <= self.rect.width - 8:
                self.text.rect.centerx = self.rect.width / 2
                self.scroll = False
            elif frame%2 == 0:
                if self.text.rect.left >= 5:
                    self.scroll = -1
                elif self.text.rect.right <= self.rect.width - 5:
                    self.scroll = 1
                self.text.rect.move_ip(self.scroll, 0) 
                
            self.image.fill(bg_color)
            self.image.blit(self.text.image, self.text.rect)  
                                                   
            
    def inp(self, value):
        self.text = text.render(pprint.saferepr(value), text_color)
        self.text.rect.topleft = (5, 4)
        self.scroll = True

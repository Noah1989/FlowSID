import pygame, graphics, palette, toolbar, component

# looks good for sizes 3 to 8 
def draw_button(sprite, size, up=True):
    if up:
        color_button = palette.color(0x2a)
        color_light = palette.color(0x3f)
        color_dark = palette.color(0x15)
    else:
        color_button = palette.color(0x15)
        color_light = palette.color(0x00)
        color_dark = palette.color(0x2a)        
    circles = ((color_button, (0, 0), size, 0),               
               (color_dark, (-1, -1), size, 1),
               (color_light, (1, 1), size, 1),
               (color_dark, (0, -1), size, 1),
               (color_light, (0, 1), size, 1),
               (graphics.transparent, (0, 0), size + 1, 1),
               (graphics.transparent, (0, -1), size + 1, 1),
               (graphics.transparent, (0, 1), size + 1, 1),
               (palette.color(0x00), (0, 0), size, 1))               
    for c in circles:        
        pygame.draw.circle(sprite.image, c[0],
                           pygame.Rect(c[1], sprite.rect.size).center, 
                           c[2], c[3])  


class ButtonTool(toolbar.Tool):

    def __init__(self, board):
        toolbar.Tool.__init__(self)
        self.board = board
        draw_button(self, 6)       
    
    def click(self):
        self.board.add_component(ButtonComponent())
        pass        
   
        
class ButtonComponent(component.Component):  
    
    size = 8
    
    def __init__(self):
        component.Component.__init__(self, self.size*2, self.size*2)
        draw_button(self, self.size)
        self.is_down = False
        
    def mouse_down(self, position, button):        
        component.Component.mouse_down(self, position, button)
        if button == 1:
            draw_button(self, self.size, up=False)
            self.is_down = True
    
    def mouse_up(self, position, button):        
        component.Component.mouse_up(self, position, button)
        if self.is_down:
            draw_button(self, self.size, up=True)
            self.is_down = False
                 
    def update(self, frame):
        component.Component.update(self, frame)        
        

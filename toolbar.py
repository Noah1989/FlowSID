import pygame, graphics, palette

iconsize = 16

class Toolbar(graphics.SimpleSprite):

    border = 1
    width = 1*iconsize + 2*border
    height = 8*iconsize + 2*border

    tools = []
    _pressed_tool = None
    
    def __init__(self):
        graphics.SimpleSprite.__init__(self, self.width, self.height)
        self.image.fill(palette.color(0x39))
        pygame.draw.rect(self.image, palette.color(0x24), self.rect, 1)
        self.add(graphics.uilayer)
    
    def add_tool(self, tool):
        self.tools.append(tool)
        self._tool_up(tool)
    
    def mouse_down(self, position, button):
        tool_number = self._tool_number(position)
        if 0 <= tool_number < len(self.tools):
            self._pressed_tool = self.tools[tool_number]
            self._tool_down(self._pressed_tool)
        
    def mouse_up(self, position, button):
        if self._pressed_tool is None: return
        if self._tool_number(position) == self.tools.index(self._pressed_tool):
            self._pressed_tool.click()
        self._tool_up(self._pressed_tool)
        self._pressed_tool = None
    
    def _tool_number(self, position):
        x, y = position
        if not self.border <= x < self.width - self.border: return -1
        if not self.border <= y < self.height - self.border: return -1
        return (y - self.border)/iconsize
    
    def _tool_up(self, tool):
        tool_number = self.tools.index(tool)
        rect = pygame.Rect(self.border, self.border + tool_number*iconsize, 
                           iconsize - 1, iconsize - 1)
        self.image.fill(palette.color(0x2a), rect)
        pygame.draw.lines(self.image, palette.color(0x15), False, 
                          (rect.topright, rect.bottomright, rect.bottomleft))        
        pygame.draw.lines(self.image, palette.color(0x3f), False, 
                          (rect.bottomleft, rect.topleft, rect.topright))
        tool.rect.topleft = rect.topleft
        self.image.blit(tool.image, tool.rect)
                          
    def _tool_down(self, tool):
        tool_number = self.tools.index(tool)
        rect = pygame.Rect(self.border, self.border + tool_number*iconsize, 
                           iconsize - 1, iconsize - 1)
        self.image.fill(palette.color(0x15), rect)
        pygame.draw.lines(self.image, palette.color(0x00), False, 
                          (rect.bottomleft, rect.topleft, rect.topright))
        pygame.draw.lines(self.image, palette.color(0x2a), False, 
                          (rect.topright, rect.bottomright, rect.bottomleft))
        tool.rect.topleft = rect.topleft
        self.image.blit(tool.image, tool.rect)


class Tool(graphics.SimpleSprite):
    
    def __init__(self):
        graphics.SimpleSprite.__init__(self, iconsize, iconsize)
    
    def click(self):
        pass
    

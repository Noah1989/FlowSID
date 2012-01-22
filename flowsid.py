import pygame, graphics, palette, cursor, toolbar, text, components

graphics.init()
text.init()

class UserInterface:

    def __init__(self):
        self.board = Board(self)
        self.clickables = []    
        self.cursor = cursor.Cursor() 
        
        self.toolbar = toolbar.Toolbar()
        self.toolbar.add_tool(components.display.DisplayTool(self.board))
        self.clickables.append(self.toolbar)
        
        infotext = text.render('FlowSID v0.0.1')
        info = pygame.sprite.Sprite()
        info.image = pygame.Surface(infotext.rect.inflate(3, 3).size)
        info.rect = info.image.get_rect()
        info.image.fill(palette.color(0x10))
        pygame.draw.rect(info.image, palette.color(0x20), info.rect, 1)
        infotext.rect.move_ip(2, 2)
        info.image.blit(infotext.image, infotext.rect)
        colors = tuple(palette.color(x) for x in (0x10,0x20,0x30,0x20))
        def update_info(frame):
            info.rect.bottomright = graphics.screen.get_size()
            for x in range(info.rect.width - 2):
                color = colors[(x - 16*len(colors)*frame/255)/2%len(colors)]
                info.image.fill(color, pygame.Rect(x + 1, 1, 1, 1))
                info.image.fill(color, pygame.Rect(info.rect.width - x - 2, 
                                                   info.rect.height - 2, 1, 1))
            
        info.update = update_info
        graphics.uilayer.add(info)

    def event(self, event):    
        if event.type == pygame.MOUSEBUTTONDOWN:
            position = tuple(x/graphics.scale for x in event.pos)
            for clickable in self.clickables:
                if clickable.rect.collidepoint(position):
                    rel_pos = (position[0] - clickable.rect.left,
                               position[1] - clickable.rect.top)
                    clickable.mouse_down(rel_pos, event.button)
                    if clickable in self.board.components:
                        self.clickables.remove(clickable)
                        self.clickables.append(clickable)
                    break
        elif event.type == pygame.MOUSEBUTTONUP:
            position = tuple(x/graphics.scale for x in event.pos)
            for clickable in self.clickables:
                rel_pos = (position[0] - clickable.rect.left,
                           position[1] - clickable.rect.top)
                clickable.mouse_up(rel_pos, event.button)


class Board:
            
    def __init__(self, flowsid):
        self.flowsid = flowsid
        self.components = []
    
    def add_component(self, component):
        self.components.append(component)
        self.flowsid.clickables.append(component)
        graphics.mainlayer.add(component)

if __name__ == "__main__":
    graphics.render_loop(UserInterface().event)

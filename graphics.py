import pygame, palette

scale = 2
transparent = pygame.Color('white')
bg_color = palette.color(0x16)
invisible = pygame.sprite.Group()
mainlayer = pygame.sprite.Group()
wirelayer = pygame.sprite.Group()
uilayer = pygame.sprite.Group()
toplayer = pygame.sprite.Group()

def init():
    pygame.display.init()
    pygame.event.post(pygame.event.Event(pygame.VIDEORESIZE, size=(640, 400)))
    pygame.mouse.set_visible(False)

def render_loop(event_handler):
    global screen
    clock = pygame.time.Clock()
    frame = 0
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.VIDEORESIZE:
                size = tuple(x/scale for x in event.size)
                real_size = tuple(x*scale for x in size)
                real_screen = pygame.display.set_mode(real_size, pygame.RESIZABLE)
                screen = pygame.Surface(size)
            else:
                event_handler(event)
               
        screen.fill(bg_color)
        
        for layer in (invisible, mainlayer, wirelayer, uilayer, toplayer):
            layer.update(frame)
               
        for layer in (mainlayer, wirelayer, uilayer, toplayer):
            layer.draw(screen)
              
        #pygame.transform.scale2x(screen, real_screen)    
        pygame.transform.scale(screen, real_size, real_screen)    
        pygame.display.flip()
        frame = (frame + 1) % 0x100
        clock.tick(50)
        
        
class SimpleSprite(pygame.sprite.Sprite):
  
    def __init__(self, width, height):
        pygame.sprite.Sprite.__init__(self)   
        self.image = pygame.Surface((width, height))
        self.image.set_colorkey(transparent)
        self.image.fill(transparent)
        self.rect = self.image.get_rect()
        
    def update(self, frame):
        pass

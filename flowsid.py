import sys, pygame, palette

pygame.display.init()
pygame.font.init()

scale = 2
pygame.event.post(pygame.event.Event(pygame.VIDEORESIZE, size=(640, 400)))

pygame.mouse.set_visible(False)

font = pygame.font.Font('OptiSmallBP.fon', 0)
def render_text(text, color=0x3f, large=False):
    rendered = font.render(text, False, palette.color(color))
    if large: rendered = pygame.transform.scale2x(rendered)
    return rendered
    
info_text = render_text('FlowSID v0.0.1')

transparent = pygame.Color('white')
def get_surface(width, height):
    surface = pygame.Surface((width, height))
    surface.set_colorkey(transparent)
    surface.fill(transparent)
    return surface

cursor = get_surface(6, 8)
points = (0,0),(0,7),(2,5),(5,5)
pygame.draw.polygon(cursor, palette.color(0x1d), points)
pygame.draw.polygon(cursor, palette.color(0x00), points, 1)

clock = pygame.time.Clock()
frame = 0

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.VIDEORESIZE:
            real_size = event.size
            real_screen = pygame.display.set_mode(real_size, pygame.RESIZABLE)
            size = width, height = tuple(x/scale for x in real_size)
            screen = pygame.Surface(size)

    mouse_pos = tuple(x/scale for x in pygame.mouse.get_pos())
      
    screen.fill(palette.color(0x17))

    screen.blit(info_text, (1, 1))
    if pygame.mouse.get_focused():
        screen.blit(cursor, mouse_pos)    
    pygame.transform.scale(screen, real_size, real_screen)    
    pygame.display.flip()
    frame = (frame + 1) % 0x100
    clock.tick(50)

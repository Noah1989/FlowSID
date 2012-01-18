import pygame

_colors = []
for r in range(4):
    for g in range(4):
        for b in range(4):
            _colors.append(pygame.Color(r * 64, g * 64, b * 64))

def color(index):
    return _colors[index]

if __name__ == "__main__":
    import sys
    from itertools import groupby

    pygame.display.init()
    pygame.font.init()
    pygame.display.set_caption('palette')

    squaresize = 32
    gapsize = 4

    light = lambda color: (color.hsva[2], color.hsva[1])
    lights = sorted(list(set(map(light, _colors))))

    numhues = max(map(lambda g: len(list(g[1])), 
                      groupby(sorted(_colors, key=light), key=light)))
                  
    hue = lambda color: color.hsva[0]/(360.0/numhues) if color.hsva[1] else -1

    width = len(lights)*(squaresize + gapsize) + gapsize
    height = (numhues+1)*(squaresize + gapsize) + gapsize
    size = width, height     
                  
    screen = pygame.display.set_mode(size)
    screen.fill(pygame.Color('white'))

    font = pygame.font.Font('OptiSmallBP.fon', 0)

    for line, (key, group) in enumerate(groupby(sorted(_colors, key=hue), key=hue)):
        for color in group:
            position = lights.index(light(color))
            x = position*(squaresize + gapsize) + gapsize
            y = (key+1)*(squaresize + gapsize) + gapsize
            screen.fill(color, pygame.Rect(x, y, squaresize, squaresize))
            text = "0x%0.2X" % _colors.index(color)
            screen.blit(font.render(text, False, pygame.Color('white')), (x + 1, y))

    clock = pygame.time.Clock()
    pygame.display.flip()
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        clock.tick(10)

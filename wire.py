import pygame, graphics, palette

segment_width = 8

class Wire(pygame.sprite.Group):
       
    def __init__(self):
        pygame.sprite.Group.__init__(self)
        
        
        recent = None
        for x in range(50, 250, segment_width):
            segment = Segment()
            segment.y = 25
            segment.rect.left = x
            if recent:
                segment.left = recent
                recent.right = segment
            self.add(segment)
            recent = segment        
            
        graphics.wirelayer.add(self)

class Segment(pygame.sprite.Sprite):

    surface = pygame.surface.Surface((segment_width, 2))    
    
    images = {}
    
    thickness = 4
    outline_color = palette.color(0x2a)
    fill_color = palette.color(0x3f)
        
    gravity = 0.1
    spring_constant = 0.3
    friction =0.5
    mass = 0.8
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.y = 0
        self.speed = 0
        self.left = None
        self.right = None
        self.nexty = None
        self.rect = pygame.Rect(0, 0, segment_width, 1)
        self.update_size()
    
    def update(self, frame):
        if self.nexty:
            self.y = self.nexty
            self.update_size()
            self.left.update_size()           
             
        if self.left and self.right:
            force = self.gravity
            force += self.spring_constant*(self.left.y + self.right.y - 2*self.y)
            force -= self.friction*self.speed
            self.speed += force/self.mass
            self.nexty = self.y + self.speed  
        if not self.right:
            mouse_pos = tuple(x/graphics.scale for x in pygame.mouse.get_pos())
            self.y = mouse_pos[1]     
            self.rect.top = self.y
            self.left.update_size()   
            
    def update_size(self): 
        if self.right:
            size = int(self.right.y - self.y)
        else:
            size = 0
            
        height = abs(size) + self.thickness
        width = segment_width
        
        if not size in self.images:            
            image = pygame.Surface((width, height))
            image.set_colorkey(graphics.transparent)            
            image.fill(graphics.transparent)
            points = (0, 0), (width - 1, height - self.thickness)            
            for shift in range(self.thickness):
                points1 = tuple((x, y + shift) for x, y in points)
                if size < 0:
                    points1 = tuple((x, height - 1 - y) for x, y in points1)
                if shift in (0, self.thickness-1):
                    color = self.outline_color
                else:
                    color = self.fill_color
                pygame.draw.lines(image, color, False, points1)
                
            self.images[size] = image
            
        self.image = self.images[size]
        self.rect.height = height
        if self.right:
            if self.y < self.right.y:
                self.rect.top = self.y
            else:
                self.rect.top = self.right.y
            

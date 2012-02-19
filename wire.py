import pygame, graphics, palette

segment_width = 8

class Wire():
       
    def __init__(self):        
        segment = Segment()
        self.segments = [segment]
        
        
    def set_start(self, (x, y)):         
        old_stop = self.segments[-1].rect.topright
        self.segments[0].rect.left = x
        self.segments[0].y = y
        for segment in self.segments[1:]:
            segment.rect.left = segment.left.rect.right
        self.set_stop(old_stop)
            
    def set_stop(self, (x, y)):
        for segment in self.segments[1:]:            
            if segment.rect.right > x:
                segment.left.right = None
                segment.kill()
                self.segments.remove(segment)        
        while self.segments[-1].rect.right < x:
            segment = Segment()            
            segment.y = y
            segment.rect.topleft = self.segments[-1].rect.right, y
            segment.left = self.segments[-1]
            segment.update_size()
            self.segments[-1].right = segment 
            self.segments.append(segment)
            segment.left.rect.width = segment_width
        self.segments[-1].y = y
        self.segments[-1].nexty = None        
        self.segments[-1].rect.top = y
        self.segments[-1].rect.width = max(x - self.segments[-1].rect.left, 1)
        self.segments[-1].rect.right = x
        self.segments[-1].update_size()
        graphics.wirelayer.add(self.segments)        

class Segment(pygame.sprite.Sprite):
    
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
            self.rect.top = self.y
                    
        if self.left:
            self.left.update_size()   
            
    def update_size(self): 
        if self.right:
            size = int(self.right.y - self.y)
        else:
            size = 0
            
        height = abs(size) + self.thickness
        width = self.rect.width
        key = (width, size)
        
        if not key in self.images:            
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
                
            self.images[key] = image
            
        self.image = self.images[key]
        self.rect.height = height
        if self.right:
            if self.y < self.right.y:
                self.rect.top = self.y
            else:
                self.rect.top = self.right.y
            

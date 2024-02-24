import pygame as pg
class Planet:
    '''init planet object'''
    def __init__(self, 
                 x:float,
                 y:float, 
                 mass:float, 
                 radius:float, 
                 color:dict[int,int,int],
                 speed_x:float=0,
                 speed_y:float=0,
                 state:bool=True # static planet
                 ):
        
        self.x = x
        self.y = y
        self.mass = mass
        self.radius = radius
        self.color = color
        self.speed = [speed_x,speed_y]
        self.f = [0,0]
        self.status = True
        self.radius = radius
        self.state = state
        
        self.impulse = ...
        self.pot_energy = ...
        self.kin_energy = ...
        
    def update(self):
        '''move planet '''
        if self.state != False:
            self.speed[0] += (self.f[0] / self.mass) #acc
            self.speed[1] += (self.f[1] / self.mass)
            self.x += self.speed[0] 
            self.y += self.speed[1]
    
    def planet(self, screen:dict[int,int]):
        '''draw planet on screen'''
        pg.draw.circle(screen, self.color, ((self.x), (self.y)), self.radius)
    
    
import pygame as pg
import numpy as np
from phy import Physics
from planet import Planet


class Start:
    def __init__(self):
        self.width=1000 
        self.height=1000
        self.center=self.width/2,self.height/2
        self.screen = pg.display.set_mode((self.width,self.height))
        self.running = True
        self.mouse_pos = (0, 0)
        self.lmp = False #Left Mouse pressed (lmb)

    def generator_planet(
        self,n_planet:int,
        planets_array:list,
        mass:float=1,
        radius:float=1,
        color:dict[int,int,int]=[255,255,255]
        ):
        '''generate planet'''

        for _ in range(n_planet):
            __planet = Planet(np.random.randint(1,self.width),#x
                              np.random.randint(1,self.height),#y
                              mass,
                              radius,
                              color,#color
                              np.random.random(),
                              np.random.random()
                              )
            
            planets_array.append(__planet)
    
    def starter(
        self,
        n_planet:int,
        concore_pos_gen_planet:bool,
        mass_planet:float,
        radius_planet:float,
        color_planet:dict[int,int,int],
        collision:bool,
        center_body:bool):
        
        planets = []
        
        if center_body:
            center_planet = Planet(self.center[0],self.center[1],500,10,"yellow",state=False)
            planets.append(center_planet)
        
        if concore_pos_gen_planet:
            self.generator_planet(n_planet=n_planet,planets_array=planets)
        
        
        while self.running:
            for event in pg.event.get(): 
                if event.type == pg.QUIT:
                    self.running = False
                elif event.type == pg.MOUSEBUTTONDOWN:
                    self.mouse_pos = event.pos
                    self.lmp = True
                elif event.type == pg.MOUSEBUTTONUP:
                    self.lmp = False
                elif event.type == pg.MOUSEMOTION:
                    if self.lmp:
                        self.mouse_pos = event.pos 
                
            collides = []
            _planet = []
            
            Physics(planets,collides).update()
            
            if collision: 
                Physics(planets,collides).remove() #collision
            
            if self.lmp:
                planets.append(
                    Planet(self.mouse_pos[0], 
                           self.mouse_pos[1], 
                           mass_planet, 
                           radius_planet, 
                           color_planet, 
                           np.random.random(), 
                           np.random.random()))

            for planet in planets:
                if planet.status:
                    planet.update()
                    planet.f = [0, 0]
                    _planet.append(planet)
                    planet.planet(screen=self.screen)
            planets = _planet
            pg.display.update()
            self.screen.fill([0,0,0])
            
        pg.quit()
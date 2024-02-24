from planet import Planet
   
class Physics:
    '''Move planet'''
    def __init__(self, planet, collides):
        self.planet = planet 
        self.collides = collides
        
    def update(self):
            '''update pos planet'''
            for i in range(len(self.planet)):
                for j in range(i+1,len(self.planet)):
                    p1 = self.planet[i]
                    p2 = self.planet[j]
                    dx = p2.x - p1.x
                    dy = p2.y - p1.y
                    r  = (dx*dx + dy*dy)**0.5
                    f = (p1.mass * p2.mass) / r**3
                    
                    p1.f[0] += f * dx
                    p1.f[1] += f * dy
                    
                    p2.f[0] -= f * dx
                    p2.f[1] -= f * dy
                    if (p1.radius + p2.radius > r): self.collides.append((i,j))
                    
    def remove(self):
        '''remove planet'''
        
        for i in self.collides:
            p1, p2 = self.planet[i[0]], self.planet[i[1]]
            if p1.status and p2.status:
                sum_p_mass = p1.mass + p2.mass
                _planet = Planet(p1.x, p1.y, p1.mass, p1.radius, p1.color) if p1.mass > p2.mass else Planet(p2.x, p2.y, p2.mass, p2.radius, p2.color)
                _planet.speed = [
                    (p1.mass * p1.speed[0] + p2.mass * p2.speed[0]) / (sum_p_mass),
                    (p1.mass * p1.speed[1] + p2.mass * p2.speed[1]) / (sum_p_mass)
                ]
                self.planet.append(_planet)
                p1.status = p2.status = False
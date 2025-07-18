import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    
    def __init__(self ,x ,y, radius):
        super().__init__(x ,y ,radius)

    def draw(self, screen):
        pygame.draw.circle(screen ,
                           (255 ,255 ,255),
                           (self.position),
                           self.radius,
                           2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20,50)
        vel_p = self.velocity.rotate(random_angle)
        vel_n = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        astroid1 = Asteroid(self.position.x ,self.position.y,new_radius)
        astroid1.velocity = vel_p *1.2

        astroid2 = Asteroid(self.position.x ,self.position.y,new_radius)
        astroid2.velocity = vel_n *1.2

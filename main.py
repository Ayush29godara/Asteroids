from re import split
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from shot import Shot

def simple_print():
    print("Starting Asteroids!")
    print("Screen width:",SCREEN_WIDTH)
    print("Screen height:",SCREEN_HEIGHT)
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers  = (updatable,drawable)
    Asteroid.containers = (asteroids ,updatable ,drawable)
    AsteroidField.containers = (updatable)
    CircleShape.containers = (asteroids)
    Shot.containers = (shots,updatable,drawable)
    
    dt = 0

    player = Player( SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    astro_field_obj = AsteroidField()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        
        screen.fill((0,0,0))
        
        for obj in drawable:
            obj.draw(screen)

        for astro in asteroids:
            if astro.Collisions(player) == True:
                sys.exit("Game over!")

        for astro in asteroids:
            for bullet in shots:
                if bullet.Collisions(astro) == True:
                    bullet.kill()
                    astro.split()

        pygame.display.flip()
        
        dt = clock.tick(60) /1000
    simple_print()

if __name__ =="__main__":
    main()

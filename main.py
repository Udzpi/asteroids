import pygame
from constants import *
from logger import log_state
from player import *
from asteroid import *
from asteroidfield import *
from logger import log_event
from shot import Shot
import sys

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH} \nScreen height: {SCREEN_HEIGHT}")
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)
    asteroidField = AsteroidField()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill("black")
    clock = pygame.time.Clock()
    dt = 0.0
    while(True):
        log_state()
        screen.fill((0,0,0))
        updatable.update(dt)
        for elemen in asteroids:
            if player.collides_with(elemen):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            
        for elemnt in drawable:
            elemnt.draw(screen)

        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    shot.kill()
                    asteroid.split()
                    log_event("asteroid_shot")
        for event in pygame.event.get():
            pass
        pygame.display.flip()
        dt = clock.tick(60)/1000
        


if __name__ == "__main__":
    main()

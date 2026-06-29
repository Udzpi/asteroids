from circleshape import CircleShape
import pygame
from constants import *
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, LINE_WIDTH )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            first_asteroid =self.velocity.rotate(angle)
            second_asteroid = self.velocity.rotate(-angle)
            new_rad = self.radius - ASTEROID_MIN_RADIUS
            astOne = Asteroid(self.position.x, self.position.y, new_rad)
            astTwo = Asteroid(self.position.x, self.position.y, new_rad)
            astOne.velocity = first_asteroid *1.2
            astTwo.velocity = second_asteroid *1.2
        
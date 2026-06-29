from circleshape import *
from constants import *
import pygame
from shot import Shot


class Player(CircleShape):
    def __init__(self, x: int, y: int, radius: float):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown = 0.0
        

    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen: pygame.Surface):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def rotate(self, dt: float) -> None:
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()
        self.cooldown -= dt

        if keys[pygame.K_a]:
            left = -1 * dt
            self.rotate(left)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if keys[pygame.K_SPACE] and self.cooldown <= 0:
                self.shoot()
                self.cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS

    def move(self, dt: float) -> float:
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def shoot(self):
        single_shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)

        single_shot.velocity = pygame.Vector2(0, 1)
        single_shot.velocity = single_shot.velocity.rotate(self.rotation)
        single_shot.velocity *= PLAYER_SHOOT_SPEED


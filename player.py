import pygame

from circleshape import *
from constants import *
from shot import Shot

class Player(CircleShape):  # noqa: F405

    timer = 0
    
    def __init__(self, x, y, radius = PLAYER_RADIUS, rotation = 0):
        super().__init__(x, y, radius)
        self.rotation = rotation

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle() , 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.timer -= dt


        if keys[pygame.K_LEFT]:
            self.rotate(dt*-1)
        if keys[pygame.K_RIGHT]:
            self.rotate(dt)
        if keys[pygame.K_UP]:
            self.move(dt)
        if keys[pygame.K_DOWN]:
            self.move(dt*-1)
        if keys[pygame.K_SPACE]:
            print(self.rotation)
            if self.timer < 0 :
                self.shoot(self.rotation)
                self.timer = 0.3

    def shoot(self, direction):
        shot = Shot(self.position.x, self.position.y)
        velocity = pygame.Vector2(0,1).rotate(direction) * PLAYER_SHOOT_SPEED
        shot.velocity = velocity

# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()

    # Create a clock object
    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting asteroids!")

    # creating 2 groups that are updatable and drawable

    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteriod_group = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()

    Player.containers = (updatable_group, drawable_group)
    Asteroid.containers = (asteriod_group, updatable_group, drawable_group)
    AsteroidField.containers = (updatable_group)
    Shot.containers = (shot_group, updatable_group, drawable_group)

    # spawn a new player in the middle of the screen
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x,y)
    ateriodfield = AsteroidField()

    gamePlay = True

    while gamePlay:
        screen.fill((0, 0, 0))  # Fills the screen with black
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gamePlay = False

        for thing in updatable_group:
            thing.update(dt)
        for thing in drawable_group:
            thing.draw(screen)
        for thing in asteriod_group:
            if thing.collision(player):
                print("Game Over!!!")
                gamePlay = False
            for bullit in shot_group:
                if thing.collision(bullit):
                    thing.split()
                    bullit.kill()

        dt = clock.tick(60)/1000

        pygame.display.flip()

if __name__ == "__main__":
    main()
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")






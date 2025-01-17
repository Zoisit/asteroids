import pygame
from constants import *
from player import Player

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    ## setup
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable  = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable , drawable)
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    while(True):
        ## update logic
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt += clock.tick(60) / 1000
        for ua in updatable:
            ua.update(dt)
        #player.update(dt)
        
        #draw
        screen.fill("black")
        for da in drawable:
            da.draw(screen)
        

        #last
        pygame.display.flip()

if __name__ == "__main__":
    main()
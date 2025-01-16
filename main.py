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
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    while(True):
        ## update logic
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt += clock.tick(60) / 1000
        player.update(dt)
        
        #draw
        screen.fill("black")
        player.draw(screen)
        

        #last
        pygame.display.flip()

if __name__ == "__main__":
    main()
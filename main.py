import pygame as pg
import sys
from game import GAME
from variables import *

if __name__ == "__main__":
    pg.init()
    game = GAME()
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
                
    
        screen.fill((0,0,0))
        game.run()
        pg.display.flip()
        clock.tick(60)

        
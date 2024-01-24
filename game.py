import pygame
from player import PLAYER
from variables import *
class GAME:
    def __init__(self):
        player_sprite = PLAYER((screen_width/2,screen_height),screen_width,5)
        self.player = pygame.sprite.GroupSingle(player_sprite)

    def run(self):
        self.player.update()
        self.player.sprite.lasers.draw(screen)
        self.player.draw(screen)
        
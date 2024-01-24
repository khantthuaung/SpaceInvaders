import pygame as pg


screen_width = 500
screen_height = 500
screen = pg.display.set_mode((screen_width,screen_height))
clock = pg.time.Clock()
pg.display.set_caption("Space Invador")
clock.tick(60)
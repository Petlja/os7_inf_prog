# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

(sirina, visina) = (300, 300) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Sest nijansi sive")

# -*- acsection: main -*-

# crtamo 6 kvadrata
pg.draw.rect(prozor, (255, 255, 255), (0,   0, 50, 50))
pg.draw.rect(prozor, (204, 204, 204), (50,  0, 50, 50))
pg.draw.rect(prozor, (153, 153, 153), (100, 0, 50, 50))
pg.draw.rect(prozor, (102, 102, 102), (150, 0, 50, 50))
pg.draw.rect(prozor, (51,  51,  51 ), (200, 0, 50, 50))
pg.draw.rect(prozor, (0,   0,   0  ), (250, 0, 50, 50))

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()

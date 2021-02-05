# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

(sirina, visina) = (300, 50) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Kvadrati u nijansama crvene boje")

# -*- acsection: main -*-

# crtamo 6 kvadrata
pg.draw.rect(prozor, (255, 0, 0), (0,   0, 50, 50))
pg.draw.rect(prozor, (204, 0, 0), (50,  0, 50, 50))
pg.draw.rect(prozor, (153, 0, 0), (100, 0, 50, 50))
pg.draw.rect(prozor, (102, 0, 0), (150, 0, 50, 50))
pg.draw.rect(prozor, (51,  0, 0), (200, 0, 50, 50))
pg.draw.rect(prozor, (0,   0, 0), (250, 0, 50, 50))

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()

# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

(sirina, visina) = (250, 50) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Pet kvadrata u pet boja")

# -*- acsection: main -*-

# crtamo 5 kvadrata
pg.draw.rect(prozor, pg.Color("red"),   (0, 0, 50, 50))
pg.draw.rect(prozor, pg.Color("green"), (50, 0, 50, 50))
pg.draw.rect(prozor, pg.Color("blue"),  (100, 0, 50, 50))
pg.draw.rect(prozor, pg.Color("black"), (150, 0, 50, 50))
pg.draw.rect(prozor, pg.Color("white"), (200, 0, 50, 50))

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()

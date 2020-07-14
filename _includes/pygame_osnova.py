# -*- acsection: general-init -*-
import pygame as pg

pg.init()                             # uključivanje rada biblioteke PyGame
pg.display.set_caption("Pygame")      # podešavamo naslov prozora
(sirina, visina) = (300, 300)         # otvaramo prozor dimenzije 300x300
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-

# -*- acsection: after-main -*-
pg.display.update()   # prikazujemo nacrtano na ekranu

# petlja obrade događaja - čekamo dok korisnik ne isključi prozor
while pg.event.wait().type != pg.QUIT:
    pass

# isključivanje rada biblioteke PyGame
pg.quit()

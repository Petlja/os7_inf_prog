# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

(sirina, visina) = (300, 200) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Pravougaonici")

# -*- acsection: main -*-

# bojimo pozadinu u belo
prozor.fill(pg.Color("white"))

# crtamo crni pravougaonik
pg.draw.rect(prozor, pg.Color("black"), (50, 50, 200, 100), 1)

# crtamo crveni pravougaonik
pg.draw.rect(prozor, pg.Color("red"), (75, 75, 150, 50))

# -*- acsection: after-main -*-

# ažuriramo prikaz sadržaja ekrana
pg.display.update()

# čekamo da korisnik isključi prozor
#while pg.event.wait().type != pg.QUIT:
#    pass

# isključivanje rada biblioteke PyGame
pg.quit()

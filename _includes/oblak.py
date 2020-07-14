# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

(sirina, visina) = (400, 400) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Облак")

# -*- acsection: main -*-

# bojimo pozadinu u plavo
prozor.fill(pg.Color("skyblue"))

# crtamo sunce
pg.draw.circle(prozor, pg.Color("yellow"), (100, 100), 80)

# crtamo oblak od tri kruga
pg.draw.circle(prozor, pg.Color("white"), (200, 200), 80)
pg.draw.circle(prozor, pg.Color("white"), (120, 200), 50)
pg.draw.circle(prozor, pg.Color("white"), (280, 200), 50)

# -*- acsection: after-main -*-

# ažuriramo prikaz sadržaja ekrana
pg.display.update()

# čekamo da korisnik isključi prozor
#while pg.event.wait().type != pg.QUIT:
#    pass

# isključivanje rada biblioteke PyGame
pg.quit()

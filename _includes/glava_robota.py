# -*- acsection: general-init -*-
import pygame as pg

pg.init()  # uključivanje rada biblioteke PyGame
import pygamebg

(sirina, visina) = (300, 300) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Glava robota")

# -*- acsection: main -*-
prozor.fill(pg.Color("white"))
pg.draw.rect(prozor, pg.Color("orange"), (50, 50, 200, 200))
pg.draw.rect(prozor, pg.Color("black"), (90, 90, 40, 40))
pg.draw.rect(prozor, pg.Color("black"), (170, 90, 40, 40))
pg.draw.rect(prozor, pg.Color("black"), (110, 170, 80, 40))
# -*- acsection: after-main -*-

# ažuriramo prikaz sadržaja ekrana
pg.display.update()

# čekamo da korisnik isključi prozor
#while pg.event.wait().type != pg.QUIT:
#    pass

# isključivanje rada biblioteke PyGame
pg.quit()

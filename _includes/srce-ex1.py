# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

(sirina, visina) = (200, 200) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Srce")

# -*- acsection: main -*-

pg.draw.polygon(prozor, pg.Color("red"), [(50, 100), (100, 50), (150, 100), (100, 150)])
pg.draw.circle(prozor, pg.Color("red"), (75, 75), 35)
pg.draw.circle(prozor, pg.Color("red"), (125, 75), 35)

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()

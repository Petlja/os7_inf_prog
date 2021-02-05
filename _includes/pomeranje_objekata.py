# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

(sirina, visina) = (300, 300) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Pomeri objekte")

# -*- acsection: main -*-

prozor.fill(pg.Color("white"))
pg.draw.rect(prozor, pg.Color("red"), (100, 100, 100, 100))
pg.draw.circle(prozor, pg.Color("blue"), (150, 150), 30)
pg.draw.circle(prozor, pg.Color("yellow"), (150, 150), 5)
pg.draw.polygon(prozor, pg.Color("green"), [(100, 100), (200, 100), (150, 50)])

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()

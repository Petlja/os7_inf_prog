# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

(sirina, visina) = (225, 225) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Срце")

# -*- acsection: main -*-

pg.draw.rect(prozor, pg.Color("red"), (0, 75, 150, 150))
pg.draw.circle(prozor, pg.Color("red"), (75, 75), 75)
pg.draw.circle(prozor, pg.Color("red"), (150, 150), 75)

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()

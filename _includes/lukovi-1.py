# -*- acsection: general-init -*-
import math
import pygame as pg
import pygamebg

(sirina, visina) = (300, 300) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Кружни лукови")

# -*- acsection: main -*-

prozor.fill(pg.Color("black"))

(cx, cy) = (sirina // 2, visina // 2)
debljina = 5
r = 80
pg.draw.arc(prozor, pg.Color("red"), (cx-r, cy-r, 2*r, 2*r),
            math.radians(0), math.radians(180), debljina)
r = 70
pg.draw.arc(prozor, pg.Color("blue"), (cx-r, cy-r, 2*r, 2*r),
            math.radians(90), math.radians(270), debljina)
r = 60
pg.draw.arc(prozor, pg.Color("green"), (cx-r, cy-r, 2*r, 2*r),
            math.radians(-180), math.radians(0), debljina)

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()

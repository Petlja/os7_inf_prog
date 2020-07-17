# -*- acsection: general-init -*-
import random
import pygame as pg
import pygamebg

(sirina, visina) = (300, 300) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Ноћно небо")

# -*- acsection: main -*-

# bojimo pozadinu prozora u crno
prozor.fill(pg.Color("black"))

# crtamo mlad mesec pomoću jednog crnog i jednog belog kruga
pg.draw.circle(prozor, pg.Color("white"), (100, 100),  30)
pg.draw.circle(prozor, pg.Color("black"), (120, 100),  30)

# crtamo 100 nasumično raspoređenih zvezdica
for i in range(100):
    # nasumično određujemo koordinate
    x = random.randint(0, sirina)
    y = random.randint(0, visina)
    # crtamo zvezdicu kao mali kružić
    pg.draw.circle(prozor, pg.Color("white"), (x, y), 2)


# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()

# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

(sirina, visina) = (225, 225)  # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Srce")

# -*- acsection: main -*-

treba_crtati = True  # da li treba crtati srce

def crtaj():
    prozor.fill(pg.Color("white"))

    if treba_crtati:
        pg.draw.polygon(prozor, pg.Color("red"), [(50, 100), (100, 50), (150, 100), (100, 150)])
        pg.draw.circle(prozor, pg.Color("red"), (75, 75), 36)
        pg.draw.circle(prozor, pg.Color("red"), (125, 75), 36)

def novi_frejm():
    global treba_crtati
    treba_crtati = not treba_crtati

# -*- acsection: after-main -*-

# animacija poziva funkciju novi_frejm dva puta u sekundi
pygamebg.frame_loop(2, novi_frejm)

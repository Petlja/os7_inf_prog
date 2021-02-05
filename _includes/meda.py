# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

(sirina, visina) = (300, 300) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Medvdic")

# -*- acsection: main -*-

# bojimo pozadinu prozora u belo
prozor.fill(pg.Color("white"))

def uokviren_krug(prozor, boja, centar, poluprecnik):
    pg.draw.circle(prozor, boja, centar, poluprecnik)
    pg.draw.circle(prozor, pg.Color("black"), centar, poluprecnik, 1)
   
uokviren_krug(prozor, pg.Color("yellow"), (90, 80), 45)
uokviren_krug(prozor, pg.Color("yellow"), (210, 80), 45)
uokviren_krug(prozor, pg.Color("yellow"), (150, 150), 100)
uokviren_krug(prozor, pg.Color("yellow"), (150, 200), 50)
uokviren_krug(prozor, pg.Color("black"), (100, 120), 15)
uokviren_krug(prozor, pg.Color("black"), (200, 120), 15)
uokviren_krug(prozor, pg.Color("black"), (150, 170), 15)

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()

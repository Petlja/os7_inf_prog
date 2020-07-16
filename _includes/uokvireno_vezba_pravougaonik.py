# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

(sirina, visina) = (350, 350) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Uokviren krug")

# -*- acsection: main -*-

# bojimo pozadinu prozora u belo
prozor.fill(pg.Color("white"))

def uokviren_pravougaonik(prozor, boja, x, y, sirina, visina):
    pg.draw.rect(prozor, boja, (x, y, sirina, visina))
    pg.draw.rect(prozor, pg.Color("black"), (x, y, sirina, visina), 1)
   
uokviren_pravougaonik(prozor, pg.Color("green"), 50, 50, 100, 50)
uokviren_pravougaonik(prozor, pg.Color("green"), 50, 150, 100, 50)
uokviren_pravougaonik(prozor, pg.Color("green"), 50, 250, 100, 50)

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()

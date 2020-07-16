# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

(sirina, visina) = (350, 200) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Uokviren krug")

# -*- acsection: main -*-

# bojimo pozadinu prozora u belo
prozor.fill(pg.Color("white"))

def uokviren_kvadrat(prozor, boja, x, y, stranica):
    pg.draw.rect(prozor, boja, (x, y, stranica, stranica))
    pg.draw.rect(prozor, pg.Color("black"), (x, y, stranica, stranica), 1)
   
uokviren_kvadrat(prozor, pg.Color("green"), 50, 50, 50)
uokviren_kvadrat(prozor, pg.Color("green"), 150, 50, 50)
uokviren_kvadrat(prozor, pg.Color("green"), 250, 50, 50)

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()

# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

(sirina, visina) = (300, 300) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Правоугаоник у правоугаонику")

# -*- acsection: main -*-

prozor.fill(pg.Color("white"))
pg.draw.rect(prozor, pg.Color("yellow"), (130, 170, 120, 100))
pg.draw.rect(prozor, pg.Color("blue"), (170, 205, 40, 30))
    
# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()

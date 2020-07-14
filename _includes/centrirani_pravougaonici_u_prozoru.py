# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

(sirina, visina) = (300, 300)   # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Центрирани квадрати")

# -*- acsection: main -*-

prozor.fill(pg.Color("white"))
pg.draw.rect(prozor, pg.Color("red"), (50, 50, 200, 200))
pg.draw.rect(prozor, pg.Color("green"), (75, 75, 150, 150))
pg.draw.rect(prozor, pg.Color("blue"), (100, 100, 100, 100))
    
# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()


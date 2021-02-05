# -*- acsection: general-init -*-
import pygame as pg, random
import pygamebg

(sirina, visina) = (300, 300) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Kucica")

# -*- acsection: main -*-

prozor.fill(pg.Color("white"))
pg.draw.rect(prozor, pg.Color("yellow"), (60, 120, 180, 160))
pg.draw.polygon(prozor, pg.Color("red"), [(60, 120), (150, 20), (240, 120)])
pg.draw.rect(prozor, pg.Color("skyblue"), (80, 140, 50, 50))
pg.draw.line(prozor, pg.Color("black"), (80, 165), (130, 165))
pg.draw.line(prozor, pg.Color("black"), (105, 140), (105, 190))
pg.draw.rect(prozor, pg.Color("skyblue"), (170, 140, 50, 50))
pg.draw.line(prozor, pg.Color("black"), (170, 165), (220, 165))
pg.draw.line(prozor, pg.Color("black"), (195, 140), (195, 190))
pg.draw.rect(prozor, pg.Color("brown"), (120, 200, 60, 80))


# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()

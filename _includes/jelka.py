# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

(sirina, visina) = (300, 300) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Јелка")

# -*- acsection: main -*-

# bojimo pozadinu u belo
prozor.fill(pg.Color("white"))

# boje koje cemo koristiti
ZELENA = (0, 100, 36)
BRAON = (97, 26, 9)

# stablo
pg.draw.rect(prozor, BRAON, (130, 250, 40, 50))
# krošnja
pg.draw.polygon(prozor, ZELENA, [(50, 250), (150, 150), (250, 250)])
pg.draw.polygon(prozor, ZELENA, [(75, 200), (150, 100), (225, 200)])
pg.draw.polygon(prozor, ZELENA, [(100, 150), (150, 50), (200, 150)])


# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()

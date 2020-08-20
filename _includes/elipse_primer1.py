# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

# otvaramo prozor
(sirina, visina) = (250, 250)
prozor = pygamebg.open_window(sirina, visina, "Elipse")
# -*- acsection: main -*-

# bojimo pozadinu u belo
prozor.fill(pg.Color("white"))
# debljina linija je 10 piksela
debljina = 10
# vertikalna plava linija dužine 100 piksela
pg.draw.ellipse(prozor, pg.Color("blue"), (50, 50, 50, 80), 5) 
pg.draw.ellipse(prozor, pg.Color("red"), (125, 50, 50, 80))
pg.draw.ellipse(prozor, pg.Color("yellow"), (65, 150, 100, 50))
 
# -*- acsection: after-main -*-
# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()

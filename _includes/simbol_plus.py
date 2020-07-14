# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

# otvaramo prozor
(sirina, visina) = (200, 200)
prozor = pygamebg.open_window(sirina, visina, "Simbol plus")
# -*- acsection: main -*-

# bojimo pozadinu u belo
prozor.fill(pg.Color("white"))
# debljina linija je 10 piksela
debljina = 10
# vertikalna crna linija dužine 100 piksela
pg.draw.line(prozor, pg.Color("black"), (100, 50), (100, 150), debljina)
# horizontalna crna linija dužine 100 piksela
pg.draw.line(prozor, pg.Color("black"), (50, 100), (150, 100), 10)
 
# -*- acsection: after-main -*-
# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()

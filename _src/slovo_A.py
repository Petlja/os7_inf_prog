# -*- acsection: general-init -*-
import pygame as pg
import pygamebg
 
# otvaramo prozor
(sirina, visina) = (200, 200)
prozor = pygamebg.open_window(sirina, visina, "Slovo A")

# -*- acsection: main -*-

# bojimo pozadinu prozora u sivo
prozor.fill(pg.Color("gray"))
 
# debljina linije
debljina = 10
# leva kosa linija
pg.draw.line(prozor, pg.Color("white"), (50, 150), (100, 50), debljina)
# desna kosa linija
pg.draw.line(prozor, pg.Color("white"), (100, 50), (150, 150), debljina)
# horizontalna linija po sredini
pg.draw.line(prozor, pg.Color("white"), (75, 100), (125, 100), debljina)

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()

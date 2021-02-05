# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

(sirina, visina) = (200, 200) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Slovo M")

# -*- acsection: main -*-

# bojimo pozadinu prozora u sivo
prozor.fill(pg.Color("gray"))

# debljina linije
debljina = 10

# horizontalne koordinate tačaka
levo = 50
sredina_x = 100
desno = 150

# vertikalne koordinate tačaka
gore = 50
sredina_y = 120
dole = 150
 
# leva vertikalna linija
pg.draw.line(prozor, pg.Color("white"), (levo, gore), (levo, dole), debljina)
# kosa linija 
pg.draw.line(prozor, pg.Color("white"), (levo, gore), (sredina_x, sredina_y), debljina)
# kosa linija
pg.draw.line(prozor, pg.Color("white"), (sredina_x, sredina_y), (desno, gore), debljina)
# desna vertikalna linija
pg.draw.line(prozor, pg.Color("white"), (desno, gore), (desno, dole), debljina)
 
# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()

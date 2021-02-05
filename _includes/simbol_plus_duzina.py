# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

(sirina, visina) = (200, 200) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Simbol plus promenljive velicine")

# -*- acsection: main -*-

# bojimo pozadinu u belo
prozor.fill(pg.Color("yellow"))
# debljina linija je 10 piksela
debljina = 10
# duzina linija koje čine plus
duzina = 100
# koordinate centra ekrana
(cx, cy) = (sirina / 2, visina / 2)
# vertikalna plava linija
pg.draw.line(prozor, pg.Color("blue"), (cx, cy - duzina/2), (cx, cy + duzina/2), debljina)
# horizontalna crvena linija
pg.draw.line(prozor, pg.Color("red"), (cx - duzina/2, cy), (cx + duzina/2, cy), debljina)
 
# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()

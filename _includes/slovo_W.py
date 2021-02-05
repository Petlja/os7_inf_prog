# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

(sirina, visina) = (200, 200) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Slovo W")

# -*- acsection: main -*-

# bojimo pozadinu u sivo
prozor.fill(pg.Color("gray"))

# debljina linije
debljina = 10

# sredina prozora
sredina = sirina / 2

# jedinična dimenzija slova
dim = 25

# koordinate karakterističnih tačaka
levo1 = sredina - 3*dim
desno1 = sredina + 3*dim
levo2 = sredina - 2*dim
desno2 = sredina + 2*dim
gore = sredina - 2*dim
dole = sredina + 2*dim

Alevo = (levo1, gore)
Adesno = (desno1, gore)
Blevo = (levo2, dole)
Bdesno = (desno2, dole)
C = (sredina, sredina)

# iscrtavamo slovo pomoću duži
pg.draw.line(prozor, pg.Color("white"), Alevo, Blevo, debljina)
pg.draw.line(prozor, pg.Color("white"), Blevo, C, debljina)
pg.draw.line(prozor, pg.Color("white"), C, Bdesno, debljina)
pg.draw.line(prozor, pg.Color("white"), Bdesno, Adesno, debljina)

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()

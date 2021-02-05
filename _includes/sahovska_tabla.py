# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

(sirina, visina) = (400, 400) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Sahovska tabla")

# -*- acsection: main -*-

# bojimo pozadinu u belo
prozor.fill(pg.Color("white"))

# dimenzije table i polja
brojPolja = 8
sirinaPolja = sirina / brojPolja
visinaPolja = visina / brojPolja

# prolazimo kroz sva polja
for i in range(brojPolja):
    for j in range(brojPolja):
        # bojimo crna polja
        if (i + j) % 2 != 0:
            pg.draw.rect(prozor, pg.Color("black"), (i*sirinaPolja, j*visinaPolja, sirinaPolja, visinaPolja))

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()

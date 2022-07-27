# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

(sirina, visina) = (300, 300) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Mackica")

# -*- acsection: main -*-

# bojimo pozadinu u belo
prozor.fill(pg.Color("white"))

# učitavamo sličicu iz datoteke macka.png
slika = pg.image.load("macka.png")
# prikazujemo sličicu na sredini ekrana
(x, y) = ((sirina - slika.get_width()) / 2, (visina - slika.get_height()) / 2)
prozor.blit(slika, (x, y))

# -*- acsection: after-main -*-

# prikazujemo prozor i cekamo da ga korisnik iskljuci
pygamebg.wait_loop()

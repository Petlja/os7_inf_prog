# -*- acsection: general-init -*-
import random
import pygame as pg
import pygamebg

(sirina, visina) = (750, 300) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Кравице")

# -*- acsection: main -*-

# bojimo pozadinu u belo
prozor.fill(pg.Color("white"))
# učitavamo sliku
slika = pg.image.load("kravica.png")
# očitavamo dimenzije slike
(sirina_slike, visina_slike) = (slika.get_width(), slika.get_height())
# pet puta iscrtavamo sliku
for i in range(5):
    prozor.blit(slika, (i*sirina_slike, visina - visina_slike))

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()

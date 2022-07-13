# -*- acsection: general-init -*-
import random
import pygame as pg
import pygamebg

(sirina, visina) = (300, 300) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Macka / Mis")

# -*- acsection: main -*-


# bojimo pozadinu prozora u zeleno
prozor.fill(pg.Color("green"))

macka = True

if macka:
    slika = pg.image.load("macka.png")
    prozor.blit(slika,(150 - slika.get_width()//2, 150 - slika.get_height()//2))
else:
    slika = pg.image.load("mouse.png")
    prozor.blit(slika,(150 - slika.get_width()//2, 150 - slika.get_height()//2))

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()
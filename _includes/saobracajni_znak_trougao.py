# -*- acsection: general-init -*-
import math
import pygame as pg
import pygamebg

(sirina, visina) = (300, 300) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Saobracajni znak")

# -*- acsection: main -*-

def jedakostranicni_trougao(tx, ty, h, boja):
    a = h * 2 / math.sqrt(3)  # dužina stranice
    # koordinate temena - težiste deli visinu u odnosu 1 : 2
    A = (tx - a/2, ty - h/3)
    B = (tx + a/2, ty - h/3)
    C = (tx, ty + 2*h/3)
    pg.draw.polygon(prozor, boja, [A, B, C])
   
# bojimo pozadinu prozora u belo
prozor.fill(pg.Color("white"))
margina = 30
h = visina - 2*margina
(tx, ty) = (sirina / 2, margina + h / 3)
jedakostranicni_trougao(tx, ty, h, pg.Color("red"))
jedakostranicni_trougao(tx, ty, 0.65*h, pg.Color("yellow"))


# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()

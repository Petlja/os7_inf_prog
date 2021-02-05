# -*- acsection: general-init -*-
import math
import pygame as pg
import pygamebg

(sirina, visina) = (500, 300)  # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Auto i avion")

# -*- acsection: main -*-

avion_slika = pg.image.load("avion.png")
(avion_x, avion_y) = (0, 0)
auto_slika = pg.image.load("auto.png")
(auto_x, auto_y) = (0, visina - auto_slika.get_height())

def crtaj():
    prozor.fill(pg.Color("white"))
    prozor.blit(avion_slika, (avion_x, avion_y))
    prozor.blit(auto_slika, (auto_x, auto_y))

def novi_frejm():
    global avion_x, avion_y, auto_x, auto_y

    # pomeramo avion
    avion_x += 2
    if avion_x > sirina:
        avion_x = - avion_slika.get_width()

    # pomeramo auto
    auto_x += 1
    if auto_x > sirina:
        auto_x = - auto_slika.get_width()

    # crtamo scenu
    crtaj()


# -*- acsection: after-main -*-

pygamebg.frame_loop(100, novi_frejm)

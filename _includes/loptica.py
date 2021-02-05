# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

(sirina, visina) = (400, 450)    # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Loptica")

# -*- acsection: main -*-

(x, y) = (sirina // 2, visina // 2) # pozicija loptice (na početku je u centru prozora)
(dx, dy) = (2, 2)  # vektor brzine kretanja loptice
r = 30             # poluprečnik loptice

def crtaj():
    # crtamo lopticu
    prozor.fill(pg.Color("white"))
    pg.draw.circle(prozor, pg.Color("black"), (x, y), r)

def novi_frejm():
    global x, y, dx, dy  # ove promenljive se mogu menjati ovom funkcijom
    # pomeramo lopticu
    x += dx
    y += dy
    # ako je loptica ispala van prozora, menjamo joj smer
    if x - r < 0 or x + r > sirina:
        dx = -dx
    if y - r < 0 or y + r > visina:
        dy = -dy
    crtaj()

# -*- acsection: after-main -*-

pygamebg.frame_loop(100, novi_frejm)

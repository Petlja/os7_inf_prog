# -*- acsection: general-init -*-
import random
import pygame as pg
import pygamebg

(sirina, visina) = (250, 250)   # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Nasumicni krugovi")

# -*- acsection: main -*-

# funkcija koja vraća nasumično određenu boju
def nasumicna_boja():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

r = 20                               # poluprečnik kruga
(x, y) = (sirina // 2, visina // 2)  # u prvom trenutku je krug na centru prozora
boja = nasumicna_boja()              # boju određujemo na nasumičan način

def crtaj():
    prozor.fill(pg.Color("white"))           # bojimo pozadinu u belo
    pg.draw.circle(prozor, boja, (x, y), r)  # crtamo krug

def novi_frejm():
    global x, y, boja  # promenljive koje se menjaju
    # određujemo centar tako da krug ne ispadne van ekrana
    (x, y) = (random.randint(r, sirina - r), random.randint(r, visina - r))
    boja = nasumicna_boja()  # boju određujemo na nasumičan način
    crtaj()

# -*- acsection: after-main -*-

# pokrecemo animaciju tako što funkciju novi_frejm pozivamo 4 puta u sekundi
pygamebg.frame_loop(4, novi_frejm)

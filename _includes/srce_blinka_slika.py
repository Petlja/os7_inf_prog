# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

(sirina, visina) = (200, 181)  # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Srce")

# -*- acsection: main -*-

srce_slika = pg.image.load("srce.png")  # slika srca
treba_crtati = True  # da li treba crtati srce

def crtaj():
    prozor.fill(pg.Color("white"))        # bojimo pozadinu u belo
    if treba_crtati:                      # crtamo srce ako je to potrebno
        prozor.blit(srce_slika, (0, 0))

def novi_frejm():
    global treba_crtati
    treba_crtati = not treba_crtati       # negiramo vrednost treba_crtati
    crtaj()

# -*- acsection: after-main -*-

# animacija poziva funkciju novi_frejm dva puta u sekundi
pygamebg.frame_loop(2, novi_frejm)

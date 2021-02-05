# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

(sirina, visina) = (230, 230)  # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Smajlic i tuzic")

# -*- acsection: main -*-

smajlic_slika = pg.image.load("smajlic.png")
tuzic_slika = pg.image.load("tuzic.png")

smajlic = True  # da li treba crtati smajlića ili tužića

def crtaj():
    prozor.fill(pg.Color("skyblue"))
    if smajlic:
        prozor.blit(smajlic_slika, (0, 0))
    else:
        prozor.blit(tuzic_slika, (0, 0))

def novi_frejm():
    global smajlic
    # smajlic = not smajlic
    if smajlic == True:
        smajlic = False
    else:
        smajlic = True
    crtaj()

# -*- acsection: after-main -*-

# animacija poziva funkciju novi_frejm dva puta u sekundi
pygamebg.frame_loop(2, novi_frejm)

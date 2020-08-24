# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

(sirina, visina) = (400, 400)    # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Бојење круга тастатуром")

# -*- acsection: main -*-

obojen = False   # promenljiva koja određuje da li je krug obojen ili nije

def crtaj():
    debljina = 0 if obojen else 1
    prozor.fill(pg.Color("white"))
    pg.draw.circle(prozor, pg.Color("red"), (200, 200), 100, debljina)

def obradi_dogadjaj(dogadjaj):
    global obojen
    if dogadjaj.type == pg.KEYDOWN:    # prisnut je taster
        obojen = True
        return True
    elif dogadjaj.type == pg.KEYUP:    # otpušten je taster
        obojen = False
        return True
    return False

# -*- acsection: after-main -*-

pygamebg.event_loop(crtaj, obradi_dogadjaj)

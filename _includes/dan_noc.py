# -*- acsection: general-init -*-
import random
import pygame as pg
import pygamebg

(sirina, visina) = (200, 200) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Dan i noc")

# -*- acsection: main -*-

dan = True   # da li je dan ili noć

def crtaj():
    if dan:  # ako je dan
        prozor.fill(pg.Color("skyblue"))                          # plavo nebo
        pg.draw.circle(prozor, pg.Color("yellow"), (50, 50), 40)  # sunce
    else:    # ako je noć
        prozor.fill(pg.Color("black"))                            # crno nebo
        broj_zvezda = 100                                         # zvezde
        for i in range(broj_zvezda):
            x = random.randint(0, sirina)
            y = random.randint(0, visina)
            pg.draw.circle(prozor, pg.Color("white"), (x, y), 2)    

def obradi_dogadjaj(dogadjaj):
    global dan
    if dogadjaj.type == pg.MOUSEBUTTONDOWN: # pritisak dugmeta miša
        dan = not(dan)          # ako je bio dan, sada više nije i obratno
        return True  # treba ponovo crtati
    return False # ne treba ponovo crtati

# -*- acsection: after-main -*-

pygamebg.event_loop(crtaj, obradi_dogadjaj)

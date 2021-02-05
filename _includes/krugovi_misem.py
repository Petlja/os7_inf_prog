# -*- acsection: general-init -*-
import random
import pygame as pg

pg.init()   # uključujemo rad biblioteke PyGame
pg.display.set_caption("Krugovi misem")  # otvaramo prozor
(visina, sirina) = (400, 400)
prozor = pg.display.set_mode((visina, sirina))

# funkcija vraća nasumično određenu boju
def nasumicna_boja():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# -*- acsection: main -*-

krugovi = []

def crtanje():
    prozor.fill(pg.Color("white")) # bojimo pozadinu prozora u belo 
    for (centar, boja) in krugovi: # crtamo sve krugove
        pg.draw.circle(prozor, boja, centar, 30)

def obradi_dogadjaj(dogadjaj):
    if dogadjaj.type == pg.MOUSEBUTTONDOWN:     # pritisak dugmeta miša
        # dodajemo krug nasumične boje sa centrom na poziciji klika mišem
        krugovi.append((dogadjaj.pos, nasumicna_boja()))
        return True
    return False

# -*- acsection: after-main -*-

treba_crtati = True
kraj = False
while not(kraj):
    if treba_crtati:
        crtanje()
        pg.display.update()  # ažuriramo prikaz sadržaja ekrana
        treba_crtati = False # ne treba crtati do daljnjeg

    dogadjaj = pg.event.wait()      # čekamo naredni dogadjaj
    if dogadjaj.type == pg.QUIT:    # isključivanje prozora
        kraj = True
    else:
        treba_crtati = obradi_dogadjaj(dogadjaj)

pg.quit()  # isključivanje rada biblioteke PyGame

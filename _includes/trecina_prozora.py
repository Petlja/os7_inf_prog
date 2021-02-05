# -*- acsection: general-init -*-
import pygame as pg

pg.init()   # uključujemo rad biblioteke PyGame
pg.display.set_caption("Trecina prozora")  # otvaramo prozor
(sirina, visina) = (250, 100)
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-

def crtanje():
    prozor.fill(pg.Color("white")) # bojimo pozadinu prozora u belo
    (x, y) = pg.mouse.get_pos()    # trenutna pozicija miša
    trecina = sirina // 3          # trećina širine prozora
    # određujemo x koordinatu leve ivice pravougaonika koji crtamo
    if x <= trecina:               # ako se nalazimo u prvoj trećini
        levo = 0                   
    elif x <= 2 * trecina:         # ako se nalaziimo u drugoj trećini
        levo = trecina
    else:                          # ako se nalazimo u trećoj trećini
        levo = 2 * trecina
    pg.draw.rect(prozor, pg.Color("blue"), (levo, 0, trecina, visina))

def obradi_dogadjaj(dogadjaj):
    if dogadjaj.type == pg.MOUSEMOTION: # pomeranje miša
        return True # treba ponovo nacrtati scenu
    return False # ne treba ponovo crtati

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

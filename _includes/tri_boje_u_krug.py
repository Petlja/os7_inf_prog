# -*- acsection: general-init -*-
import pygame as pg

pg.init()  # uključivanje rada biblioteke PyGame
pg.display.set_caption("Tri boje u krug")   # otvaramo prozor
(sirina, visina) = (300, 300)
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-

# lista boja koje se redom menjaju: crvena, zelena, plava
boje = [pg.Color("red"), pg.Color("green"), pg.Color("blue")]
broj_boje = 0  # broj tekuće boje pozadine

def crtanje():
    prozor.fill(boje[broj_boje])  # bojimo pozadinu prozora u tekuću boju

def obradi_dogadjaj(dogadjaj):
    global broj_boje
    if dogadjaj.type == pg.MOUSEBUTTONDOWN: # kliknuto je dugme miša
        broj_boje = (broj_boje + 1) % len(boje) # prelazimo na narednu boju
        return True # iniciramo ponovno crtanje
    return False # ne treba ponovo crtati

# -*- acsection: after-main -*-

treba_crtati = True
kraj = False
while not(kraj):
    if treba_crtati:
        crtanje()
        pg.display.update()       # ažuriramo prikaz sadrzaja ekrana
        treba_crtati = False      # nećemo crtati sve dok se ne klikne mišem
    dogadjaj = pg.event.wait()    # čekamo na naredni događaj
    if dogadjaj.type == pg.QUIT:  # isključivanje prozora
        kraj = True
    else:                         # ostali događaji
        treba_crtati = obradi_dogadjaj(dogadjaj)
        
pg.quit() # isključivanje rada biblioteke PyGame

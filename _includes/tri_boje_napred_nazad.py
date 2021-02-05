# -*- acsection: general-init -*-
import pygame as pg

pg.init()  # uključivanje rada biblioteke PyGame
pg.display.set_caption("Tri boje napred-nazad")   # otvaramo prozor
(sirina, visina) = (300, 300)
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-

# lista boja koje se redom menjaju: bela, siva, crna
boje = [pg.Color("white"), pg.Color("gray"), pg.Color("black")]
broj_boje = 0  # broj tekuće boje pozadine
smer = 1       # smer promene boja: 1 unapred, -1 unazad

def crtanje():
    prozor.fill(boje[broj_boje])  # bojimo pozadinu prozora u tekuću boju

def obradi_dogadjaj(dogadjaj):
    global broj_boje, smer
    if dogadjaj.type == pg.MOUSEBUTTONDOWN: # kliknuto je dugme miša
        # ako ne postoji sledeća boja u trenutnom smeru, menjamo smer
        if not(0 <= broj_boje + smer and broj_boje + smer < len(boje)):
            smer = -smer
        broj_boje += smer     # prelazimo na sledeću boju
        return True   # iniciramo ponovno crtanje
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
        treba_crtati =  obradi_dogadjaj(dogadjaj)

pg.quit() # isključivanje rada biblioteke PyGame

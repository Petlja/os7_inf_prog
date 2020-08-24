# -*- acsection: general-init -*-
import random
import pygame as pg

pg.init()  # inicijalizujemo biblioteku pygame

pg.display.set_caption("Кртица")  # otvaramo prozor
(sirina, visina) = (150, 150)
prozor = pg.display.set_mode((sirina, visina))

pg.key.set_repeat(10, 10)  # podešavamo dogadjaje tastature

# -*- acsection: main -*-

slika     = 0 # redni broj slike krtice koja se prikazuje
promena   = 1 # promena tog rednog broja
              # (1 ako se krtica diže, -1 ako se spušta, 0 ako miruje)
preostalo = 0 # preostalo frejmova do promene stanja

# učitavamo u listu slike krtica1.png, ..., krtica10.png
slike = []   # niz u koji dodajemo slike
for i in range(1, 11):
    naziv_slike = "krtica" + str(i) + ".png"  # gradimo naziv slike od delova
    slike.append(pg.image.load(naziv_slike))

def crtaj():
    prozor.fill(pg.Color("white"))     # bojimo pozadinu prozora u belo
    x = 0                              # položaj gornjeg levog ugla slike
    y = visina - slike[slika].get_height()
    prozor.blit(slike[slika], (x, y))  # prikazujemo sliku

def novi_frejm():
    global preostalo, slika, promena

    slika += promena
    if slika == 0 or slika == len(slike) - 1:
        promena = 0

    if preostalo == 0:
        if slika == 0:
            promena = 1
        elif slika == len(slike) - 1:
            promena = -1
        preostalo = 20
    preostalo -= 1  # smanjujemo preostalo vreme

# -*- acsection: after-main -*-

kraj = False
sat = pg.time.Clock()  # sat koji određuje broj frejmova u sekundi
while not kraj:
    # crtamo i ažuriramo sadržaj prozora
    crtaj()
    pg.display.update()

    # proveravamo da li je korisnik isključio prozor
    for dogadjaj in pg.event.get():
        if dogadjaj.type == pg.QUIT:
            kraj = True

    # pauziramo do sledeceg frejma
    sat.tick(10)
    novi_frejm()

pg.quit() # isključujemo rad biblioteke PyGame

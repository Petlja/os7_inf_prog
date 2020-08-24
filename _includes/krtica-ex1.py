# -*- acsection: general-init -*-
import random
import pygame as pg

pg.init()  # inicijalizujemo biblioteku pygame

pg.display.set_caption("Кртица")  # otvaramo prozor
(sirina, visina) = (150, 150)
prozor = pg.display.set_mode((sirina, visina))

pg.key.set_repeat(10, 10)  # podešavamo dogadjaje tastature

# -*- acsection: main -*-

slika   = 0 # redni broj slike koja se prikazuje
promena = 0 # promena tog rednog broja
            # (1 ako se krtica diže, -1 ako se spušta, 0 ako miruje)

# učitavamo u listu slike krtica1.png, ..., krtica10.png
slike = []   # niz u koji dodajemo slike
for i in range(1, 11):
    naziv_slike = "krtica" + str(i) + ".png"  # gradimo naziv slike od delova
    slike.append(pg.image.load(naziv_slike))

def crtaj():
    prozor.fill(pg.Color("white"))     # bojimo pozadinu prozora u belo
    (x, y) = (0, visina - slike[slika].get_height())  # položaj gornjeg levog ugla slike
    prozor.blit(slike[slika], (x, y))  # prikazujemo sliku

def novi_frejm():
    global slika, promena

    slika += promena # pomeramo krticu
    if slika == 0 or slika == len(slike) - 1: # ako je u rupi ili na površini
        promena = 0 # zaustavljamo je

    if promena == 0: # ako je krtica zaustavljena
        if slika == 0: # ako se krtica nalazi u rupi
            if random.randint(1, 20) == 1: # sa verovatnoćom 1/20
                promena = 1  # kreće da se diže
        if slika == len(slike) - 1: # ako se krtica nalazi na površini
            if random.randint(1, 40) == 1: # sa verovatnoćom 1/40
                promena = -1  # kreće da se spušta

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

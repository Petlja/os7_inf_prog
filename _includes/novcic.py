# -*- acsection: general-init -*-
import random
import pygame as pg

pg.init()  # inicijalizujemo biblioteku pygame

pg.display.set_caption("Novcic")  # otvaramo prozor
(sirina, visina) = (222, 227)
prozor = pg.display.set_mode((sirina, visina))

pg.key.set_repeat(10, 10)  # podešavamo dogadjaje tastature

# -*- acsection: main -*-

# učitavamo u listu slike novčića (od glave do sredine, pa od sredine do pisma)
slike = []   # niz u koji dodajemo slike
for i in range(0, 11):
    naziv_slike = "5dinara_glava" + str(i) + ".jpeg"  # gradimo naziv slike od delova
    slika = pg.image.load(naziv_slike)
    slike.append(slika)

for i in range(10, -1, -1):
    naziv_slike = "5dinara_pismo" + str(i) + ".jpeg"  # gradimo naziv slike od delova
    slika = pg.image.load(naziv_slike)
    slike.append(slika)

slika = 0        # indeks tekuće slike
uvecanje = 0     # smer promene slike
vrti_se = False  # da li se novčić trenutno vrti

def crtaj():
    prozor.fill(pg.Color("white"))     # bojimo pozadinu prozora u belo
    prozor.blit(slike[slika], (0, 0))  # prikazujemo sliku

def novi_frejm():
    global slika, uvecanje, vrti_se
    slika += uvecanje                                      # menjamo sliku
    if slika == len(slike) - 1:                            # ako smo stigli do slike pisma
        if not vrti_se or random.randint(1, 5) == 1:       #   zaustavljamo promenu sa verovatnoćom 20%
            uvecanje = 0
            vrti_se = False
        else:                                              #   u suprotnom
            uvecanje = -1                                  #      nasavljamo da se vrtimo, ali sada ka slici glave
    if slika == 0:                                         # ako smo stigli do slike glave
        if not vrti_se or random.randint(1, 5) == 1:       #   zaustavljamo promenu sa verovatnoćom 20%
            uvecanje = 0                                   
            vrti_se = False
        else:                                              #   u suprotnom
            uvecanje = 1                                   #      nastavljamo da se vrtimo, ali sada ka slici pisma

def obradi_dogadjaj(dogadjaj):
    global uvecanje, vrti_se
    if dogadjaj.type == pg.MOUSEBUTTONDOWN:     # klik mišem
        if slika == 0:                          #   ako je prikazana slika glave
            uvecanje = 1                        #       krećemo ka slici pisma
        if slika == len(slike) - 1:             #   ako je prikazana slika pisma 
            uvecanje = -1;                      #       krećemo ka slici glave
        vrti_se = True                          #   novcic je krenuo da se vrti

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
        else:
            obradi_dogadjaj(dogadjaj)

    # pauziramo do sledeceg frejma
    sat.tick(100)
    novi_frejm()

pg.quit() # isključujemo rad biblioteke PyGame

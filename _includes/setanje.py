# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

(sirina, visina) = (300, 190)  # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Шетање")

pg.key.set_repeat(10, 10)  # podešavamo dogadjaje tastature

# -*- acsection: main -*-

# učitavamo u listu slike setanje1.png, setanje2.png, ..., setanje5.png
slike_unapred = []   # niz u koji dodajemo slike
slike_unazad = []   # niz u koji dodajemo slike
for i in range(1, 6):
    naziv_slike = "setanje" + str(i) + ".png"  # gradimo naziv slike od delova
    slika = pg.image.load(naziv_slike)
    slike_unapred.append(slika)
    slike_unazad.append(pg.transform.flip(slika, True, False))  # pravimo sliku u ogledalu
slike = slike_unapred

slika = 0   # indeks tekuće slike
x = 0       # x-koordinata leve ivice slike
cilj_x = 0  # x-koordinata do koje treba da stigne leva ivica slike

def crtaj():
    prozor.fill(pg.Color("white"))                          # bojimo pozadinu prozora u belo
    prozor.blit(slike[slika], (x, 0))                       # prikazujemo sliku
    # crtamo platformu
    cilj_sredina_x = cilj_x + slike[slika].get_width() / 2  # x koordinata sredine slike - sredina platforme
    pg.draw.line(prozor, pg.Color("black"), (cilj_sredina_x - 20, visina - 5), (cilj_sredina_x + 20, visina - 5), 10)

def novi_frejm():
    global slika, x
    if x < cilj_x:                        # ako je lik levo od platforme
        x += 4                            #   pomeramo ga 4 piksela nadesno
        slika = (slika + 1) % len(slike)  #   prelazimo na sledeću sliku
    elif x > cilj_x:                      # ako je lik desno od platforme
        x -= 4                            #   pomeramo ga 4 piksela nalevo
        slika = (slika + 1) % len(slike)  #   prelazimo na sledeću sliku
    crtaj()

def obradi_dogadjaj(dogadjaj):
    global cilj_x, slike
    if dogadjaj.type == pg.KEYDOWN:
        if dogadjaj.key == pg.K_RIGHT:                        # strelica na desno
            if cilj_x + slike[slika].get_width() <= sirina:   #   ako desna ivica slike ne ispada van desnog dela ekrana
                cilj_x += 20                                  #     pomeramo platformu 20 piksela nadesno
                slike = slike_unapred                         #     lik je okrenut nadesno
        elif dogadjaj.key == pg.K_LEFT:                       # strelica na levo
            if cilj_x >= 0:                                   #   ako leva ivica slike ne ispada van levog dela ekrana
                cilj_x -= 20                                  #     pomeramo platformu 20 piksela nalevo
                slike = slike_unazad                          #     lik je okrenut nalevo
    crtaj()

# -*- acsection: after-main -*-

pygamebg.frame_loop(7, novi_frejm, obradi_dogadjaj)

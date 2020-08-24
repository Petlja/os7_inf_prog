# -*- acsection: general-init -*-
import random
import pygame as pg
import pygamebg

(sirina, visina) = (800, 400)  # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Корњача и зец")

# -*- acsection: main -*-

kornjaca_slika = pg.image.load("kornjaca.png")                                      # slika kornjače
(kornjaca_x, kornjaca_y) = (0, visina - kornjaca_slika.get_height())                # pozicija njenog gornjeg levog ugla
zec_slika = pg.image.load("zec.png")                                                # slika zeca
(zec_x, zec_y) = (sirina - zec_slika.get_width(), visina - zec_slika.get_height())  # pozicija njenog gornjeg levog ugla

# funkcija koja ispisuje tekst tako da mu je centar na datoj poziciji
def centriraj_tekst(tekst, x, y):
    font = pg.font.SysFont("Arial", 40)                                       # font kojim se ispisuje tekst
    tekst = font.render(tekst, True, pg.Color("white"))                       # sličica koja sadrži ispisan tekst
    (sirina_teksta, visina_teksta) = (tekst.get_width(), tekst.get_height())  # dimenzije te sličice
    (x, y) = (x - sirina_teksta / 2, y - visina_teksta / 2)                   # koordinate gornjeg levog ugla
    prozor.blit(tekst, (x, y))                                                # prikazujemo tekst

# funkcija koja proverava da li su se sreli
def sreli_su_se():
    desni_kraj_kornjace = kornjaca_x + kornjaca_slika.get_width()  # desni kraj slike kornjače
    levi_kraj_zeca = zec_x                                         # levi kraj slike zeca
    return desni_kraj_kornjace >= levi_kraj_zeca                   # proveravamo da li su se mimiošli

def crtaj():
    pg.draw.rect(prozor, pg.Color("skyblue"), (0, 0, sirina, visina / 2))            # crtamo nebo
    pg.draw.rect(prozor, pg.Color("forestgreen"), (0, visina / 2, sirina, visina))   # crtamo zemlju
    pg.draw.circle(prozor, pg.Color("yellow"), (80, 80), 60)                         # crtamo sunce
    prozor.blit(kornjaca_slika, (kornjaca_x, kornjaca_y))                            # prikazujemo sliku kornjače
    prozor.blit(zec_slika, (zec_x, zec_y))                                           # prikazujemo sliku zeca
    if sreli_su_se():                                                                # ako su se sreli
        centriraj_tekst("Здраво", sirina / 2, visina / 3)                            #   prikazujemo tekst

def novi_frejm():
    global zec_x, kornjaca_x
    if not sreli_su_se():     # ako se nisu sreli
        kornjaca_x += 1       #    pomeramo kornjaču jedan piksel nadesno
        zec_x -= 2            #    pomeramo zeca dva piksela nalevo
        crtaj()

# -*- acsection: after-main -*-

pygamebg.frame_loop(30, novi_frejm)

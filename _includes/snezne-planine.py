# -*- acsection: general-init -*-
import random
import pygame as pg

import pygamebg

(sirina, visina) = (800, 400) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Врхови планина под снегом")

# -*- acsection: main -*-

# bojimo pozadinu prozora u svetlo plavo
PLAVA = [100, 100, 255]
prozor.fill(PLAVA)

# ukupan broj planina na slici
broj_planina = 5
# sirina jedne planine (sve planine su iste sirine)
sirina_planine = sirina / broj_planina
# crtamo jednu po jednu planinu
for i in range(broj_planina):
    # x koordinata pocetka tekuce planine
    pocetak_planine_x = i*sirina_planine
    # y koordinata vrha planine (obavezno iznad sredine prozora)
    vrh_planine_y = random.randint(0, visina / 2)
    # tri temena planine - levi kraj podnozja, vrh i desni kraj podnozja
    levo  = (pocetak_planine_x, visina)
    vrh   = (pocetak_planine_x + sirina_planine / 2, vrh_planine_y)
    desno = (pocetak_planine_x + sirina_planine, visina)
    # crtamo planinu pomocu poligona
    pg.draw.polygon(prozor, pg.Color("green"), [levo, vrh, desno])
  
    # visina snega (od vrha planine do dna snega)
    visina_snega = random.randint(visina / 4, visina / 2)
    # y koordinata dna snega
    dno_snega_y = vrh_planine_y + visina_snega
    # visina cele planine
    visina_planine = visina - vrh_planine_y
    # sirina snega (na osnovu slicnosti trouglova)
    sirina_snega = sirina_planine / visina_planine * visina_snega
    # x koordinata podnozja sneznog pokrivaca
    pocetak_snega_x = pocetak_planine_x + (sirina_planine - sirina_snega) / 2
    # tri temena snega - levi kraj podnozja snega, vrh planine i desni kraj podnozja snega
    levo_sneg  = (pocetak_snega_x, dno_snega_y)
    desno_sneg = (pocetak_snega_x + sirina_snega, dno_snega_y)
    pg.draw.polygon(prozor, pg.Color("white"),  [levo_sneg, vrh, desno_sneg])

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()

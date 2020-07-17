# -*- acsection: general-init -*-
import random
import pygame as pg
import pygamebg

(sirina, visina) = (800, 400) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Врхови планина")

# -*- acsection: main -*-

# bojimo pozadinu prozora u belo
prozor.fill(pg.Color("white"))

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
    # tri temena planine
    levo  = (pocetak_planine_x, visina)
    vrh   = (pocetak_planine_x + sirina_planine / 2, vrh_planine_y)
    desno = (pocetak_planine_x + sirina_planine, visina)
    # crtamo planinu pomocu dve duzi
    pg.draw.line(prozor, pg.Color("black"), levo, vrh, 3)
    pg.draw.line(prozor, pg.Color("black"), vrh, desno, 3)

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()

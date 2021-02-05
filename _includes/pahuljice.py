# -*- acsection: general-init -*-
import random
import pygame as pg
import pygamebg

(sirina, visina) = (800, 400)  # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Pahuljice")

# -*- acsection: main -*-

pahulja_slika = pg.image.load("pahulja.png")  # slika pahuljice
broj_pahulja = 10                             # ukupan broj pahuljica
# nasumično generišemo centre pahuljica
centri_pahulja = [(random.randint(0, sirina), random.randint(0, visina))
                  for i in range(broj_pahulja)]

def crtaj():
    prozor.fill(pg.Color("white"))    # bojimo pozadinu u belo
    dim = pahulja_slika.get_width()   # dimenzije slike pahulje
    for (x, y) in centri_pahulja:     # crtamo sve pahulje
        prozor.blit(pahulja_slika, (x - dim / 2, y - dim / 2))

def novi_frejm():
    global centri_pahulja

    # pomeramo pahulje i u listi ostavljamo samo one koje još nisu ispale
    centri_pahulja = [(x, y+1) for (x, y) in centri_pahulja if y - pahulja_slika.get_height() / 2 < visina]
    # popunjavamo prazna mesta novih pahuljama koje kreću da padaju iznad vrha ekrana
    while len(centri_pahulja) < broj_pahulja:
        centri_pahulja.append((random.randint(0, sirina),
                               random.randint(-round(0.2 * visina), 0)))

    # iscrtavamo ponovo scenu
    crtaj()

# -*- acsection: after-main -*-

pygamebg.frame_loop(50, novi_frejm)

# -*- acsection: general-init -*-
import random, math
import pygame as pg
import pygamebg

(sirina, visina) = (400, 400)  # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Лептир прати миша")

# -*- acsection: main -*-

# učitavamo dve slike leptira u listu
leptir_slike = []
for i in range(2):
    naziv_slike = "leptir" + str(i+1) + ".png"
    leptir_slike.append(pg.image.load(naziv_slike))

broj_frejma = 0 # redni broj tekućeg frejma

def crtaj():
    prozor.fill(pg.Color("white"))                        # bojimo pozadinu u belo
    (mis_x, mis_y) = pg.mouse.get_pos()                   # koordinate miša
    broj_slike = (broj_frejma // 10) % len(leptir_slike)  # redni broj slike - svaka se slika prikazuje 10 frejmova
    slika = leptir_slike[broj_slike]                      # slika koja se prikazuje
    slika_sirina = slika.get_width()                      # prikazujemo sliku centrirano
    slika_visina = slika.get_height()
    (x, y) = (mis_x - slika_sirina / 2, mis_y - slika_visina / 2)
    prozor.blit(slika, (x, y))

def novi_frejm():
    global broj_frejma
    broj_frejma += 1    # uvećavamo redni broj frejma
    crtaj()

# -*- acsection: after-main -*-

pygamebg.frame_loop(50, novi_frejm)

# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

(sirina, visina) = (400, 400)  # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Automobil")

# -*- acsection: main -*-

auto_slika = pg.image.load("auto.png")   # slika automobila
(sirina_auta, visina_auta) = (auto_slika.get_width(), auto_slika.get_height()) # dimenzije slike automobila

auto_v = 100                   # brzina automobila (broj piksela u sekundi)
auto_x = 0                     # početni polozaj - x koordinata
auto_y = visina - visina_auta  # početni polozaj - y koordinata
frejmova_u_sekundi = 50
dt = 1 / frejmova_u_sekundi

def crtaj():
    prozor.fill(pg.Color("skyblue"))            # bojimo pozadinu u nebo-plavu
    prozor.blit(auto_slika, (auto_x, auto_y))   # prikazujemo sliku auta

def novi_frejm():
    global auto_x               # menjaćemo horizontalni položaj auta
    auto_x += auto_v * dt       # pomeramo auto nadesno
    if auto_x > sirina:         # ako je ispao van prozora
        auto_x = - sirina_auta  #     vraćamo ga na početak
    crtaj()

# -*- acsection: after-main -*-

pygamebg.frame_loop(frejmova_u_sekundi, novi_frejm)

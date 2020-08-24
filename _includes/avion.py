# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

(sirina, visina) = (800, 400)    # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Авион")

# -*- acsection: main -*-

sunce_slika = pg.image.load("sunce.png")   # slika sunca
avion_slika = pg.image.load("avion.png")   # slika aviona
avion_visina = avion_slika.get_height()    # visina slike aviona

(avion_x, avion_y) = (0, visina - avion_visina) # položaj aviona
avion_dy = -1                                   # vertikalna brzina - avion se prvo diže

def crtaj():
    prozor.fill(pg.Color("skyblue"))               # bojimo pozadinu u plavo
    prozor.blit(avion_slika, (avion_x, avion_y))   # crtamo avion
    prozor.blit(sunce_slika, (0, 0))               # crtamo sunce

def novi_frejm():
    global avion_x, avion_y, avion_dy        # menjamo položaj i smer kretanja aviona
    avion_x += 1                             # pomeramo avion na desno
    avion_y += avion_dy                      # menjamo mu visinu
    if avion_y < 0:                          # ako je dodirnuo vrh ekrana
        avion_dy = 1                         # menjamo mu smer tako da počne da se spušta
    if avion_y + avion_visina == visina:     # ako je dodirnuo dno ekrana
        avion_dy = 0                         # prestaje da menja visinu
    crtaj()

# -*- acsection: after-main -*-

pygamebg.frame_loop(50, novi_frejm)

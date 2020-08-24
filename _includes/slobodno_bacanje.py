# -*- acsection: general-init -*-
import math
import pygame as pg
import pygamebg

(sirina, visina) = (800, 480) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "PyGame")

# -*- acsection: main -*-

kos = pg.image.load('kos.png')
lopta = pg.image.load('lopta.png')
mrezica = pg.image.load('mrezica.png')
petlja = pg.image.load('petlja_logo.png')
pygame = pg.image.load('pygame_logo.png')

g     = 9.81     # gravitaciona konstanta - 9.81 metara u sekundi po sekundi
t     = 0        # đule se ispucava u trenutku t = 0 sekundi
v0    = 9.2      # pocetna brzina u metrima po sekundi
alpha = 52       # ugao ispucavanja u stepenima
H = 3            # visina kosa u metrima
h = 1.95         # visina igraca u metrima
d = 7.2          # udaljenost linije slobodnih bacanja u metrima
(x, y) = (x0, y0) = (0, h)  # početni položaj je na mestu ispucavanja
v0x  = v0 * math.cos(math.radians(alpha)) # horizontalna brzina
v0y  = v0 * math.sin(math.radians(alpha)) # vertikalna brzina
dt = 0.01  # vremenski interval između dva susedna frejma

def crtaj():
    prozor.fill(pg.Color("white"))  # bojimo pozadinu u belo

    ppm = 90 # broj piksela po metru

    # ekranske koordinate centra kosa
    kos_xe = ppm * d
    kos_ye = visina - ppm * H

    # koordinate gornje leve ivice slike kosa
    kos_x0 = kos_xe - (1/3) * kos.get_width()
    kos_y0 = kos_ye - (2/3) * kos.get_height()

    # crtamo kos
    prozor.blit(kos, (kos_x0, kos_y0))

    # ekranske koordinate centra lopte
    lopta_xe = ppm * x
    lopta_ye = visina - ppm * y

    # koordinate gornje leve ivice centra lopte
    lopta_x0 = lopta_xe - lopta.get_width() / 2
    lopta_y0 = lopta_ye - lopta.get_height() / 2

    # crtamo loptu
    prozor.blit(lopta, (lopta_x0, lopta_y0))

    # crtamo mrezicu
    prozor.blit(mrezica, (kos_x0, kos_y0))

    # ako je lopta pala na zemlju
    if y < 0:
        # prikazujemo logo petlje i logo pygame
        prozor.blit(petlja, (sirina / 2 - petlja.get_width() / 2,
                             visina / 2 - petlja.get_height()))
        prozor.blit(pygame, (sirina / 2 - pygame.get_width() / 2,
                             visina / 2))

def novi_frejm():
    global t, x, y  # menjaćemo ove globalne promenljive
    t += dt         # uvećavamo vreme
    if x < x0 + d:    # ako lopta nije udarila u tablu
        x = x0 + v0x * t  # pomeramo je nadesno
    y = y0 + v0y * t - g*t**2 / 2  # pomeramo je nadole
    crtaj()

# -*- acsection: after-main -*-

# pokrećemo animaciju
pygamebg.frame_loop(round(1/dt), novi_frejm)

# -*- acsection: general-init -*-
import math
import pygame as pg
import pygamebg

(sirina, visina) = (300, 300) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Kosi hitac")

# -*- acsection: main -*-

g     = 9.81     # gravitaciona konstanta - 9.81 metara u sekundi po sekundi
t     = 0        # đule se ispucava u trenutku t = 0 sekundi
v0    = 10       # pocetna brzina je 10 m/s
alpha = 45       # ugao je 45 stepeni
(x, y) = (0, 0)  # početni položaj je u koordinatnom početku

v0x  = v0 * math.cos(math.radians(alpha)) # horizontalna brzina
v0y  = v0 * math.sin(math.radians(alpha)) # vertikalna brzina
xmax = v0x * (2 * v0y / g)                # maksimalni domet

dt = 0.01  # vremenski interval između dva susedna frejma

def crtaj():
    prozor.fill(pg.Color("white"))  # bojimo pozadinu u belo
    r = 20                          # poluprecnik đuleta
    # preračunavamo iz koordinata sveta u ekranske koordinate
    # za x=0 želimo da je xe=r, a za x=xmax želimo da je xe=sirina-r
    # skaliranje po obe ose treba da bude jednako
    k = (sirina - 2 * r) / xmax
    xe = round(k * x + r)
    ye = round(visina - r - k * y)
    pg.draw.circle(prozor, pg.Color("blue"), (xe, ye), r)  # crtamo đule

def novi_frejm():
    global t, x, y  # menjaćemo ove globalne promenljive
    t += dt         # uvećavamo vreme
    if x < xmax:    # ako đule još nije palo
        (x, y) = (v0x * t, v0y * t - g*t**2 / 2) # novi polozaj đuleta
        if y < 0: # ako je đule propalo u zemlju
            (x, y) = (xmax, 0)  # vraćamo ga na površinu
    crtaj()

# -*- acsection: after-main -*-

pygamebg.frame_loop(round(1/dt), novi_frejm)

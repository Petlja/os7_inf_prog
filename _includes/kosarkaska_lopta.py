# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

(sirina, visina) = (400, 400) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Кошаркашка лопта")

# -*- acsection: main -*-

g  = 9.81  # gravitaciona konstanta - 9.81 metara u sekundi po sekundi
k  = 0.75  # koeficijent elastičnosti
h0 = 2     # početna visina sa koje se baca lopta - 2 metra
v0 = 0     # nema početne brzine
h  = h0    # tekuća visina (položaj lopte)
t = 0      # lopta se baca u trenutku t = 0 sekundi
dt = 0.01  # promena vremena nakon kog se lopta pomera i ponovo crta

def crtaj():
    # boje koje cemo koristiti
    BELA = (255, 255, 255)
    NARANDZASTA = (255, 120, 0)

    prozor.fill(BELA)   # bela pozadina
    r = 40              # poluprečnik lopte
    # lopta se nalazi horizontalno na sredini prozora, a
    # visina se odredjuje tako da za h=2 vazi y=r, a za h=0 vazi y=visina-r
    (x, y) = (sirina / 2, (2 * r - visina) / 2 * h + visina - r)
    pg.draw.circle(prozor, NARANDZASTA, (round(x), round(y)), r)  # crtamo loptu

def novi_frejm():
    global t, h, h0, v0
    t += dt                     # ažuriramo proteklo vreme
    h = h0 - (v0*t + g*t*t/2)   # izracunavamo novu visinu lopte
    if h <= 0:                  # ako je lopta dodirnula zemlju
        v0 = -k*(v0 + g*t)      # izračunavamo novi vektor brzine
        if v0 > -0.2: v0 = 0    #    ako je brzina premala, zaustavljamo odbijanje
        h0 = h = 0              #    započinjemo novi hitac
        t = 0                   #    vreme kreće iz početka
    crtaj()
    
# -*- acsection: after-main -*-

pygamebg.frame_loop(round(1/dt), novi_frejm)


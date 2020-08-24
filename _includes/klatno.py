# -*- acsection: general-init -*-
import math
import pygame as pg
import pygamebg

(sirina, visina) = (400, 400) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Клатно")

# -*- acsection: main -*-

# mesto gde je klatno zakaceno
(cx, cy) = (sirina / 2, 0)
# gravitaciona konstanta u (m/s^2)
g = 9.81
# duzina klatna (u m)
l = 0.2
# pocetno vreme (u s)
t = 0
# promena vremena (u s)
dt = 0.01

# početni ugao otklona klatna (ujedno i maksimalni)
theta_max = math.radians(15)
# trenutni ugao kada se izračunava po stvarnim formulama
klatno_theta = theta_max
# trenutni ugao kada se izračunava po uproscenim formulama
klatno_uprosceno_theta = theta_max
# trenutni ugao kada se izračunava po eksplicitnim formulama
klatno_eksplicitno_theta = theta_max

# pocetna brzina
v0 = 0
# trenutna brzina kada se izračunava po stvarnim formulama
klatno_v_theta = v0
# trenutna brzina kada se izračunava po uproscenim formulama
klatno_uprosceno_v_theta = v0

# crtanje klatna u datoj boji, na datom uglu
def nacrtaj_klatno(theta, boja):
    # broj piksela po metru (faktor zumiranja)
    ppm = 1000
    # poluprečnik loptica u pikselima
    r = 15
    # polozaj tačke izračunavamo na osnovu ugla
    x = cx + ppm*l*math.sin(theta)
    y = cy + ppm*l*math.cos(theta)
    # crtamo crno klatno
    pg.draw.line(prozor, boja, (cx, cy), (x, y), 1)
    pg.draw.circle(prozor, boja, (round(x), round(y)), r)

def crtaj():
    # bojimo pozadinu prozora u belo
    prozor.fill(pg.Color("white"))
    
    nacrtaj_klatno(klatno_theta, pg.Color("black"))
    nacrtaj_klatno(klatno_uprosceno_theta, pg.Color("red"))
    nacrtaj_klatno(klatno_eksplicitno_theta, pg.Color("green"))

def novi_frejm():
    global t
    global klatno_a_theta, klatno_v_theta, klatno_theta
    global klatno_uprosceno_a_theta, klatno_uprosceno_v_theta, klatno_uprosceno_theta
    global klatno_eksplicitno_theta
    
    # vreme se menja na osnovu datog priraštaja
    t += dt
        
    # klatno izračunato na osnovu stvarnih formula
       
    # ugaono ubrzanje - stvarna formula
    klatno_a_theta = -(g/l) * math.sin(klatno_theta)
    # ugaona brzina se menja na osnovu ugaonog ubrzanja
    klatno_v_theta += klatno_a_theta * dt
    # ugao se menja na osnovu ugaone brzine
    klatno_theta += klatno_v_theta * dt
    
    # klatno izračunato na osnovu uprošćenih formula
    
    # ugaono ubrzanje - uprošćena formula (sin(theta) je približno theta)
    klatno_uprosceno_a_theta = -(g/l) * klatno_uprosceno_theta
    # ugaona brzina se menja na osnovu ugaonog ubrzanja
    klatno_uprosceno_v_theta += klatno_uprosceno_a_theta * dt
    # ugao se menja na osnovu ugaone brzine
    klatno_uprosceno_theta += klatno_uprosceno_v_theta * dt
        
    # klatno na osnovu eksplicitne jednace kretanja koja se dobija
    # uprošćavanjem formula
       
    # ugao izračunat na osnovu eksplicitne formule
    klatno_eksplicitno_theta = theta_max * math.cos(math.sqrt(g/l)*t)

    crtaj()

# -*- acsection: after-main -*-

pygamebg.frame_loop(round(1/dt), novi_frejm)


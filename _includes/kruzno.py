# -*- acsection: general-init -*-
import pygame as pg, math

pg.init() # uključivanje rada biblioteke PyGame

pg.display.set_caption("Kruzno kretanje")  # otvaramo prozor
(sirina, visina) = (400, 400)
prozor = pg.display.set_mode((sirina, visina))
(cx, cy) = (sirina / 2, visina / 2)    # centar prozora

# -*- acsection: main -*-

R = 100             # poluprečnik putanje
omega = math.pi     # ugaona brzina - polukrug po sekundi
vt = R * omega      # intenzitet tangencijalne brzine
t = 0               # početno vreme
dt = 0.01           # promena vremena
(x, y)     = (R, 0) # početni položaj loptice čija se putanja računa tačnom formulom
(xO, yO)   = (R, 0) # početni polozaj loptice čija se putanja računa Ojlerovom metodom
(xRK, yRK) = (R, 0) # početni polozaj loptice čija se putanja računa metodom Runge-Kuta

def crtaj():
    prozor.fill(pg.Color("white"))                                           # bojimo pozadinu prozora u belo
    pg.draw.circle(prozor, pg.Color("black"), (round(cx), round(cy)), R, 1)  # crtamo putanju po kojoj očekujemo da ce se loptice kretati
    r = 10  # poluprečnik loptice
    pg.draw.circle(prozor, pg.Color("blue"),  (round(cx + x),   round(cy - y)),   r)  # crtamo tačan položaj loptice 
    pg.draw.circle(prozor, pg.Color("red"),   (round(cx + xO),  round(cy - yO)),  r)  # crtamo Ojlerovu lopticu
    pg.draw.circle(prozor, pg.Color("green"), (round(cx + xRK), round(cy - yRK)), r)  # crtamo lopticu Runge-Kuta

def novi_frejm():
    global t, x, y, xO, yO, xRK, yRK

    t += dt   # uvećavamo vreme
    
    # izracunavamo položaj na kome bi teorijski loptica trebalo da se nađe
    (x, y) = (R*math.cos(omega * t), R*math.sin(omega * t))

    # Ojlerovom metodom određujemo novi položaj loptice
    (vx, vy) = (-yO * omega, xO * omega)
    (xO, yO) = (xO + vx * dt, yO + vy * dt)

    # metodom Runge-Kutta drugog reda određujemo novi položaj loptice
    (vx, vy) = (-yRK * omega, xRK * omega)
    (k1x, k1y) = (vx * dt / 2, vy * dt / 2)
    (v1x, v1y) = (-(yRK + k1y) * omega, (xRK + k1x) * omega)
    (k2x, k2y) = (v1x * dt, v1y * dt)
    (xRK, yRK) = (xRK + k2x, yRK + k2y)

    # metodom Runge-Kutta četvrtog reda određujemo novi položaj loptice
#    (vx, vy) = (-yRK * omega, xRK * omega)
#    (k1x, k1y) = (vx * dt, vy * dt)
#    (v1x, v1y) = (-(yRK + k1y/2) * omega, (xRK + k1x/2) * omega)
#    (k2x, k2y) = (v1x * dt, v1y * dt)
#    (v2x, v2y) = (-(yRK + k2y/2) * omega, (xRK + k2x/2) * omega)
#    (k3x, k3y) = (v2x * dt, v2y * dt)
#    (v3x, v3y) = (-(yRK + k3y) * omega, (xRK + k3x) * omega)
#    (k4x, k4y) = (v3x * dt, v3y * dt)
#    (xRK, yRK) = (xRK + 1/6*(k1x + 2*k2x + 2*k3x + k4x), yRK + 1/6*(k1y + 2*k2y + 2*k3y + k4y))

# -*- acsection: after-main -*-

# program radi sve dok ne nastupi dogadjaj pg.QUIT
kraj = False
sat = pg.time.Clock()
while not kraj:
    crtaj()
    # osvezavamo prikaz sadrzaja prozora
    pg.display.update()

    # proveravamo da li je korisnik iskljucio prozor
    for dogadjaj in pg.event.get():
        if dogadjaj.type == pg.QUIT:
            kraj = True

    # cekamo pre prelaska na sledeci korak
    sat.tick(round(1 / dt))
    novi_frejm()

pg.quit()  # isključivanje rada biblioteke PyGame

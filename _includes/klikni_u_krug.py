# -*- acsection: general-init -*-
import pygame as pg, random

pg.init()  # uključivanje rada biblioteke PyGame
pg.display.set_caption("Klikni u krug")   # otvaramo prozor
(sirina, visina) = (200, 300)
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-

# funkcija proverava da li je tačka (x, y) unutar kruga
# koji ima centar u (cx, cy) i poluprečnik r
def u_krugu(x, y, cx, cy, r):
    return (x - cx)**2 + (y - cy)**2 <= r**2

(cx, cy) = (sirina // 2, visina // 2)  # koordinate centra kruga
r = min(sirina // 2, visina // 2)      # poluprečnik kruga
ukljuceno = False                      # da li je uključeno bojenje kruga

def crtanje():
    # određujemo boje
    if ukljuceno:
        boja_pozadine = pg.Color("white")
        boja_kruga = pg.Color("green")
    else:
        boja_pozadine = pg.Color("green")
        boja_kruga = pg.Color("white")
    prozor.fill(boja_pozadine)                       # bojimo pozadinu
    pg.draw.circle(prozor, boja_kruga, (cx, cy), r)  # crtamo krug

def obradi_dogadjaj(dogadjaj):
    global x, y, ukljuceno
    if dogadjaj.type == pg.MOUSEBUTTONDOWN:    # pritisnuto je dugme miša
        (x, y) = dogadjaj.pos                  # koordinate tačke na koju je kliknuto
        if u_krugu(x, y, cx, cy, r):
            ukljuceno = not ukljuceno
        return True  # treba ponovo crtati
    return False # ne treba ponovo crtati

# -*- acsection: after-main -*-

treba_crtati = True
kraj = False
while not(kraj):
    if treba_crtati:
        crtanje()
        pg.display.update()         # ažuriramo prikaz sadrzaja ekrana
        treba_crtati = False
    dogadjaj = pg.event.wait()      # čekamo na događaj
    if dogadjaj.type == pg.QUIT:    # isključivanje prozora
        kraj = True
    else:                           # ostali događaji
        treba_crtati = obradi_dogadjaj(dogadjaj)

pg.quit()  # isključivanje rada biblioteke PyGame

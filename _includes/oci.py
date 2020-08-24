# -*- acsection: general-init -*-
import math
import pygame as pg

pg.init()  # započinje rad biblioteke PyGame
pg.display.set_caption("Очи")  # otvaramo prozor
(sirina, visina) = (400, 400)
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-

(mis_x, mis_y) = pg.mouse.get_pos() # pozicija miša

# crta oko čiji je centar u (cx, cy), poluprečnik r, a zenica mu je
# postavljena tako da gleda ka pozicji misa (mx, my)
def nacrtaj_oko(cx, cy, r, mx, my):
    pg.draw.circle(prozor, pg.Color("black"), (cx, cy), r, 1)            # crtamo oko
    D = math.sqrt((mx-cx)**2 + (my-cy)**2)                               # izračunavamo koordinate zenice
    d = r // 2                                                           # poluprečnik zenice
    zx = cx + d/D*(mx-cx) if D != 0 else cx                              # centar zenice
    zy = cy + d/D*(my-cy) if D != 0 else cy
    pg.draw.circle(prozor, pg.Color("black"), (round(zx), round(zy)), d) # crtamo zenicu

def crtanje():
    # crta oči koje gledaju ka poziciji miša
    prozor.fill(pg.Color("white"))                      # bojimo pozadinu prozora u belo
    (centar_x, centar_y) = (sirina // 2, visina // 2)   # centar prozora
    r = sirina // 8                                     # poluprečnik oka
    levo_x = centar_x - r - r//2                        # x koordinata centra levog oka
    desno_x = centar_x + r + r//2                       # x koordinata centra desno oka
    y = centar_y                                        # y koordinata centara oba oka
    # crtamo oba oka primenom pomocne funkcije
    nacrtaj_oko(levo_x, y, r, mis_x, mis_y)
    nacrtaj_oko(desno_x, y, r, mis_x, mis_y)

def obradi_dogadjaj(dogadjaj):
    global mis_x, mis_y
    if dogadjaj.type == pg.MOUSEMOTION:  # pomeranje miša
        (mis_x, mis_y) = dogadjaj.pos    # pamtimo poziciju miša
        return True                      # ponovo iscrtavamo oči
    return False                         # nema potrebe za ponovnim iscrtavanjem

# -*- acsection: after-main -*-

treba_crtati = True
kraj = False
while not kraj:
    if treba_crtati:
        crtanje()                      # crtamo i osvežavamo prikaz prozora
        pg.display.update()
        treba_crtati = False
    dogadjaj = pg.event.wait()
    if dogadjaj.type == pg.QUIT:       # događaj isključivanja prozora
        kraj = True
    else:
        treba_crtati = obradi_dogadjaj(dogadjaj)

pg.quit()  # završava rad biblioteke PyGame


# -*- acsection: general-init -*-
import math
import pygame as pg

pg.init()                           # ukljucivanje rada biblioteke PyGame
pg.display.set_caption("Rotirajuci pravougaonik")  # otvaramo prozor
(sirina, visina) = (300, 300)
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-
ugao = 0.0
(sirina_kartice, visina_kartice) = (160, 200)

# ucitava sliku i skalira je tako da se uklopi u pravougaonik
# dimenzije zeljena_sirina x zeljena_visina, zadrzavajuci originalne
# proporcije
def ucitaj_i_skaliraj(naziv, zeljena_sirina, zeljena_visina):
    slika = pg.image.load(naziv)
    faktor_skaliranja = min(slika.get_width() / zeljena_sirina, slika.get_height() / zeljena_visina)
    slika = pg.transform.scale(slika, (round(faktor_skaliranja * slika.get_width()), round(faktor_skaliranja * slika.get_height())))
    return slika

slika = ucitaj_i_skaliraj("krtica10.png", sirina_kartice, visina_kartice)

def crtaj():
    if math.pi / 2 < ugao % (2 * math.pi) < 3 * math.pi / 2:
        boja = pg.Color("blue")
        treba_slika = False
    else:
        boja = pg.Color("red")
        treba_slika = True
    
    (s, v) = (sirina_kartice, visina_kartice)
    ss = abs(s/2 * math.cos(ugao))
    (cx, cy) = (sirina / 2, visina / 2)
    prozor.fill(pg.Color("white"))
    pg.draw.rect(prozor, boja, (cx - ss, cy - v/2, 2*ss, v))
    pg.draw.rect(prozor, pg.Color("black"), (cx - ss, cy - v/2, 2*ss, v), 3)

    if treba_slika:
        (s, v) = (slika.get_width(), slika.get_height())
        ss = abs(s / 2 * math.cos(ugao))    
        prozor.blit(pg.transform.scale(slika, (2*round(ss), v)), (cx - ss, cy - v/2))

def novi_frejm():
    global ugao
    ugao += math.radians(5)
    

# -*- acsection: after-main -*-
sat = pg.time.Clock()
kraj = False
while not kraj:
    crtaj()
    pg.display.update()

    for dogadjaj in pg.event.get():     # obrađujemo sve događaje nastale u međuvremenu
        if dogadjaj.type == pg.QUIT:    # proveravamo da li je iskljucen prozor
            kraj = True

    sat.tick(20)  # crtamo 10 frejmova u sekundi
    novi_frejm()

pg.quit() # iskljucivanje rada biblioteke PyGame

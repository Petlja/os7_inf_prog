# -*- acsection: general-init -*-
import random
import pygame as pg

pg.init()  # uključivanje rada biblioteke PyGame
pg.display.set_caption("Двобој")   # otvaramo prozor
(sirina, visina) = (300, 300)
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-

misic_slika = pg.image.load("misic.png")

a = 1  # snaga igrača A
b = 1  # snaga igrača B
pobednik = "" # pobednik dvoboja

def crtanje():
    prozor.fill(pg.Color("white"))

    # prikazujemo snagu igrača A
    for i in range(a):
        prozor.blit(misic_slika, (0, visina - (i + 1) * misic_slika.get_height()))
    
    # prikazujemo snagu igrača B
    for i in range(b):
        prozor.blit(misic_slika, (sirina - misic_slika.get_width(), visina - (i + 1) * misic_slika.get_height()))

    # prikazujemo pobednika dvoboja u centru ekrana
    font = pg.font.SysFont("Arial", 100)
    tekst = font.render(pobednik, True, pg.Color("black"))
    (sirina_teksta, visina_teksta) = (tekst.get_width(), tekst.get_height())
    (x, y) = ((sirina - sirina_teksta) / 2, (visina - visina_teksta) / 2)
    prozor.blit(tekst, (x, y))
        

# nasumično određujemo pobednika u zavisnosti od snage
def dvoboj():
    if random.randint(1, a + b) <= a:
        return "A"
    else:
        return "B"
        
def obradi_dogadjaj(dogadjaj):
    global a, b, pobednik
    if dogadjaj.type == pg.MOUSEBUTTONDOWN:   # pritisnut je taster miša
        (x, y) = dogadjaj.pos
        if x <= misic_slika.get_width():
            if dogadjaj.button == 1 and a < 10:
                a += 1
                return True
            if dogadjaj.button == 3 and a > 1:
                a -= 1
                return True
        elif x >= sirina - misic_slika.get_width():
            if dogadjaj.button == 1 and b < 10:
                b += 1
                return True
            if dogadjaj.button == 3 and b > 1:
                b -= 1
                return True
        else:
            pobednik = dvoboj()
            return True
    return False # ne treba ponovo crtati

# -*- acsection: after-main -*-
treba_crtati = True
kraj = False
while not(kraj):
    if treba_crtati:
        crtanje()
        pg.display.update()  # ažuriramo prikaz sadržaja ekrana
        treba_crtati = False # ne treba crtati do daljnjeg

    dogadjaj = pg.event.wait()      # čekamo naredni dogadjaj
    if dogadjaj.type == pg.QUIT:    # isključivanje prozora
        kraj = True
    else:
        treba_crtati = obradi_dogadjaj(dogadjaj)

pg.quit()  # isključivanje rada biblioteke PyGame

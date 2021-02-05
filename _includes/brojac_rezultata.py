# -*- acsection: general-init -*-
import random
import pygame as pg

pg.init()  # uključivanje rada biblioteke PyGame
pg.display.set_caption("Rezultat")   # otvaramo prozor
(sirina, visina) = (200, 200)
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-

a = 0  # broj poena igrača A
b = 0  # broj poena igrača B

def tekst_levo(x, y, tekst, velicina):
    font = pg.font.SysFont("Arial", velicina)
    tekst = font.render(tekst, True, pg.Color("black"))
    prozor.blit(tekst, (x, y))

def tekst_desno(x, y, tekst, velicina):
    font = pg.font.SysFont("Arial", velicina)
    tekst = font.render(tekst, True, pg.Color("black"))
    (sirina_teksta, visina_teksta) = (tekst.get_width(), tekst.get_height())
    prozor.blit(tekst, (x - sirina_teksta, y))

def tekst_centar(x, y, tekst, velicina):
    font = pg.font.SysFont("Arial", velicina)
    tekst = font.render(tekst, True, pg.Color("black"))
    (sirina_teksta, visina_teksta) = (tekst.get_width(), tekst.get_height())
    (x, y) = (x - sirina_teksta / 2, y - visina_teksta / 2)
    prozor.blit(tekst, (x, y))

def crtanje():
    prozor.fill(pg.Color("white"))

    # prikazujemo rezultat igrača A u levom uglu ekrana
    tekst_levo(0, 0, "A: " + str(a), 30)
    # prikazujemo rezultat igrača B u desnom uglu ekrana
    tekst_desno(sirina, 0, "B: " + str(b), 30)
    # određujemo ko je pobednik
    if a > b:
        poruka = "A"
    elif b > a:
        poruka = "B"
    else:
        poruka = "-"
    tekst_centar(sirina / 2, visina / 2, poruka, 100)

def obradi_dogadjaj(dogadjaj):
    global a, b
    if dogadjaj.type == pg.KEYDOWN:   # pritisnut je neki taster
        if dogadjaj.key == pg.K_a:    # ako je to taster A
            a += 1                    # uvećavamo broj poena igrača A
            return True               # ponovo iscrtavamo ekran
        if dogadjaj.key == pg.K_b:    # ako je to taster B
            b += 1                    # uvećavamo broj poena igrača B
            return True               # ponovo iscrtavamo ekran
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

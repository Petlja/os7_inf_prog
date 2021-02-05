# -*- acsection: general-init -*-
import pygame as pg, random

pg.init()   # uključujemo rad biblioteke PyGame

pg.display.set_caption("Prevlacenje pahulje misem") # otvaramo prozor
(sirina, visina) = (400, 400)
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-

pahulja_slika = pg.image.load("pahulja.png")  # slika pahulje
pahulja = (sirina // 2, visina // 2)          # pozicija centra slike pahulje
prevlacenje = False                           # da li je u toku prevlačenje pahulje

# provera da li tačka (x, y) pripada pravougaoniku čije je gornje levo teme (x0, y0), širina je s i visina je v
def tacka_u_pravougaoniku(x, y, x0, y0, s, v):
    return x0 <= x and x <= x0 + s and y0 <= y and y <= y0 + v

def mis_na_pahulji(mis):
    slika_sirina = pahulja_slika.get_width()                  # dimenzije slike
    slika_visina = pahulja_slika.get_height()
    (xp, yp) = pahulja                                        # koordinate sredine pahulje
    (x0, y0) = (xp - slika_sirina / 2, yp - slika_visina / 2) # koordinate gornjeg levog temena pahulje
    (x, y) = mis                                              # koordinate misa
    return tacka_u_pravougaoniku(x, y, x0, y0, slika_sirina, slika_visina)

def crtanje():
    # bojimo prozor u belo
    prozor.fill(pg.Color("white"))
    # crtamo pahulju
    slika_sirina = pahulja_slika.get_width()
    slika_visina = pahulja_slika.get_height()
    (x, y) = pahulja
    centar = (x - slika_sirina // 2, y - slika_visina // 2)
    prozor.blit(pahulja_slika, centar)

def obradi_dogadjaj(dogadjaj):
    global pahulja, prevlacenje
    if dogadjaj.type == pg.MOUSEBUTTONDOWN:   # pritisnuto je dugme miša
        if mis_na_pahulji(dogadjaj.pos):      #   ako se miš nalazi negde iznad slike pahulje
            prevlacenje = True                #      započinjemo prevlačenje
    elif dogadjaj.type == pg.MOUSEBUTTONUP:   # otpušteno je dugme miša
        prevlacenje = False                   #   završavamo prevlačenje
    elif dogadjaj.type == pg.MOUSEMOTION:     # miš je pomeren
        if prevlacenje:                       #   ako je u toku prevlačenje
            pahulja = dogadjaj.pos            #      postavljamo centar pahulje na mesto miša
            return True                       #      ponovo iscrtavamo scenu
    return False                              # nema potrebe za ponovnim iscrtavanjem

# -*- acsection: after-main -*-
treba_crtati = True
kraj = False
while not kraj:
    if treba_crtati:    # ako je potrebno nacrtati lopticu
        crtanje()
        pg.display.update()        # ažuriramo prikaz sadržaja prozora
        treba_crtati = False

    dogadjaj = pg.event.wait()     # čekamo naredni događaj
    if dogadjaj.type == pg.QUIT:   # isključivanje prozora
        kraj = True
    else:
        treba_crtati = obradi_dogadjaj(dogadjaj)

pg.quit()  # isključujemo rad biblioteke PyGame

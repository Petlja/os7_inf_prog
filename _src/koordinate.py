# -*- acsection: general-init -*-
import pygame as pg

# uključivanje rada biblioteke PyGame
pg.init()

# postavljamo naslov prozora
pg.display.set_caption("Pygame")
# određujemo dimenzije prozora
(sirina, visina) = (300, 300)
# prikazujemo prozor tih dimenzija
prozor = pg.display.set_mode((sirina, visina))

def tekst(s, x, y):
    # font kojim će biti prikazan tekst
    font = pg.font.SysFont("Arial", 25)
    tekst = font.render(s, True, pg.Color("red"))
    # određujemo veličinu tog teksta (da bismo mogli da ga centriramo)
    (sirina_teksta, visina_teksta) = (tekst.get_width(), tekst.get_height())
    # položaj određujemo tako da tekst bude centriran
    (x, y) = (x - sirina_teksta * (x / sirina), y - visina_teksta * (y / visina))
    # prikazujemo sličicu na odgovarajućem mestu na ekranu
    prozor.blit(tekst, (x, y))
# -*- acsection: main -*-

# -*- acsection: after-main -*-
# petlja obrade događaja - čekamo dok korisnik ne isključi prozor
while True:
    dogadjaj = pg.event.wait()

    if dogadjaj.type == pg.QUIT:
        break
    elif dogadjaj.type == pg.MOUSEMOTION:
        # bojimo pozadinu prozora u belo
        prozor.fill(pg.Color("white"))
        (x, y) = dogadjaj.pos
        pg.draw.line(prozor, pg.Color("black"), (x, 0), (x, visina))
        pg.draw.line(prozor, pg.Color("black"), (0, y), (sirina, y))
        s = "(" + str(x) + ", " + str(y) + ")"
        tekst(s, x, y)
        s = "x: " + str(x) + " " + "y: " + str(y)+ " Pronadji tacke (0, 0), (150, 150), (150, 10), (280, 10), (10, 150), (280, 150)"
        pg.display.set_caption(s)
        # osvežavamo sadržaj prozora i tako prikazujemo ono što smo nacrtali
        pg.display.update()

# isključivanje rada biblioteke PyGame
pg.quit()

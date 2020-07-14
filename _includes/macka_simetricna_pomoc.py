# -*- acsection: general-init -*-
import pygame as pg, random
import pygamebg

(sirina, visina) = (300, 300) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Мачка")

# -*- acsection: main -*-

def crtanje():
    prozor.blit(platno, (0, 0))  # crtanje onoga sto je zadato
    
    # ose
    pg.draw.line(prozor, pg.Color("black"), (mis_x, 0), (mis_x, visina), 1) # uspravna linija misa
    pg.draw.line(prozor, pg.Color("black"), (0, mis_y), (sirina, mis_y), 1) # vodoravna linija misa

    # ispis koordinata
    str_x, str_y = str(mis_x), str(mis_y)
    xt_y, yt_y = (5, mis_y - 25) if 2 * mis_y > visina else (visina - 25, mis_y + 5)
    xt_x, yt_x = (mis_x - 50, 5) if 2 * mis_x > sirina else (mis_x + 5, sirina - 50)
    sl_x = font.render(str_x, True, pg.Color("black"))
    sl_y = font.render(str_y, True, pg.Color("black"))
    if mis_x <= sirina // 2:
        prozor.blit(sl_x, (xt_x, xt_y))
    prozor.blit(sl_y, (yt_x, yt_y))

def obradi_dogadjaj(dogadjaj):
    global mis_x, mis_y
    if dogadjaj.type == pg.MOUSEMOTION:   # miš je pomeren
        mis_x, mis_y = dogadjaj.pos
        return True                         # ponovo iscrtavamo scenu
    return False                            # nema potrebe da iscrtavamo scenu

################# crtez
platno = pg.Surface((sirina, visina)) # platno na kome je slika nacrtana
platno.fill(pg.Color("white")) # bojimo pozadinu ekrana u belo

pg.draw.circle(platno, pg.Color("gray"), (150, 160), 100) # glava
pg.draw.polygon(platno, pg.Color("gray"), [(50, 30), (70, 100), (110, 100)]) # levo uvo
pg.draw.polygon(platno, pg.Color("gray"), [(250, 30), (230, 100), (190, 100)]) # desno uvo
pg.draw.ellipse(platno, pg.Color("yellow"), ( 90, 110, 40, 60)) # levo oko
pg.draw.ellipse(platno, pg.Color("yellow"), (170, 110, 40, 60)) # desno oko
pg.draw.ellipse(platno, pg.Color("green"),  (105, 135, 20, 30)) # leva zenica
pg.draw.ellipse(platno, pg.Color("green"),  (175, 135, 20, 30)) # desna zenica
pg.draw.ellipse(platno, pg.Color("darkgray"),  (80, 180, 70, 30)) # levi deo njuske
pg.draw.ellipse(platno, pg.Color("darkgray"),  (150, 180, 70, 30)) # desni deo njuske
pg.draw.circle(platno, pg.Color("black"), (150, 190), 10) # vrh njuske
pg.draw.line(platno, pg.Color("black"), (90, 190), (20, 160), 2) # levi gornji brk
pg.draw.line(platno, pg.Color("black"), (90, 195), (20, 195), 2) # levi srednji brk
pg.draw.line(platno, pg.Color("black"), (90, 200), (20, 220), 2) # levi donji brk
pg.draw.line(platno, pg.Color("black"), (210, 190), (280, 160), 2) # desni gornji brk
pg.draw.line(platno, pg.Color("black"), (210, 195), (280, 195), 2) # desni srednji brk
pg.draw.line(platno, pg.Color("black"), (210, 200), (280, 220), 2) # desni donji brk
#################

font = pg.font.SysFont("Arial", 20)         # font kojim će biti prikazan tekst
font.set_bold(True)
mis_x, mis_y = 0, 0

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

# Zavrsetak skrivenog progrma, koji radi kao primer
pg.time.set_timer(pg.QUIT,50)
pg.time.wait(70)
pg.time.set_timer(pg.QUIT,0)

# Zavrsetak korisnickog programa je posebnoj sekciji

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()

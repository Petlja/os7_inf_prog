# -*- acsection: general-init -*-
import pygame as pg

pg.init()  # inicijalizujemo biblioteku pygame

pg.display.set_caption("Шетање")  # otvaramo prozor
(sirina, visina) = (400, 400)
prozor = pg.display.set_mode((sirina, visina))
sredina_y = visina / 2

# -*- acsection: main -*-
# učitavamo u listu slike setanje1.png, setanje2.png, ..., setanje5.png
slike = []   # niz u koji dodajemo slike
for i in range(5):
    naziv_slike = "setanje" + str(i + 1) + ".png"  # gradimo naziv slike od delova
    slike.append(pg.image.load(naziv_slike))   # učitavamo sliku i dodajemo je na kraj niza

x,y = 100, 100  # polozaj slike

def crtaj():
    t = pg.time.get_ticks()
    prozor.fill(pg.Color("white"))     # bojimo pozadinu prozora u belo
    prozor.blit(slike[(t // 250) % 5], (x, y))  # prikazujemo sliku

def novi_frejm():
    global x, y
    pritisnuto = pg.key.get_pressed()
    if pritisnuto[pg.K_LEFT]:
        x -= 1
    if pritisnuto[pg.K_RIGHT]:
        x += 1
    if pritisnuto[pg.K_DOWN]:
        y += 1
    if pritisnuto[pg.K_UP]:
        y -= 1

# -*- acsection: after-main -*-
kraj = False
sat = pg.time.Clock()  # sat koji određuje broj frejmova u sekundi
while not kraj:
    # crtamo i ažuriramo sadržaj prozora
    crtaj()
    pg.display.update()

    # proveravamo da li je korisnik isključio prozor
    for dogadjaj in pg.event.get():
        if dogadjaj.type == pg.QUIT:
            kraj = True

    # pauziramo do sledeceg frejma
    sat.tick(30)
    novi_frejm()

pg.quit() # isključujemo rad biblioteke PyGame

# -*- acsection: general-init -*-
import pygame as pg

pg.init()  # inicijalizujemo biblioteku PyGame
pg.display.set_caption('Пингвин пада')  # otvaramo prozor
(sirina, visina) = (400, 300)
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-

(stena_x, stena_y) = (0, visina / 2)                     # gornji levi ugao stene (kvadratnog oblika)
(stena_sirina, stena_visina) = (sirina / 2, visina / 2)  # dimenzije stene

pingvin_slika = pg.image.load('pingvin.png')             # učitavamo sliku pingvina
(pingvin_x, pingvin_y) = (0, stena_y)                    # donji levi ugao slike pingvina
                                                         # pingvin je na levom kraju prozora i stoji na steni

def crtaj():
    prozor.fill(pg.Color("white"))                                    # bojimo pozadinu u belo
    pg.draw.rect(prozor, pg.Color("brown"),
                (stena_x, stena_y, stena_sirina, stena_visina))       # crtamo stenu
    prozor.blit(pingvin_slika,
                (pingvin_x, pingvin_y - pingvin_slika.get_height()))  # prikazujemo sliku pingvina

def novi_frejm():
    global pingvin_x, pingvin_y
    pingvin_x += 1                                               # pomeramo pingvina nadesno
    stena_desno = stena_x + stena_sirina                         # x koordinata desne ivice stene
    if pingvin_x > stena_desno and pingvin_y < visina:           # ako je pingvin prešao desnu ivicu stene i nije pao na dno
        pingvin_y += 5                                           #    spuštamo ga

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
    sat.tick(50)
    novi_frejm()

pg.quit() # isključujemo rad biblioteke PyGame

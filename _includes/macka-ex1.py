# -*- acsection: general-init -*-
import pygame as pg

pg.init()  # inicijalizujemo biblioteku PyGame
pg.display.set_caption('Macka')  # otvaramo prozor
(sirina, visina) = (400, 300)
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-

macka_slika = pg.image.load('macka.png')        # učitavamo sliku mačke
(macka_x, macka_y) = (0, 0)                     # koordinate gornje leve ivice slike mačke
macka_v = 2                                     # brzina kretanja mačke (pomeraj u pikselima)
macka_smer = 0                                  # smer kretanja mačke (0 - desno, 1 - dole, 2 - levo, 3 - gore)
macka_pomeraj = [(macka_v, 0), (0, macka_v),    # promena koordinata za svaki smer kretanja
                 (-macka_v, 0), (0, -macka_v)]

def crtaj():
    prozor.fill(pg.Color("white"))                 # bojimo pozadinu u belo
    prozor.blit(macka_slika, (macka_x, macka_y))   # prikazujemo sliku mačke na njenim koordinatama


def novi_frejm():
    global macka_x, macka_y, macka_smer  # promenljive koje se mogu promeniti
    
    # pomeramo mačku u smeru njenog kretanja
    (dx, dy) = macka_pomeraj[macka_smer]
    macka_x += dx
    macka_y += dy

    # ako je ispala van prozora, menjamo joj smer
    if not (0 <= macka_x and macka_x + macka_slika.get_width() <= sirina) or \
       not (0 <= macka_y and macka_y + macka_slika.get_height() <= visina):
        macka_x -= dx
        macka_y -= dy
        macka_smer = (macka_smer + 1) % len(macka_pomeraj)

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

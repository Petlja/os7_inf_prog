# -*- acsection: general-init -*-
import pygame as pg

pg.init()  # inicijalizujemo biblioteku PyGame
pg.display.set_caption('Macka')  # otvaramo prozor
(sirina, visina) = (400, 300)
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-

macka_slika = pg.image.load('macka.png')  # učitavamo sliku mačke
(macka_x, macka_y) = (0, 0)               # koordinate gornje leve ivice slike mačke
macka_v = 2                               # brzina kretanja mačke (pomeraj u pikselima)
macka_smer = 'desno'                      # smer kretanja mačke

def crtaj():
    prozor.fill(pg.Color("white"))                 # bojimo pozadinu u belo
    prozor.blit(macka_slika, (macka_x, macka_y))   # prikazujemo sliku mačke na njenim koordinatama

def novi_frejm():
    global macka_x, macka_y, macka_smer  # promenljive koje se mogu promeniti
    # pomeramo mačku u smeru njenog kretanja
    # ako ispadne van prozora, menjamo joj smer kretanja

    if macka_smer == 'desno':
        macka_x += macka_v
        if macka_x + macka_slika.get_width() >= sirina:  # ako je desni slike desno od desne ivice ekrana
            macka_smer = 'dole'
    elif macka_smer == 'dole':
        macka_y += macka_v
        if macka_y + macka_slika.get_height() >= visina: # ako je donji kraj slike ispod dna ekrana
            macka_smer = 'levo'
    elif macka_smer == 'levo':
        macka_x -= macka_v
        if macka_x <= 0:                                 # ako je levi kraj slike levo od leve ivice ekrana
            macka_smer = 'gore'
    elif macka_smer == 'gore':
        macka_y -= macka_v
        if macka_y <= 0:                                 # ako je donji kraj slike iznad vrha ekrana
            macka_smer = 'desno'

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

# -*- acsection: general-init -*-
import pygame as pg

pg.init()  # inicijalizujemo biblioteku PyGame
pg.display.set_caption('Pingvin silazi niz stepenice')  # otvaramo prozor
(sirina, visina) = (600, 600)
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-

broj_stepenica = 5                           # ukupan broj stepenica
sirina_stepenice = sirina // broj_stepenica  # širina jedne stepenice
visina_stepenice = sirina_stepenice // 2     # visina jedne stepenice

# pravougaonik kojim se crta i-ta stepenica (x, y, sirina, visina)
def stepenica(i):
    stepenica_sirina = sirina_stepenice
    stepenica_visina = (broj_stepenica - i) * visina_stepenice
    stepenica_x = i * sirina_stepenice
    stepenica_y = visina - stepenica_visina
    return (stepenica_x, stepenica_y, stepenica_sirina, stepenica_visina)

pingvin_slika = pg.image.load('pingvin.png')  # slika pingvina
pingvin_x = 0                                 # x koordinata donjeg levog ugla
(_, stepenica_y, _, _) = stepenica(0)         # y koordinata vrha početne stepenice
pingvin_y = stepenica_y                       # y koordinata donjeg levog ugla - inicijalno je pingvin na početnoj stepenici

def crtaj():
    prozor.fill(pg.Color("white"))                         # bojimo pozadinu
    pingvin_y_vrh = pingvin_y - pingvin_slika.get_height() # y koordinata gornjeg levog ugla pingvina
    prozor.blit(pingvin_slika, (pingvin_x, pingvin_y_vrh)) # crtamo pingvina

    for i in range(broj_stepenica):                        # crtamo stepenice
        pg.draw.rect(prozor, pg.Color("black"), stepenica(i))

def novi_frejm():
    global pingvin_x, pingvin_y
    pingvin_x += 1                         # pingvin se pomera na desno
    # ako je potrebno spušta se i na dole
    i = pingvin_x // sirina_stepenice      # redni broj stepenice iznad koje se pingvin trenutno nalazi
    (_, stepenica_y, _, _) = stepenica(i)  # y koordinata vrha te stepenice
    if pingvin_y < stepenica_y:            # ako je pingvin strogo iznad vrha te stepenice
        pingvin_y += 5                     # spušta se naniže

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

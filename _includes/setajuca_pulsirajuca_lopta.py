# -*- acsection: general-init -*-
import pygame as pg

# incicijalizujemo biblioteku PyGame
pg.init()
# postavljamo naslov prozora
pg.display.set_caption("Pulsirajuca loptica koja se moze pomerati")
# otvaramo prozor dimenzije 400x400 piksela
(sirina, visina) = (400, 400)
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-

(x, y) = (200, 200)        # položaj centra loptice
d = 20                     # pomeraj prilikom pomeranja loptice strelicama
(min_r, max_r) = (20, 50)  # minimalni i maksimalni poluprečnik loptice
r = min_r                  # animacija započinje od minimalnog poluprečnika

def crtaj():
    # crtamo lopticu
    prozor.fill(pg.Color("white"))
    pg.draw.circle(prozor, pg.Color("green"), (x, y), r)
    
def obradi_dogadjaj(dogadjaj):
    global x, y, r
    if dogadjaj.type == pg.MOUSEBUTTONDOWN:   # klik mišem
        (x, y) = dogadjaj.pos                 #   pomeramo lopticu na mesto gde je kliknuto mišem
        treba_crtati = True
    elif dogadjaj.type == pg.KEYDOWN:         # pritisak tastera tastature
        if dogadjaj.key == pg.K_LEFT:         #   taster levo
            x = (x - d + sirina) % sirina
        elif dogadjaj.key == pg.K_RIGHT:      #   taster desno
            x = (x + d) % sirina
        elif dogadjaj.key == pg.K_UP:         #   taster gore
            y = (y - d + visina) % visina
        elif dogadjaj.key == pg.K_DOWN:       #   taster dole
            y = (y + d) % visina
        return True                           #   ponovo iscrtavamo scenu

def na_otkucaj_tajmera():    
    global r
    r = (r - min_r + 1) % (max_r - min_r) + min_r  # menjamo poluprečnik loptice
    
# -*- acsection: after-main -*-

kraj= False
treba_crtati = True
pg.time.set_timer(pg.USEREVENT, 20)
while not kraj:
    if treba_crtati:
        crtaj()
        pg.display.update()
        treba_crtati = False

    dogadjaj = pg.event.wait()                    # čekamo na naredni događaj

    if dogadjaj.type == pg.QUIT:                  # isključivanje prozora
        kraj = True
    elif dogadjaj.type == pg.USEREVENT:
        na_otkucaj_tajmera()
        treba_crtati = True
    else:
        treba_crtati = obradi_dogadjaj(dogadjaj)  # ostali dogadjaji

# -*- acsection: after-main -*-
pg.quit()  # isključivanje biblioteke PyGame

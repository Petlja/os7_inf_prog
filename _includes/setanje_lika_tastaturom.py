# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

(sirina, visina) = (400, 400)    # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Setanje lika tastaturom")

# podešavamo događaje tastaturom - prvi događaj se generiše nakon
# 50ms, a svaki naredni nakon 25ms
pg.key.set_repeat(50, 25)

# -*- acsection: main -*-

brod = pg.image.load('spaceship.png')  # učitavamo sliku svemirskog broda
brod_sirina = brod.get_width()         # očitavamo dimenzije slike
brod_visina = brod.get_height()

(x, y) = (sirina / 2, visina / 2)   # koordinate centra prozora
(dx, dy) = (10, 10)                 # pomeraji po x i y koordinati

def crtaj():
    prozor.fill(pg.Color("black"))    # bojimo prozor u belo
    prozor.blit(brod, (x - brod_sirina / 2, y - brod_visina / 2)) # crtamo brod

def obradi_dogadjaj(dogadjaj):
    global x, y
    # pomeraji koji odgovaraju strelicama
    pomeraj = {pg.K_LEFT: (-dx, 0),
               pg.K_RIGHT: (dx, 0),
               pg.K_DOWN: (0, dy),
               pg.K_UP: (0, -dy)}
    if dogadjaj.type == pg.KEYDOWN:      # pritisak tastera na tastaturi
        if dogadjaj.key in pomeraj:
            # pomeramo centar broda za odgovarajući pomeraj
            (DX, DY) = pomeraj[dogadjaj.key]
            x += DX
            y += DY
            # pošto je brod pomeren, ponovo ćemo crtati scenu
            return True
    return False # ne treba ponovo crtati scenu

# -*- acsection: after-main -*-

pygamebg.event_loop(crtaj, obradi_dogadjaj)

# -*- acsection: general-init -*-
import pygame as pg
import pygamebg
(sirina, visina) = (400, 400)
prozor = pygamebg.open_window(sirina, visina, "Slika kao kursor miša")

# -*- acsection: main -*-

mis_slika = (pg.image.load("CekicGore.png"), pg.image.load("CekicDole.png"))
i_slika = 0
(mis_x, mis_y) = (sirina // 2, visina // 2)
pg.mouse.set_pos((mis_x, mis_y))
pg.mouse.set_visible(False)

def crtaj():
    prozor.fill(pg.Color("skyblue")) # bojimo prozor u nebo-plavo
    # crtamo sliku tako da je mis na sredini slike
    slika_sirina = mis_slika[i_slika].get_width()
    slika_visina = mis_slika[i_slika].get_height()
    gore_levo = (mis_x - slika_sirina // 2, mis_y - slika_visina // 2)
    prozor.blit(mis_slika[i_slika], gore_levo)

def obradi_dogadjaj(dogadjaj):
    global mis_x, mis_y, i_slika
    if dogadjaj.type == pg.MOUSEBUTTONDOWN:
        i_slika = 1
        return True
    elif dogadjaj.type == pg.MOUSEBUTTONUP:
        i_slika = 0
        return True
    elif dogadjaj.type == pg.MOUSEMOTION:
        mis_x, mis_y = dogadjaj.pos
        return True
    return False

# -*- acsection: after-main -*-

pygamebg.event_loop(crtaj, obradi_dogadjaj)

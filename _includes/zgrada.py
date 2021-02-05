# -*- acsection: general-init -*-
import math
import pygame as pg
import pygamebg

(sirina, visina) = (200, 400) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Zgarda")

# -*- acsection: main -*-

# bojimo pozadinu prozora u belo
prozor.fill(pg.Color("white"))

# broj spratova
brojSpratova = 4
# broj medjuspratova, racunajuci i prizemlje i potkrovlje
brojMedjuSpratova = brojSpratova + 1
# broj vertikala u zgradi
brojVertikala = 2
# broj medjuvertikala, racunajuci i prvu i poslednju
brojMedjuVertikala = brojVertikala + 1

# visina prozora je jednaka visini medjusprata
visinaProzora = visina / (brojSpratova + brojMedjuSpratova)
# sirina prozora je jednaka sirini medjuvertikale
sirinaProzora = sirina / (brojVertikala + brojMedjuVertikala)

# iscrtavamo konturu zgrade
pg.draw.rect(prozor, pg.Color("blue"), (0, 0, sirina, visina), 10)

# crtamo prozore

# obradjujemo sprat po sprat
for i in range(brojSpratova):
    # za svaki sprat obradjujemo vertikalu, po vertikalu
    for j in range(brojVertikala):
        # crtamo prozor
        prozor_x = sirinaProzora + 2*j*sirinaProzora
        prozor_y = visinaProzora + 2*i*visinaProzora
        pg.draw.rect(prozor, pg.Color("blue"), (prozor_x, prozor_y, sirinaProzora, visinaProzora))

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()

# -*- acsection: general-init -*-
import pygame as pg, pygamebg

(sirina, visina) = (300, 300)    # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Центрирани правоугаоник и елипса")

# -*- acsection: main -*-

prozor.fill(pg.Color("white"))
pg.draw.rect(prozor, pg.Color("yellow"), (150-50, 150-40, 100, 80))
pg.draw.ellipse(prozor, pg.Color("blue"), (150-50, 150-40, 100, 80))
    
# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()

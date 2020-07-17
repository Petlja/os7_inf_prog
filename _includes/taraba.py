# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

(sirina, visina) = (300, 300) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Тараба")

# -*- acsection: main -*-

prozor.fill(pg.Color("skyblue")) # bojimo pozadinu ekrana u nebo-plavo
pg.draw.rect(prozor, pg.Color("forestgreen"), (0, 200, 300, 100))  # trava

# gornja i donja horizontalna prečaga
pg.draw.line(prozor, pg.Color('brown'), ( 10, 100), (290, 100), 10)
pg.draw.line(prozor, pg.Color('brown'), ( 10, 250), (290, 250), 10)

# crtamo 7 pritki
for x in range(20, 300, 40):
    pg.draw.polygon(prozor, pg.Color('brown'),
                    [(x, 80), (x + 10, 70), (x + 20, 80), (x + 20, 270), (x, 270)])

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()

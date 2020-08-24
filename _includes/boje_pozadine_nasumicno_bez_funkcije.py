# -*- acsection: general-init -*-
import random
import pygame as pg

pg.init()                                # pokrećemo biblioteku PyGame
pg.display.set_caption("Боја позадине")  # postavljamo naslov prozora
(sirina, visina) = (200, 200)            # otvaramo prozor dimenzije 200x200 piksela
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-

kraj = False
sat = pg.time.Clock()  # sat koji određuje broj frejmova u sekundi
while not kraj:
    boja = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) # nasumično određujemo boju pozadine
    prozor.fill(boja)                     # bojimo pozadinu prozora
    pg.display.update()                   # ažuriramo sadržaj prozora
    
    for dogadjaj in pg.event.get():       # proveravamo da li je korisnik isključio prozor
        if dogadjaj.type == pg.QUIT:
            kraj = True
            
    sat.tick(4)                           # pauziramo do sledećeg frejma

# -*- acsection: after-main -*-

pg.quit() # isključujemo rad biblioteke PyGame

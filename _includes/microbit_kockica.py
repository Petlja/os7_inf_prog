# -*- acsection: general-init -*-
import random
import pygame as pg


pg.init()  # inicijalizujemo rad biblioteke PyGame
pg.display.set_caption("Бацање коцкице")  # otvaramo prozor
(sirina, visina) = (300, 300)
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-

broj = random.randint(1, 6)  # broj na kockici

def crtaj_displej_5x5(displej):
    prozor.fill(pg.Color("white"))
    R = sirina // 5   # prečnik
    for i in range(5):
        for j in range(5):
            if displej[i][j] == '1':
                r = R // 2                    # poluprečnik
                (x, y) = (j*R + r, i*R + r)   # centar
                pg.draw.circle(prozor, pg.Color("red"), (x, y), r)
    
def crtaj():
    kockice = [["00000",
                "00000",
                "00100",
                "00000",
                "00000"],
               ["00000",
                "00010",
                "00000",
                "01000",
                "00000"],
               ["00000",
                "01000",
                "00100",
                "00010",
                "00000"],
               ["00000",
                "01010",
                "00000",
                "01010",
                "00000"],
               ["00000",
                "01010",
                "00100",
                "01010",
                "00000"],
               ["00000",
                "01010",
                "01010",
                "01010",
                "00000"]]

    crtaj_displej_5x5(kockice[broj - 1])
    
def obradi_dogadjaj(dogadjaj):
    global broj
    if dogadjaj.type == pg.MOUSEBUTTONDOWN or dogadjaj.type == pg.KEYDOWN:
        broj = random.randint(1, 6)
        return True
    return False
    
# -*- acsection: after-main -*-

kraj = False
treba_crtati = True
while not kraj:
    if treba_crtati:
        crtaj()
        pg.display.update()
        treba_crtati = False

    dogadjaj = pg.event.wait()
    if dogadjaj.type == pg.QUIT:
        kraj = True
    else:
        treba_crtati = obradi_dogadjaj(dogadjaj)

pg.quit() # isključujemo rad biblioteke PyGame

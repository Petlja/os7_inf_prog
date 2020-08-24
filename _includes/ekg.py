# -*- acsection: general-init -*-
import pygame as pg

pg.init()                           # ukljucivanje rada biblioteke PyGame
pg.display.set_caption("ЕКГ срца")  # otvaramo prozor
(sirina, visina) = (400, 150)
prozor = pg.display.set_mode((sirina, visina))

dy = [0, 0, 1, -1, 5, -5, 1, 0, 0, 0]  # vertikalni pomeraji ekg signala
dx = 7                                 # horizontalni pomeraj
broj_duzi = 0                          # broj duzi u izlomljenoj liniji

# -*- acsection: main -*-

def crtaj():
    sredina = visina / 2              # vertikalna sredina prozora
    prozor.fill(pg.Color("black"))    # bojimo pozadinu prozora u crno

    # iscrtavamo liniju od leve ivice prozora, do tekuce horizontalne tacke
    for i in range(broj_duzi):
        # odredjujemo koordinate duzi (i, i+1)
        # vertikalni pomeraji se ponavljaju periodicno, pa koristimo
        # ostatak po modulu duzine liste
        (x1, y1) = (i*dx, sredina - 10 * dy[i % len(dy)])
        (x2, y2) = ((i+1)*dx, sredina - 10 * dy[(i + 1) % len(dy)])
        # boju odredjujemo tako da je poslednja duz obojena svetlo zeleno,
        # a one pre nje tamnije zeleno (sto je indeks manji, duz je tamnija)
        zelena = 255 / (broj_duzi - 1) * i if broj_duzi > 1 else 255
        boja = [0, zelena, 0]
        # crtamo duz
        pg.draw.line(prozor, boja, (x1, y1), (x2, y2), 2)

def novi_frejm():
    global broj_duzi            # menjaćemo globalni broj duži
    broj_duzi += 1              # dodajemo još jednu duž u izlomljenu liniju
    if broj_duzi * dx > sirina: # ako je krajnja desna prešla desnu ivicu prozora
        broj_duzi = 0           # vraćamo se na početak

# -*- acsection: after-main -*-
sat = pg.time.Clock()
kraj = False
while not kraj:
    crtaj()
    pg.display.update()

    for dogadjaj in pg.event.get():     # obrađujemo sve događaje nastale u međuvremenu
        if dogadjaj.type == pg.QUIT:    # proveravamo da li je iskljucen prozor
            kraj = True

    sat.tick(10)  # crtamo 10 frejmova u sekundi
    novi_frejm()

pg.quit() # iskljucivanje rada biblioteke PyGame

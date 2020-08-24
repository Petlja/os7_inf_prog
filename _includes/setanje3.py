# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

(sirina, visina) = (400, 400) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Шетање")

pg.key.set_repeat(10, 10)  # podešavamo dogadjaje tastature

# -*- acsection: main -*-

# učitavamo u listu slike setanje1.png, setanje2.png, ..., setanje5.png
slike = []   # niz u koji dodajemo slike
for i in range(5):
    naziv_slike = "setanje" + str(i + 1) + ".png"  # gradimo naziv slike od delova
    slike.append(pg.image.load(naziv_slike))   # učitavamo sliku i dodajemo je na kraj niza

slika = 0            # redni broj slike koja se prikazuje
(x, y) = (100, 100)  # polozaj slike

def crtaj():
    prozor.fill(pg.Color("white"))              # bojimo pozadinu prozora u belo
    prozor.blit(slike[slika], (x, y))           # prikazujemo trenutnu sliku

def obradi_otkucaj_tajmera():
    global slika
    slika = (slika + 1) % 5                    # prelazimo na narednu sliku
    return True        
    
def obradi_dogadjaj(dogadjaj):
    global x, y, slika
    if dogadjaj.type == pg.USEREVENT:          # otkucao je tajmer
        return obradi_otkucaj_tajmera()
    elif dogadjaj.type == pg.KEYDOWN:          # pritisnut je taster na tastaturi
        if dogadjaj.key == pg.K_LEFT:          #   strelica na levo
            x -= 1
        elif dogadjaj.key == pg.K_RIGHT:       #   strelica na desno
            x += 1
        elif dogadjaj.key == pg.K_DOWN:        #   strelica na dole
            y += 1
        elif dogadjaj.key == pg.K_UP:          #   strelica na gore
            y -= 1
        return True

# -*- acsection: after-main -*-

pg.time.set_timer(pg.USEREVENT, 250)                   # navijamo tajmer da otkucava na svakih 250 milisekundi
pygamebg.event_loop(crtaj, obradi_dogadjaj)

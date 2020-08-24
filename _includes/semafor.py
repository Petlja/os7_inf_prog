# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

(sirina, visina) = (200, 450) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina,  "Семафор")


# -*- acsection: main -*-

# redosled kojim se svetla pale i njihovo trajanje:
#    crveno       3 sekunde
#    crveno-žuto  1 sekunda
#    zeleno       4 sekunde
#    žuto         1 sekunda
svetla = [((True, False, False), 3000),  
          ((True, True, False), 1000),   
          ((False, False, True), 4000),  
          ((False, True, False), 1000)]  

broj_svetla = 0   # redni broj svetla koje se uključuje

def crtaj():
    # crtamo semafor
    prozor.fill(pg.Color("white"))
    razmak = 10                    # razmak između susednih svetala i između svetla i gornje tj. donje ivice prozora
    cx = sirina / 2                # centar svakog svetla je horizontalno na sredini prozora
    r = (visina - 4 * razmak) / 6  # poluprečnik svakog svetla (3 prečnika, dva razmaka između svetala i dva razmaka od ivice daju visinu prozora)
    ((crveno, zuto, zeleno), trajanje) = svetla[broj_svetla]  # čitamo boju i trajanje trenutnog svetla
    if crveno:    # crtamo crveno svetlo (ako je potrebno)
        cy = r + razmak
        pg.draw.circle(prozor, pg.Color("red"), (round(cx), round(cy)), round(r))
    if zuto:     # crtamo žuto svetlo (ako je potrebno)
        cy = 3*r + 2*razmak
        pg.draw.circle(prozor, pg.Color("yellow"), (round(cx), round(cy)), round(r))
    if zeleno:   # crtamo zeleno svetlo (ako je potrebno)
        cy = 5*r + 3*razmak
        pg.draw.circle(prozor, pg.Color("green"), (round(cx), round(cy)), round(r))

def obradi_otkucaj_tajmera():
    global broj_svetla                             # otkucao je tajmer i menja se svetlo
    broj_svetla = (broj_svetla + 1) % len(svetla)  # prelazimo na naredno svetlo
    trajanje = svetla[broj_svetla][1]              # čitamo trajanje narednog svetla
    pg.time.set_timer(pg.USEREVENT, trajanje)      # zakazujemo sledeći otkucaj tajmera
    return True

def obradi_dogadjaj(dogadjaj):
    if dogadjaj.type == pg.USEREVENT:
        return obradi_otkucaj_tajmera()
    return False

# -*- acsection: after-main -*-

# zakazujemo prvi otkucaj tajmera na osnovu trajanja prvog svetla
pg.time.set_timer(pg.USEREVENT, svetla[broj_svetla][1])

pygamebg.event_loop(crtaj, obradi_dogadjaj)

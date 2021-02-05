# -*- acsection: general-init -*-
import pygame as pg, math


pg.init()  # ukljucivanje rada biblioteke PyGame
pg.display.set_caption("Recamanova sekvenca")  # otvaranje prozora
(sirina, visina) = (500, 500)
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-

prozor.fill(pg.Color("white"))  # bojimo pozadinu prozora u belo

xt = 0           # tekući element Recamanove sekvence (kreće od nule)
recaman = [0]    # lista prethodnih elemenata Recamanove sekvence
razlika = 1      # razlika između dva susedna elementa (u svakom koraku ona raste za 1)

def crtaj():
    for i in range(1, len(recaman)):  # obilazimo jedan po jedan element sekvence
         # polukrugovi naizmenično idu na gore, pa na dole
         if i % 2 == 0:
             (odUgao, doUgao) = (0, math.pi)
         else:
             (odUgao, doUgao) = (math.pi, 0)

         zoom = 5                                                         # faktor zumiranja - dužina jedinične duži na brojevnoj pravoj
         r = round(zoom * i / 2)                                          # poluprecnik polukruga (u pikselima)
         sredina = visina // 2                                            # vertikalna sredina prozora
         (x, y) = (zoom * min(recaman[i], recaman[i-1]), sredina - r)     # koordinate gornjeg levog temena kvadrata opisanog oko polukruga
         boja = [24, 188, 156]                                            # rezeda boja kojom cemo crtati linije
         pg.draw.arc(prozor, boja, (x, y, 2*r, 2*r), odUgao, doUgao, 1)   # kružni luk koji spaja tekući i prethodni element
         (cx, cy) = (round(zoom * recaman[i]), round(sredina))            # tekući element označavamo malom crnom tačkom
         pg.draw.circle(prozor, pg.Color("black"), (cx, cy), 2)
     
def novi_frejm():
     global xt, razlika
     
     # ako je (xt - razlika) prirodan broj koji se nije prethodno javljao
     if xt >= razlika and not ((xt - razlika) in recaman):
         xt = xt - razlika           # tekući element postaje xt - razlika
     else:
         xt = xt + razlika           # tekući element postaje xt + razlika

     recaman.append(xt) # dodajemo tekući element u sekvencu
     razlika += 1       # razlika između naredna dva elementa je za 1 veća

# -*- acsection: after-main -*-
kraj = False
sat = pg.time.Clock()  # sat koji određuje broj frejmova u sekundi
while not kraj:
    crtaj()                          # crtamo i ažuriramo sadržaj prozora
    pg.display.update()

    for dogadjaj in pg.event.get():  # proveravamo da li je korisnik isključio prozor
        if dogadjaj.type == pg.QUIT:
            kraj = True

    sat.tick(50)                     # pauziramo do sledeceg frejma
    novi_frejm()

pg.quit() # isključujemo rad biblioteke PyGame

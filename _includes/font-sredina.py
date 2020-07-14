# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

(sirina, visina) = (300, 300) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Zdravo svete!")

# bojimo pozadinu prozora u belo
prozor.fill(pg.Color("white"))

# -*- acsection: main -*-

# font kojim će biti prikazan tekst
font = pg.font.SysFont("Arial", 40)
# poruka koja će se ispisivati
poruka = "Zdravo svete!"
# gradimo sličicu koja predstavlja tu poruku ispisanu crnom bojom
tekst = font.render(poruka, True, pg.Color("black"))
# određujemo veličinu tog teksta (da bismo mogli da ga centriramo)
(sirina_teksta, visina_teksta) = (tekst.get_width(), tekst.get_height())
# položaj određujemo tako da tekst bude centriran
(x, y) = ((sirina - sirina_teksta) / 2, (visina - visina_teksta) / 2)
# prikazujemo sličicu na odgovarajućem mestu na ekranu
prozor.blit(tekst, (x, y))

# -*- acsection: after-main -*-

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()

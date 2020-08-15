Слике и текст - тест
====================

Питање 1.
~~~~~~~~~

.. mchoice:: blit
   :answer_a: prozor.blit
   :feedback_a: Тачно
   :answer_b: pg.draw.image
   :feedback_b: Нетачно    
   :answer_c: pg.image
   :feedback_c: Нетачно
   :answer_d: prozor.image
   :feedback_d: Нетачно    
   :correct: a
    
   Коју функцију користимо да бисмо приказали слику на Пајгејм прозору?

   Изабери тачан одговор:

Питање 2.
~~~~~~~~~

.. fillintheblank:: ispisivanje_teksta
   
   Поређај наредбе тако да добијеш програм који у прозору исписује текст.

   (1)
      prozor.blit(tekst, (0, 0))

   (2)
      font = pg.font.SysFont("Arial", 20)

   (3)
      tekst = font.render("Zdravo svete!", True, pg.Color("black"))

   Одговор: |blank|

   - :^\s*231\s*$: Тачно
     :x: Одговор није тачан.


Питање 3.
~~~~~~~~~

.. mchoice:: sirina_Slike
   :answer_a: get_width()
   :feedback_a: Тачно
   :answer_b: pg.image.size()
   :feedback_b: Нетачно    
   :answer_c: pg.image.load()
   :feedback_c: Нетачно
   :answer_d: prozor.image.size()
   :feedback_d: Нетачно    
   :correct: a
    
   Коју функцију користимо како бисмо добили ширину слике? 

   Изабери тачан одговор:

Питање 4.
~~~~~~~~~

.. mchoice:: centrirana_slika
    :answer_a: (x, y) = (slika.get_width(), slika.get_height())
    :feedback_a: Нетачно    
    :answer_b: (x, y) = (sirina/2, visina/2)
    :feedback_b: Нетачно    
    :answer_c: (x, y) = ((sirina - slika.get_width()) / 2, (visina - slika.get_height()) / 2)
    :feedback_c: Тачно
    :answer_d: (x, y) = (slika.get_width(), slika.get_height())    
    :feedback_d: Нетачно
    :correct: c
    
    Којим од понуђених одговора је потребно допунити следећи код како би се слика у прозору приказала центрирано.

    .. code-block:: python
        
        import pygame as pg
        import pygamebg

        (sirina, visina) = (300, 300) # otvaramo prozor
        prozor = pygamebg.open_window(sirina, visina, "slika_test")
        prozor.fill(pg.Color("white"))
        slika = pg.image.load("slika.png")
        ???
        prozor.blit(slika, (x, y))
        pg.quit()


    Изабери тачан одговор:

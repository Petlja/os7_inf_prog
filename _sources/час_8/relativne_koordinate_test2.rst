Релативне координате - квиз
===========================

Провери своје знање тако што ћеш одгорити на следећа питања. 

Питање 1.
~~~~~~~~~

.. mchoice:: cokolada
    :answer_a: temena = [(x, y+2*h), (x+3*w, y+2*h), (x+3*w, y+5*h), (x+4*w, y+5*h)]
    :feedback_a: Нетачно    
    :answer_b: temena = [(x+2*w, y), (x+2*w, y+2*h), (x+4*w, y+2*h), (x+4*w, y+4*h)]
    :feedback_b: Нетачно    
    :answer_c: temena = [(x+2*w, y), (x+2*w, y+3*h), (x+5*w, y+3*h), (x+5*w, y+4*h)]
    :feedback_c: Тачно
    :answer_d: temena = [(x+3*w, y+h), (x+3*w, y+4*h), (x+6*w, y+4*h), (x+6*w, y+5*h)]
    :feedback_d: Нетачно    
    :correct: c
    
    
    Нека је на следећој слици горње лево теме чоколаде у тачки (x, y) и нека су коцкице чоколаде ширине *w* и висине *h*.

    .. image:: ../../_images/pg_rel_koord_cokolada.png

    Допунити прву наредбу следећег кода, тако да се тим кодом црта жута линија по којој је чоколада сломљена.

      .. code-block:: python

        temena = __________
        pg.draw.line(prozor, pg.Color("yellow"), temena[0], temena[1])
        pg.draw.line(prozor, pg.Color("yellow"), temena[1], temena[2])
        pg.draw.line(prozor, pg.Color("yellow"), temena[2], temena[3])


    Изабери тачан одговор:
 
Питање 2.
~~~~~~~~~

.. mchoice:: slovo_e
    :answer_a: "M"
    :feedback_a: Нетачно    
    :answer_b: "E"
    :feedback_b: Тачно
    :answer_c: "W"
    :feedback_c: Нетачно    
    :answer_d: "Ш"
    :feedback_d: Нетачно    
    :correct: b
    
    Извршавањем следећег кода црта се облик једног слова. Којег?

    .. code-block:: python

        pygame.draw.line(prozor, pygame.Color("black"), (x, y), (x, y+40))
        pygame.draw.line(prozor, pygame.Color("black"), (x, y), (x+20, y))
        pygame.draw.line(prozor, pygame.Color("black"), (x, y+20), (x+20, y+20))
        pygame.draw.line(prozor, pygame.Color("black"), (x, y+40), (x+20, y+40))


    Изабери тачан одговор:


Питање 3.
~~~~~~~~~


.. mchoice:: iks_oks_crvena
    :answer_a: (x+d, y+d), (x+2*d, y+d)
    :feedback_a: Нетачно    
    :answer_b: (x, y+d), (x+3*d, y+d)
    :feedback_b: Нетачно    
    :answer_c: (x+d, y+d), (x+d, y+3*d)
    :feedback_c: Нетачно    
    :answer_d: (x+d, y+3*d), (x+d, y)
    :feedback_d: Тачно
    :correct: d
    
    Нека је на следећој слици горње лево теме решетке у тачки (x, y), а страница малих квадрата нека је дужине *d*.

    .. image:: ../../_images/pg_rel_koord_iksoks_crvena.png

    Које су координате крајева црвене дужи?

    Изабери тачан одговор:

Питање 4.
~~~~~~~~~       

.. fillintheblank:: slova_LTVX
   
    Следеће наредбе цртају парове линија у облику слова "L", "T", "V", "X", али не тим редом.

    Упиши слова у редоследу којим их цртају ове наредбе

    .. code-block:: python

        # прво слово
        pygame.draw.line(prozor, pygame.Color("black"), (x, y), (x+50, y+100))
        pygame.draw.line(prozor, pygame.Color("black"), (x+50, y), (x, y+100))
        x += 100
      
        # друго слово
        pygame.draw.line(prozor, pygame.Color("black"), (x, y), (x+25, y+100))
        pygame.draw.line(prozor, pygame.Color("black"), (x+50, y), (x+25, y+100))
        x += 100
      
        # треће слово
        pygame.draw.line(prozor, pygame.Color("black"), (x, y), (x, y+100))
        pygame.draw.line(prozor, pygame.Color("black"), (x, y+100), (x+50, y+100))
        x += 100
  
        # четврто слово
        pygame.draw.line(prozor, pygame.Color("black"), (x, y), (x+50, y))
        pygame.draw.line(prozor, pygame.Color("black"), (x+25, y), (x+25, y+100))     
    
    Одговор: |blank|

   - :^\s*XVLT\s*$: Тачно
     :x: Одговор није тачан.
 

Питање 5.
~~~~~~~~~

.. mchoice:: slovo_k
    :answer_a: "F"
    :feedback_a: Тачно
    :answer_b: "E"
    :feedback_b: Нетачно
    :answer_c: "W"
    :feedback_c: Нетачно
    :answer_d: "Ш"
    :feedback_d: Нетачно
    :correct: a
    
    Извршавањем следећег кода црта се облик једног слова. Којег?

    .. code-block:: python

      pygame.draw.line(prozor, pygame.Color("black"), (x, y), (x, y+4*a))
      pygame.draw.line(prozor, pygame.Color("black"), (x, y), (x+2*a, y))
      pygame.draw.line(prozor, pygame.Color("black"), (x, y+2*a), (x+2*a, y+2*a))


    Изабери тачан одговор:

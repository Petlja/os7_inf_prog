4.3. Квиз - дужи
================

Провери своје знање о цртању дужи

Питање 1.
~~~~~~~~~

.. mchoice:: duz1
    :answer_a: Дуж ће бити постављена хоризонтално.
    :feedback_a: Нетачно    
    :answer_b: Дуж ће бити постављена вертикално/усправно.
    :feedback_b: Тачно
    :answer_c: Дуж ће бити искошена.
    :feedback_c: Нетачно    
    :correct: b
    
    У ком положају ће бити дуж исцртана наредном командом?

    .. code-block:: python

       pygame.draw.line(prozor, pg.Color("black"), (200, 200), (200, 300), 1)

    Изабери тачан одговор:

Питање 2.
~~~~~~~~~

.. mchoice:: dve_duzi
    :answer_a: Фигура у облику слова Г
    :feedback_a: Нетачно    
    :answer_b: Фигура у облику слова L
    :feedback_b: Нетачно    
    :answer_c: Фигура у облику слова Т
    :feedback_c: Тачно
    :answer_d: Фигура у облику знака +
    :feedback_d: Нетачно    
    :correct: c
    

    Шта се исцртава помоћу следеће две наредбе?

    .. code-block:: python

       pygame.draw.line(prozor, pygame.Color("black"), (400, 350), (500, 350), 3)
       pygame.draw.line(prozor, pygame.Color("black"), (450, 350), (450, 450), 3)



    Изабери тачан одговор:

Питање 3.
~~~~~~~~~



.. mchoice:: polovina
    :answer_a: Наредба 1
    :feedback_a: Нетачно    
    :answer_b: Наредба 2
    :feedback_b: Нетачно    
    :answer_c: Наредба 3
    :feedback_c: Нетачно    
    :answer_d: Наредба 4
    :feedback_d: Тачно
    :correct: d
    
    Нека је прозор димензија 300 x 300. Којом командом ће се исцртати вертикална линија (дебљине 1 пиксел) 
    која се налази на средини прозора и спаја горњу и доњу ивицу прозора?

    

    .. code::
  
       1) pygame.draw.line(prozor, pygame.Color("black"), (0, 150), (0, 150), 1)
       2) pygame.draw.line(prozor, pygame.Color("black"), (0, 150), (300, 150), 1)
       3) pygame.draw.line(prozor, pygame.Color("black"), (0, 0), (150, 300), 1)
       4) pygame.draw.line(prozor, pygame.Color("black"), (150, 0), (150, 300), 1)

    Изабери тачан одговор:

Питање 4.
~~~~~~~~~


.. mchoice:: duz_duzina_pravac
    :answer_a: Усправну дуж дужине 500
    :feedback_a: Нетачно    
    :answer_b: Усправну дуж дужине 50
    :feedback_b: Нетачно    
    :answer_c: Водоравну дуж дужине 500
    :feedback_c: Нетачно    
    :answer_d: Водоравну дуж дужине 50
    :feedback_d: Тачно
    :correct: d
    

    Какву дуж исцртава следећа наредба?

    .. code-block:: python

       pygame.draw.line(prozor, pygame.Color("black"), (370, 500), (420, 500), 3)


    Изабери тачан одговор:


Питање 5.
~~~~~~~~~

.. mchoice:: draw1
    :answer_a: Дебљину линије изражену у пикселима.
    :feedback_a: Тачно
    :answer_b: Дебљину линије изражену у милиметрима.
    :feedback_b: Нетачно    
    :answer_c: Дужину линије изражену у центриметрима.
    :feedback_c: Нетачно    
    :correct: a
    
    Шта представља последњи аргумент у следећем позиву функције draw (у овом случају број ``4``)?


    .. code-block:: python

       pygame.draw.line(prozor, pg.Color("black"), (100, 350), (100, 450), 4)

    Изабери тачан одговор:

Питање 6.
~~~~~~~~~

.. mchoice:: dijag
    :answer_a: Наредба 1
    :feedback_a: Нетачно    
    :answer_b: Наредба 2
    :feedback_b: Нетачно    
    :answer_c: Наредба 3
    :feedback_c: Тачно
    :correct: c
    
    Која од наредних наредби исцртава дијагоналу прозора димензије 150 x 150?

    .. code::

       1) pygame.draw.line(prozor, pygame.Color("black"), (0, 0), (0, 150), 1)
       2) pygame.draw.line(prozor, pygame.Color("black"), (150, 0), (150, 150), 1)
       3) pygame.draw.line(prozor, pygame.Color("black"), (0, 150), (150, 0), 1)

    Изабери тачан одговор:

Питање 7.
~~~~~~~~~


.. mchoice:: duz_druga_dijagonala
    :answer_a: слика 1
    :feedback_a: Нетачно    
    :answer_b: слика 2
    :feedback_b: Нетачно    
    :answer_c: слика 3
    :feedback_c: Тачно
    :answer_d: ни једна од наведених слика
    :feedback_d: Нетачно    
    :correct: c
    
    Следеће наредбе цртају једну црвену и једну црну дуж:

    .. code-block:: python

       pygame.draw.line(prozor, pygame.Color("red"), (a, b), (c, d), 3)
       pygame.draw.line(prozor, pygame.Color("black"), (a, d), (c, b), 3)

    .. image:: ../../_images/pg_linije_dve_duzi_a.png

    Која од ових слика може да се добије извршавањем горе наведених наредби?


    Изабери тачан одговор:


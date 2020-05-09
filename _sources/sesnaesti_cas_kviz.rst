Завршни квиз
============


Питање 1.
~~~~~~~~~

.. mchoice:: duz_16
    :answer_a: Дуж ће бити постављена хоризонтално.
    :feedback_a: Нетачно    
    :answer_b: Дуж ће бити постављена вертикално/усправно.
    :feedback_b: Нетачно
    :answer_c: Дуж ће бити искошена.
    :feedback_c: Тачно    
    :correct: c
    
    У ком положају ће бити дуж исцртана наредном командом?

    .. code-block:: python

       pygame.draw.line(prozor, pg.Color("black"), (100, 200), (200, 300), 1)

    Изабери тачан одговор:

Питање 2.
~~~~~~~~~

.. mchoice:: krugkruznica_16
    :answer_a: Круг попуњен бојом
    :feedback_a: Нетачно    
    :answer_b: Кружница - линија
    :feedback_b:  Тачно  
    :answer_c: Елипса (која није круг) попуњена бојом
    :feedback_c: Нетачно    
    :answer_d: Елипса - линија (која није кружница)
    :feedback_d: Нетачно 
    :correct: b
    
    Шта се исцртава следећом наредбом?

    .. code-block:: python
  
      pygame.draw.circle(prozor, pygame.Color("blue"), (120, 80), 40, 1)

    Изабери тачан одговор:

Питање 3.
~~~~~~~~~

.. mchoice:: ntougao_16
   :answer_a: троугао
   :feedback_a: Нетачно
   :answer_b: четвороугао
   :feedback_b: Нетачно    
   :answer_c: петоугао
   :feedback_c: Нетачно    
   :answer_d: ништа од наведеног
   :feedback_d: Тачно
   :correct: d
    
   Шта се исцртава помоћу следећих наредби?

   .. code-block:: python
  
      temena = [(40, 80), (80, 80), (80, 40), (60, 20), (40, 40), (100, 40), (30, 40)]
      pygame.draw.polygon(prozor, pygame.Color("gray"), temena)
    
   Изабери тачан одговор:

Питање 4.
~~~~~~~~~

.. mchoice:: pravougaonik_centrirano_16
   :multiple_answers:
   :answer_a: pg.draw.rect(prozor, boja, (100, 100, 100, 50))
   :feedback_a: Нетачно    
   :answer_b: pg.draw.rect(prozor, boja, (45, 80, 150, 80))
   :feedback_b: Тачно
   :answer_c: pg.draw.rect(prozor, boja, (120, 120, 100, 50))
   :feedback_c: Нетачно    
   :answer_d: pg.draw.rect(prozor, boja, (280, 280, 100, 50))
   :feedback_d: Нетачно    
   :correct: b
    
   Коју наредбу можеш употребити како би нацртао правоугаоник ширине 150 и висине 80 коме је центар у тачки (120, 120)?


   Изабери тачан одговор:

Питање 5.
~~~~~~~~~

.. mchoice:: pomeranje_duzi_16
    :answer_a: pygame.draw.line(prozor, pygame.Color("black"), (x+100, y1+50), (x, y2))
    :feedback_a: Нетачно    
    :answer_b: pygame.draw.line(prozor, pygame.Color("black"), (x+100, y1+100), (x+50, y2+50))
    :feedback_b: Нетачно    
    :answer_c: pygame.draw.line(prozor, pygame.Color("black"), (x, y1+100), (x, y2+100))
    :feedback_c: Нетачно    
    :answer_d: pygame.draw.line(prozor, pygame.Color("black"), (x+150, y1+50), (x+150, y2+50))
    :feedback_d: Тачно
    :answer_e: pygame.draw.line(prozor, pygame.Color("black"), (x, y1), (x+100, y2+50))
    :feedback_e: Нетачно    
    :correct: d
    
    Једна усправна дуж је нацртана наредбом

    .. code-block:: python

        pygame.draw.line(prozor, pygame.Color("black"), (x, y1), (x, y2))

    Којом наредбом ћемо нацртати исту такву дуж, померену 150 пиксела удесно и 50 пиксела на доле?

    Изабери тачан одговор:

Питање 6.
~~~~~~~~~

.. mchoice:: for_stepenice_16
    :answer_a: усправна испрекидана линија
    :feedback_a: Нетачно    
    :answer_b: водоравна испрекидана линија
    :feedback_b: Tачно    
    :answer_c: степенаста линија
    :feedback_c: Нетачно
    :correct: b
    
    Шта се исцртава следећим кодом?

    .. code-block:: python

        x, y = 100, 100
        for i in range(10):
            pygame.draw.line(prozor, pygame.Color("black"), (x, y), (x+10, y), 1)
            x = x+20

    Изабери тачан одговор:

Питање 7.
~~~~~~~~~

.. mchoice:: krstici2_16
    :answer_a: усправна испрекидана линија
    :feedback_a: Нетачно    
    :answer_b: водоравна испрекидана линија
    :feedback_b: Нетaчно   
    :answer_c: степенаста линија
    :feedback_c: Нетачно
    :answer_d: дијагонално поређани крстићи
    :feedback_d: Tачно
    :correct: d
    
    Шта се исцртава следећим кодом?

    .. code-block:: python

        x, y = 100, 100
        for i in range(10):
            pg.draw.line(prozor, pg.Color("black"), (x, y), (x+10, y), 1)
            pg.draw.line(prozor, pg.Color("black"), (x+5, y-5), (x+5, y+10), 1)
            x, y = x+20, y+20 

    Изабери тачан одговор:

Питање 8.
~~~~~~~~~

.. mchoice:: pg_brzina_kretanja2_16
    :answer_a: 5 милиметар лево
    :feedback_a: Нетачно    
    :answer_b: 5 центиметар десно
    :feedback_b: Нетачно    
    :answer_c: 5 пикселa лево
    :feedback_c: Нетачно
    :answer_d: 5 пикселa десно
    :feedback_d: Тачно
    :correct: d

    Ако функција *novi_frejm* изгледа овако:

    .. code-block:: python

        def novi_frejm():
            global x
            x += 5 
            prozor.fill(pg.Color("white"))
            pg.draw.circle(prozor, pg.Color("red"), (x, y), 30)

    Црвени круг се у сваком фрејму помера 

    Изабери тачан одговор:

Питање 9.
~~~~~~~~~

.. mchoice:: pg_krug_kroz_ivice_16
    :answer_a: y - r > visina_prozora
    :feedback_a: Тачно
    :answer_b: y - r < 0
    :feedback_b: Нетачно    
    :answer_c: y  < 0
    :feedback_c: Нетачно    
    :answer_d: y - dy < 0
    :feedback_d: Нетачно    
    :correct: a

    Нека се круг полупречника r са центром у (x, y) помера за по *dy* пиксела на доле. Услов да је цео круг прошао кроз доњу ивицу екрана гласи:
    
    Изабери тачан одговор:

Питање 10.
~~~~~~~~~

.. mchoice:: dkeypojedinacno_16
    :answer_a: 1
    :feedback_a: Тачно
    :answer_b: 2
    :feedback_b: Нетачно    
    :answer_c: 3
    :feedback_c: Нетачно    
    :correct: a

    Којим од понуђених линија кода се врши провера да ли је притиснут тастер слова L?

    1)
        .. code-block:: python

            if (dogadjaj.type == pygame.KEYDOWN) and (dogadjaj.key == pygame.K_l):  

    2)
        .. code-block:: python

            if (dogadjaj.type == pygame.KEYDOWN) or (dogadjaj.key == pygame.K_l):

    3)
        .. code-block:: python

            if (dogadjaj.type == pygame.K_l):

    Изабери тачан одговор:

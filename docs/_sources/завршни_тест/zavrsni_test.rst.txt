16.0. Завршни квиз
==================

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

.. mchoice:: kvadrat_poligon_zk
   :answer_a: Ако је c-a = d-b
   :feedback_a: Тачно
   :answer_b: Дата наредба увек исцртава квадрат
   :feedback_b: Нетачно    
   :answer_c: Ако је a=b и c=d
   :feedback_c: Нетачно    
   :answer_d: Дата наредба ни под којим условима не исцртава квадрат
   :feedback_d: Нетачно    
   :correct: a
    
   Под којим условима би следећа наредба исцртала квадрат?

   .. code-block:: python
  
      pygame.draw.polygon(prozor, pygame.Color("gray"), [(a, b), (a, d), (c, d), (c, b)])

   Изабери тачан одговор:

Питање 9.
~~~~~~~~~

.. mchoice:: elipse_simetrija_zk 
   :answer_a: pg.draw.ellipse(prozor, pg.Color("gray"), (200, 100, 50, 80) )
   :feedback_a: Тачно
   :answer_b:  pg.draw.ellipse(prozor, pg.Color("gray"), (250, 100, 50, 80) )
   :feedback_b: Нетачно    
   :answer_c: pg.draw.ellipse(prozor, pg.Color("gray"), (50, 200, 50, 80) )
   :feedback_c: Нетачно  
   :answer_d: pg.draw.ellipse(prozor, pg.Color("gray"), (100, 180, 50, 80) )
   :feedback_d: Нетачно    
   :correct: a
    
   Дата линија програма исцртава једну елипсу. Ако је прозор је ширине 300 пиксела и висине 300 пиксела, која од понуђених функција ће исцртати елипсу симетричну већ нацртаној у односу на вертикалну осу симетрије прозора?

   .. code-block:: python
  
      pg.draw.ellipse(prozor, pg.Color("gray"), (50, 100, 50, 80) )

   Изабери тачан одговор:

Питање 10.
~~~~~~~~~~

.. mchoice:: blit_zk
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
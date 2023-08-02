11.4. Квиз - цртање облика помоћу петљи
=======================================

Провери своје знање тако што ћеш одговорити на следећа питања: 

Питање 1.
~~~~~~~~~

.. mchoice:: for_isprekidana_0
    :answer_a: 10 пиксела
    :feedback_a: Нетачно    
    :answer_b: 20 пиксела
    :feedback_b: Нетачно    
    :answer_c: 30 пиксела
    :feedback_c: Тачно
    :answer_d: 40 пиксела
    :feedback_d: Нетачно    
    :correct: c
    
    Када се помоћу петље црта испрекидана линија са цртама дужине 20 и размацима дужине 10, почетак следеће
    црте је померен у односу на почетак претходне за (изабери тачан одговор):
 
Питање 2.
~~~~~~~~~

.. mchoice:: for_kose
    :answer_a: слика 1
    :feedback_a: Нетачно    
    :answer_b: слика 2
    :feedback_b: Нетачно    
    :answer_c: слика 3
    :feedback_c: Тачно
    :answer_d: слика 4
    :feedback_d: Нетачно    
    :correct: c
    
    Која од датих слика настаје извршавањем следећег кôда?

    .. code-block:: python

      for a in range(10, 60, 10):
          pygame.draw.line(prozor, pygame.Color("black"), (x+a, y), (x+a-d, y+d))

    .. image:: ../../_images/pg_petlje_kose.png

    Изабери тачан одговор:

Питање 3.
~~~~~~~~~

.. mchoice:: for_stepenice
    :answer_a: усправна испрекидана линија
    :feedback_a: Нетачно    
    :answer_b: водоравна испрекидана линија
    :feedback_b: Нетачно    
    :answer_c: степенаста линија
    :feedback_c: Тачно
    :correct: c
    
    Шта се исцртава следећим кôдом?

    .. code-block:: python

        x, y = 100, 100
        for i in range(10):
            pygame.draw.line(prozor, pygame.Color("black"), (x, y), (x+10, y), 1)
            pygame.draw.line(prozor, pygame.Color("black"), (x+10, y), (x+10, y+10), 1)
            x, y = x+10, y+10



    Изабери тачан одговор:


Питање 4.
~~~~~~~~~

.. mchoice:: for_isprekidana
    :multiple_answers:
    :answer_a: кôд 1
    :feedback_a: Тачно
    :answer_b: кôд 2
    :feedback_b: Тачно
    :answer_c: кôд 3
    :feedback_c: Тачно
    :answer_d: кôд 4
    :feedback_d: Тачно
    :correct: ['a', 'b', 'c', 'd']
    
    Којим од датих кôдова се може нацртати водоравна испрекидана линија од 10 цртица која почиње од тачке (x0, y0), тако да су и цртице и размаци дужине *a*?

    (1)
      .. code-block:: python

          for i in range(10):
              pygame.draw.line(prozor, pygame.Color("black"), (x0+2*i*a, y0), (x0+(2*i+1)*a, y0), 1)

    (2)
      .. code-block:: python

        for t in range(0, 20*a, 2*a):
            pygame.draw.line(prozor, pygame.Color("black"), (x0+t, y0), (x0+t+a, y0), 1)

    (3)
      .. code-block:: python

        x = x0
        for i in range(10):
            pygame.draw.line(prozor, pygame.Color("black"), (x, y0), (x+a, y0), 1)
            x += 2*a

    (4)
      .. code-block:: python

        for t in range(a, 20*a, 2*a):
            pygame.draw.line(prozor, pygame.Color("black"), (x0+t-a, y0), (x0+t, y0), 1)



    Изабери тачан одговор:

 

Питање 5.
~~~~~~~~~

.. mchoice:: for_cikcak
    :answer_a: слика 1
    :feedback_a: Тачно
    :answer_b: слика 2
    :feedback_b: Нетачно    
    :answer_c: слика 3
    :feedback_c: Нетачно    
    :answer_d: слика 4
    :feedback_d: Нетачно    
    :correct: a
    
    Која од понуђених слика настаје извршавањем следећег кôда?

    .. code-block:: python

        dx, dy = 10, 10
        for i in range(n):
            pygame.draw.line(prozor, pygame.Color("black"), (x, y), (x+dx, y+dy), 1)
            x += dx
            y += dy
            dy = -dy

    .. image:: ../../_images/pg_petlje_cikcak.png

    Изабери тачан одговор:



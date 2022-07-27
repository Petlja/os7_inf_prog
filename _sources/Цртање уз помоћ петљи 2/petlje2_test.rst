12.3. Квиз - Понављање облика коришћењем петљи
==============================================

Провери своје знање тако што ћеш одговорити на следећа питања:

Питање 1.
~~~~~~~~~

.. mchoice:: for_rect_1
    :answer_a: слика 1
    :feedback_a: Нетачно    
    :answer_b: слика 2
    :feedback_b: Тачно
    :answer_c: слика 3
    :feedback_c: Нетачно    
    :answer_d: слика 4
    :feedback_d: Нетачно    
    :correct: b
    
    Која од датих слика настаје извршавањем следећег кôда?

    .. code-block:: python

        boje = [pygame.Color("red"), pygame.Color("blue"), pygame.Color("white")]
        for i in range(3):
            pygame.draw.rect(prozor, boje[i], (x + i*30, y + i*40, 60, 40))


    .. image:: ../../_images/pg_petlje_rect01.png

    Изабери тачан одговор:
 
Питање 2.
~~~~~~~~~

.. mchoice:: for_krugovi01
    :answer_a: слика 1
    :feedback_a: Нетачно    
    :answer_b: слика 2
    :feedback_b: Нетачно    
    :answer_c: слика 3
    :feedback_c: Тачно
    :answer_d: слика 4
    :feedback_d: Нетачно    
    :correct: c
    
    Која од понуђених слика настаје извршавањем следећег кôда?

    .. code-block:: python

        boje = [pygame.Color("red"), pygame.Color("blue"), pygame.Color("white")]
        for i in range(3):
            pygame.draw.circle(prozor, boje[i], (x - i*20, y), 20)

    .. image:: ../../_images/pg_petlje_krugovi1.png

    Изабери тачан одговор:


Питање 3.
~~~~~~~~~       

.. mchoice:: for_krugovi03
    :multiple_answers:
    :answer_a: (x+a, y)
    :feedback_a: Нетачно    
    :answer_b: (x+a, y+a)
    :feedback_b: Нетачно    
    :answer_c: (x+2*a, y)
    :feedback_c: Тачно
    :answer_d: (x, y+2*a)
    :feedback_d: Тачно
    :answer_e: (x, y+a)
    :feedback_e: Нетачно    
    :correct: c,d
    
    Следећим кôдом треба да се исцрта пет кругова:

    .. code-block:: python

        for a in range(20, 120, 20):
            pygame.draw.circle(prozor, pygame.Color("black"), (P, Q), 20, 1)

    Ти кругови ће се додиривати ако уместо (P, Q) стоји... (изабери тачан одговор):
 

Питање 4.
~~~~~~~~~


.. mchoice:: for_krugovi02
    :multiple_answers:
    :answer_a: pygame.draw.circle(prozor, pygame.Color("black"), (x, y-r), r, 1)
    :feedback_a: Тачно
    :answer_b: pygame.draw.circle(prozor, pygame.Color("black"), (x-r, y), r, 1)
    :feedback_b: Тачно
    :answer_c: pygame.draw.circle(prozor, pygame.Color("black"), (x, y), r, 1)
    :feedback_c: Нетачно    
    :answer_d: pygame.draw.circle(prozor, pygame.Color("black"), (x+r, y), r, 1)
    :feedback_d: Тачно
    :answer_e: pygame.draw.circle(prozor, pygame.Color("black"), (x, y+r), r, 1)
    :feedback_e: Тачно
    :correct: ['a', 'b', 'd', 'e']

    Које од кружних линија, задатих следећим наредбама, садрже тачку (x, y)?

    Изабери тачан одговор:



Питање 5.
~~~~~~~~~

.. mchoice:: for_krugovi04
    :answer_a: слика 1
    :feedback_a: Нетачно    
    :answer_b: слика 2
    :feedback_b: Тачно
    :answer_c: слика 3
    :feedback_c: Нетачно    
    :answer_d: слика 4
    :feedback_d: Нетачно    
    :correct: b
    
    Која од датих слика настаје извршавањем следећег кôда?

    .. code-block:: python

       for r in range(a, n*a+1, a):
            pygame.draw.circle(prozor, pygame.Color("black"), (x+r, y), r, 1)

    .. image:: ../../_images/pg_petlje_krugovi2.png



    Изабери тачан одговор:

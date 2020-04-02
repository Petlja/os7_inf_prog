Многоуглови, комбиновање облика, слике - квиз
======================================

Провери своје знање тако што ћеш одгорити на следећа питања. 

Питање 1.
~~~~~~~~~

.. mchoice:: ntougao
   :answer_a: троугао
   :feedback_a: Нетачно
   :answer_b: четвороугао
   :feedback_b: Нетачно    
   :answer_c: петоугао
   :feedback_c: Тачно
   :answer_d: ништа од наведеног
   :feedback_d: Нетачно    
   :correct: c
    
   Шта се исртава помоћу следећих наредби?

   .. code-block:: python
  
      temena = [(40, 80), (80, 80), (80, 40), (60, 20), (40, 40)]
      pygame.draw.polygon(prozor, pygame.Color("gray"), temena)
    
   Изабери тачан одговор:
 
Питање 2.
~~~~~~~~~

.. mchoice:: trougao
   :multiple_answers:
   :answer_a: правоугли
   :feedback_a: Тачно
   :answer_b: једнакокраки
   :feedback_b: Тачно
   :answer_c: оштроугли
   :feedback_c: Нетачно    
   :answer_d: једнакостранични
   :feedback_d: Нетачно    
   :correct: ['a', 'b']
    
   Које особине има троугао који се исцртава следећом наредбом?

   .. code-block:: python
  
     pygame.draw.polygon(prozor, pygame.Color("gray"), [(10, 10), (20, 20), (10, 20)])


   Изабери тачан одговор:

Питање 3.
~~~~~~~~~

.. mchoice:: kvadrat_poligon
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

Питање 4.
~~~~~~~~~

.. mchoice:: lista
   :answer_a: pg.draw.polygon(prozor, boja, [(0, 0), (50, 100), (100, 0)])
   :feedback_a: Тачно
   :answer_b: pg.draw.polygon(prozor, boja, (0, 0), (50, 100), (100, 0))
   :feedback_b: Нетачно    
   :answer_c: pg.draw.polygon(prozor, boja, (0, 0, 50, 100, 100, 0))
   :feedback_c: Нетачно  
   :answer_d: pg.draw.polygon(prozor, boja, [0, 0, 50, 100, 100, 0])
   :feedback_d: Нетачно    
   :correct: a
    
   Желимо да нацртамо троугао. У ком облику могу да се задају координате тачака?

   Изабери тачан одговор:
 

Питање 5.
~~~~~~~~~

.. mchoice:: romb
   :multiple_answers:
   :answer_a: pygame.draw.polygon(prozor, pygame.Color("red"),  [(0, 240), (320, 480), (640, 240), (320, 0)])
   :feedback_a: Нетачно    
   :answer_b: pygame.draw.polygon(prozor, pygame.Color("red"),  [(20, 240), (320, 460), (620, 240), (320, 20)])
   :feedback_b: Тачно
   :answer_c: pygame.draw.polygon(prozor, pygame.Color("red"),  [(20, 240), (620, 240), (320, 460), (320, 20)])
   :feedback_c: Нетачно    
   :answer_d: pygame.draw.polygon(prozor, pygame.Color("red"),  [(20, 240), (320, 20), (620, 240), (320, 460)])
   :feedback_d: Тачно
   :correct: ['b', 'd']
    
   У прозор величине 640 x 480 треба уписати ромб дијагонала паралелних осама, тако да су темена ромба удаљена по 20 пиксела од средишта ивица прозора. Којом наредбом се то може учинити?


   Изабери тачан одговор:


Питање 6.
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
   :correct: а
    
   Коју функцију користимо да бисмо приказали слику на Пајгејм прозору?

   Изабери тачан одговор:
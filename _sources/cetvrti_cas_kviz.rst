Симетрично пресликавање координата, центрирани правоугаоници и елипсе - квиз 
============================================================================

Провери своје знање тако што ћеш одгорити на следећа питања. 

Питање 1.
~~~~~~~~~

.. mchoice:: krug_simetrija
   :answer_a: pygame.draw.circle(prozor, pygame.Color("blue"), (30, 50), 30)
   :feedback_a: Нетачно
   :answer_b: pygame.draw.circle(prozor, pygame.Color("blue"), (250, 30), 30)
   :feedback_b: Тачно    
   :answer_c: pygame.draw.circle(prozor, pygame.Color("blue"), (30, 250), 30)
   :feedback_c: Нетачно
   :answer_d: pygame.draw.circle(prozor, pygame.Color("blue"), (30, 150), 30)
   :feedback_d: Нетачно    
   :correct: b
    
   У прозору ширине 300 пиксела, нацртан је круг помоћу следеће функције:  

   .. code-block:: python
  
      pygame.draw.circle(prozor, pygame.Color("blue"), (50, 30), 30)

   Која од понуђених функција црта њему симетричан кург у односу на вертикалну средину прозора? 

   Изабери тачан одговор:
 
Питање 2.
~~~~~~~~~

.. mchoice:: simetrija_tacke
   :multiple_answers:
   :answer_a: (100, 500)
   :feedback_a: Тачно
   :answer_b: (500, 100)
   :feedback_b: Нетачно   
   :answer_c: (500, 500)
   :feedback_c: Нетачно    
   :answer_d: (100, 400)
   :feedback_d: Нетачно    
   :correct: a
    
   Ако је прозор висине 600 пиксела, које су координате тачке која је симетрична тачки (100, 100) у односу на хоризонталну средину прозора?

   Изабери тачан одговор:

Питање 3.
~~~~~~~~~

.. mchoice:: trouglovi
   :answer_a: Два троугла симетрично пресликана по вертикалној средини прозора
   :feedback_a: Нетачно
   :answer_b: Два троугла симетрично пресликана по хоризонталној средини прозора
   :feedback_b: Тачно
   :answer_c: Два несимтрична троулга
   :feedback_c: Нетачно    
   :answer_d: Два симетрично пресликана троугла који се додирују
   :feedback_d: Нетачно    
   :correct: a
    
   Шта ће исцртати следеће две функције у прозору ширине 300 пиксела и висине 300 пиксела? 

   .. code-block:: python
  
      pg.draw.polygon(prozor, pg.Color("gray"), [(50, 100), (150, 100), (100, 50)])
      pg.draw.polygon(prozor, pg.Color("gray"), [(50, 200), (150, 200), (100, 250)])

   Изабери тачан одговор:

Питање 4.
~~~~~~~~~

.. mchoice:: elipse_simetrija
   :answer_a: pg.draw.ellipse(prozor, pg.Color("gray"), (200, 100, 50, 80) )
   :feedback_a: Тачно
   :answer_b:  pg.draw.ellipse(prozor, pg.Color("gray"), (250, 100, 50, 80) )
   :feedback_b: Нетачно    
   :answer_c: pg.draw.ellipse(prozor, pg.Color("gray"), (50, 200, 50, 80) )
   :feedback_c: Нетачно  
   :answer_d: pg.draw.ellipse(prozor, pg.Color("gray"), (100, 180, 50, 80) )
   :feedback_d: Нетачно    
   :correct: a
    
   Ако је прозор ширине 300 пиксела и висине 300 пиксела, која од понуђених функција ће исцртати елипсу симетрично пресликану по вертикалној средини прозора у односу на елипсу коју исцртава следећа функција 

   .. code-block:: python
  
      pg.draw.ellipse(prozor, pg.Color("gray"), (50, 100, 50, 80) )

   Изабери тачан одговор:
 

Питање 5.
~~~~~~~~~

.. mchoice:: pravougaonik_centrirano
   :multiple_answers:
   :answer_a: pg.draw.rect(prozor, boja, (100, 100, 100, 50))
   :feedback_a: Нетачно    
   :answer_b: pg.draw.rect(prozor, boja, (70, 95, 100, 50))
   :feedback_b: Тачно
   :answer_c: pg.draw.rect(prozor, boja, (120, 120, 100, 50))
   :feedback_c: Нетачно    
   :answer_d: pg.draw.rect(prozor, boja, (280, 280, 100, 50))
   :feedback_d: Нетачно    
   :correct: b
    
   Коју наредбу можеш употребити како би нацртао правоугаоник ширине 100 и висине 50 коме је центар у тачки (120, 120)?


   Изабери тачан одговор:


Питање 6.
~~~~~~~~~

.. mchoice:: blit
   :answer_a: pg.draw.rect(prozor, pg.Color("blue"), (100, 50, 100, 40))
   :feedback_a: Нетачно
   :answer_b: pg.draw.rect(prozor, pg.Color("blue"), (150, 100 , 80, 20))
   :feedback_b: Нетачно    
   :answer_c: pg.draw.rect(prozor, pg.Color("blue"), (50, 60 , 80, 20))
   :feedback_c: Нетачно
   :answer_d: pg.draw.rect(prozor, pg.Color("blue"), (160, 110 , 80, 20))
   :feedback_d: Тачно
   :correct: d
    
   Који од следећих правоугаоника је центриран у правоугаоник који исцртава следећа функција? 

      .. code-block:: python
  
      pg.draw.rect(prozor, pg.Color("gray"), (150, 100, 100, 40))

   Изабери тачан одговор:
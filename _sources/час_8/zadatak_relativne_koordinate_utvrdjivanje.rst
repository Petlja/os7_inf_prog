
Прелазак са апсолутних на релативне координате
==============================================

Иако цртеже који се задају у односу на неко сидро обично креирамо
имајући ово у старту у виду, постоји систематичан поступак којим од
цртежа који је задат у апсолутним координатама можемо доћи до цртежа
који је нацртан у односу на неко задато сидро (можемо *усидрити*
цртеж). Покушајмо да резимирамо како можемо да уведемо сидро тј. да од
цртежа у ком се јављају апсолутне координате уведемо релативне
координате.

На пример, ако се црта круг помоћу ``pg.draw.circle(prozor, boja, (cx,
cy), r)``, тада га можемо усидрити у тачку ``(x, y)`` тиме што позив
заменимо са ``pg.draw.circle(prozor, boja, (x + (cx - x), y + (cy -
y)), r)``. На пример, Ако круг нацртан помоћу ``pg.draw.circle(prozor,
boja, (100, 50), r)`` желимо да усидримо у тачку ``(x, y) = (50,
100)``, тада ћемо га цртати помоћу ``pg.draw.circle(prozor, boja, (x +
50, y - 50), r)``. Слично можемо урадити и у случају осталих облика.
   
Провери да ли ово разумеш тако што ћеш одговорити на наредних неколико
питања.
   
.. mchoice:: pygame_quiz_uvodjenje_sidra
   :multiple_answers:
   :answer_a: pg.draw.circle(prozor, pg.Color("red"), (x, y), 50, 1)
   :answer_b: pg.draw.line(prozor, pg.Color("red"), (x-50, x-50), (150, 150))
   :answer_c: pg.draw.line(prozor, pg.Color("red"), (x+50, y-50), (x-50, y+50))
   :answer_d: pg.draw.rect(prozor, pg.Color("red"), (x-50, y-50, x, y))
   :correct: a,c
   :feedback_a: Тачно
   :feedback_b: Покушај поново
   :feedback_c: Тачно
   :feedback_d: Покушај поново
   
   Желимо да прилагодимо цртеж који се састоји од наредних облика,
   тако да се све црта у односу на сидро са координатама `x=100`,
   `y=100`.
                
   .. activecode:: pygame_quiz_uvodjenje_sidra_code
      :passivecode: true
                    
      pg.draw.circle(prozor, pg.Color("red"), (100, 100), 50, 1)
      pg.draw.line(prozor, pg.Color("red"), (50, 50), (150, 150))
      pg.draw.line(prozor, pg.Color("red"), (150, 50), (50, 150))
      pg.draw.rect(prozor, pg.Color("red"), (50, 50, 100, 100))

   Које наредбе ће бити део прилагођеног цртежа?
      
.. mchoice:: pygame_quiz_uvodjenje_sidra_krug
   :answer_a: pg.draw.circle(prozor, pg.Color("red"), (x, y), 60)
   :answer_b: pg.draw.circle(prozor, pg.Color("red"), (180, 240), 60)
   :answer_c: pg.draw.circle(prozor, pg.Color("red"), (100, 100), 60)
   :answer_d: pg.draw.circle(prozor, pg.Color("red"), (x + 80, y - 20), 60)
   :answer_e: pg.draw.circle(prozor, pg.Color("red"), (x + 180 , y + 240), 60)
   :correct: d
   :feedback_a: Покушај поново
   :feedback_b: Покушај поново
   :feedback_c: Покушај поново
   :feedback_d: Тачно
   :feedback_e: Покушај поново

   Круг нацртан наредбом `pg.draw.circle(prozor, boja, (180, 80), 60)`
   део је цртежа који желимо да прилагодимо тако да му основна тачка
   (сидро) буде у одређено променљивама `x = 100` и `y = 100`. Која
   наредба ће бити део тако прилагођеног цртежа?

Покрени сада наредни програм и видећеш лице човечуљка. Прилагоди цртеж
тако да се црта релативно у односу на сидро које се налази у центру
плавог круга (у почетку је то :math:`(100, 100)`).  Покретањем програма
провери да ли ти је решење добро. Ако је све урађено како треба, цртеж
ће се исправно померати док се миш помера.

       
.. activecode:: PyGame_movable
   :nocodelens:
   :enablecopy:
   :modaloutput:
   :playtask:
   :includexsrc: _includes/movable_scalable.py
                 
   def crtanje():
       prozor.fill(pg.Color("white"))
       pg.draw.circle(prozor, pg.Color("blue"), (100, 100), 60)
       pg.draw.circle(prozor, pg.Color("yellow"), (75, 75), 15)
       pg.draw.circle(prozor, pg.Color("black"), (80, 80), 5)
       pg.draw.circle(prozor, pg.Color("yellow"), (125, 75), 15)
       pg.draw.circle(prozor, pg.Color("black"), (120, 80), 5)
       pg.draw.ellipse(prozor, pg.Color("red"), (75, 110, 50, 10))


.. reveal:: PyGame_movable_reveal
   :showtitle: Прикажи решење
   :hidetitle: Сакриј решење

   .. activecode:: PyGame_movable_code
      :passivecode:

      def crtanje():
          prozor.fill(pg.Color("white"))
          pg.draw.circle(prozor, pg.Color("blue"), (x, y), 60)
          pg.draw.circle(prozor, pg.Color("yellow"), (x-25, y-25), 15)
          pg.draw.circle(prozor, pg.Color("black"), (x-20, y-20), 5)
          pg.draw.circle(prozor, pg.Color("yellow"), (x+25, y-25), 15)
          pg.draw.circle(prozor, pg.Color("black"), (x+20, y-20), 5)
          pg.draw.ellipse(prozor, pg.Color("red"), (x-25, y+10, 50, 10))

Размотримо сада како да поред цртања у односу на неки релативан
положај (сидро) направимо наше цртеже скалабилним, тј. да се цртају у
односу на релативно задату димензију.          

.. mchoice:: pygame_quiz_uvodjenje_sidra_i_velicine
   :answer_a: pg.draw.circle(prozor, pg.Color("red"), (x, y), 12*a)
   :answer_b: pg.draw.circle(prozor, pg.Color("red"), (x - 36*a, x - 48*a), 12*a)
   :answer_c: pg.draw.circle(prozor, pg.Color("red"), (x + 16*a, y - 4*a), 12*a)
   :answer_d: pg.draw.circle(prozor, pg.Color("red"), (20*a, 20*a), 60)
   :answer_e: pg.draw.circle(prozor, pg.Color("red"), (x + 16*a , y - 4*a), 60)
   :correct: c
   :feedback_a: Покушај поново
   :feedback_b: Покушај поново
   :feedback_c: Тачно
   :feedback_d: Покушај поново
   :feedback_e: Покушај поново

   Круг нацртан наредбом `pg.draw.circle(prozor, boja, (180, 80), 60)`
   део је цртежа који желимо да прилагодимо тако да му главна тачка
   (сидро) буде у одређено променљивама `x = 100` и `y = 100`, и да му
   основна величина буде `a=5`. Која наредба ће бити део тако
   прилагођеног цртежа?

          
Прилагоди сада додатно програм тако да се све црта релативно и у
односу на јединичну величину (нека у почетку то буде :math:`5`). Ако
је све урађено како треба, величина ће му се мењати кликом на лево
тј. десно дугме миша.

.. activecode:: PyGame_movable_scalable
   :nocodelens:
   :enablecopy:
   :modaloutput:
   :playtask:
   :includexsrc: _includes/movable_scalable.py
                 
   def crtanje():
       prozor.fill(pg.Color("white"))
       pg.draw.circle(prozor, pg.Color("blue"), (100, 100), 60)
       pg.draw.circle(prozor, pg.Color("yellow"), (75, 75), 15)
       pg.draw.circle(prozor, pg.Color("black"), (80, 80), 5)
       pg.draw.circle(prozor, pg.Color("yellow"), (125, 75), 15)
       pg.draw.circle(prozor, pg.Color("black"), (120, 80), 5)
       pg.draw.ellipse(prozor, pg.Color("red"), (75, 110, 50, 10))


.. reveal:: PyGame_movable_scalable_reveal
   :showtitle: Прикажи решење
   :hidetitle: Сакриј решење

   .. activecode:: PyGame_movable_scalable_code
      :passivecode:

      def crtanje():
          prozor.fill(pg.Color("white"))
          pg.draw.circle(prozor, pg.Color("blue"), (x, y), 12*a)
          pg.draw.circle(prozor, pg.Color("yellow"), (x-5*a, y-5*a), 3*a)
          pg.draw.circle(prozor, pg.Color("black"), (x-4*a, y-4*a), a)
          pg.draw.circle(prozor, pg.Color("yellow"), (x+5*a, y-5*a), 3*a)
          pg.draw.circle(prozor, pg.Color("black"), (x+4*a, y-4*a), a)
          pg.draw.ellipse(prozor, pg.Color("red"), (x-5*a, y+2*a, 10*a, 2*a))

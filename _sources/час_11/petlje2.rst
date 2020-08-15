Употреба генератора случајних бројева
=====================================

Функцијом ``random.randint(a, b)`` можемо добити насумично одабран цео
број из интервала :math:`[a, b]`. Ово може бити веома корисно када је
потребно да цртеж испунимо са већим бројем неправилно распоређених
облика. Слично, функцијом ``random.uniform(a, b)`` добијамо насумично
одабрани реалан број из интервала :math:`[a, b]`.

Ноћно небо
''''''''''

.. questionnote::

   Смркнуло се и небо је препуно звездица. Уз звездице се види и млад
   месец. Нацртај такав цртеж.

.. activecode:: nocno_nebo
   :playtask:
   :nocodelens:
   :modaloutput: 
   :enablecopy:
   :includexsrc: _includes/mesec_i_zvezdice.py

   # bojimo pozadinu prozora u crno
   prozor.fill(pg.Color("black"))

   # crtamo 100 nasumično raspoređenih zvezdica
   for i in range(100):
       # nasumično određujemo koordinate
       x = random.randint(0, sirina)
       y = ???
       # crtamo zvezdicu kao mali krug
       ???

   # crtamo mlad mesec pomoću jednog crnog i jednog belog kruga
   pg.draw.circle(prozor, pg.Color("white"), (100, 100),  30)
   pg.draw.circle(prozor, pg.Color("black"), (???, ???),  30)

   
Насумичне боје
''''''''''''''

.. questionnote::

   Украсићемо собу тако што ћемо на плафон окачити 5 балона у
   насумично одабраним бојама. Напиши програм који исцртава овакав
   цртеж, при чему сваки балон црта у облику елипсе.

Генератор случајних бројева можемо употребити и да насумично одаберемо
боју. Довољно је да за сваку од црвене, зелене и плаве компоненте
насумично одаберемо број између 0 и 255. Ово можемо издвојити у
посебну функцију коју ћемо позвати када год нам затреба насумична
боја.

Прикажимо и како да равномерно распоредимо балоне по
плафону. Претпоставимо да треба да распоредимо :math:`n` балона.
Ширину прозора ћемо поделити на :math:`n` једнаких делова. Сваки балон
ћемо закачити на средину њему одговарајућег дела. Ширину једног дела
можемо израчунати тако што ширину прозора поделимо са бројем делова, x
координату левог краја i-тог дела (где бројање креће од 0) добијамо
тако што ширину једног дела помножимо са i, док x координату средине
тог дела (тачке у којој се налази врх балона) добијамо тако што на
леви крај додамо још пола ширине дела. На основу те тачке лако
израчунавамо горњу леву тачку правоугаоника описаног око елипсе (x
координату добијамо тако што од x координате средине поља одузмемо пола
ширине елипсе, док је y координата једнака нули).

.. activecode:: baloni
   :playtask:
   :nocodelens:
   :modaloutput: 
   :enablecopy:
   :includexsrc: _includes/baloni.py

   # funkcija koja na nasumičan način određuje boju
   def nasumicna_boja():
       return (random.randint(0, 255), ???,  random.randint(0, 255))

   # bojimo pozadinu prozora u crno
   prozor.fill(pg.Color("yellow"))

   # crtamo balone
   broj_balona = 5
   sirina_polja = ???
   sirina_balona = 50
   visina_balona = 70
   for i in range(broj_balona):
       centar_polja = i*sirina_polja + sirina_polja / 2
       pg.draw.ellipse(prozor, ???, (???, ???, ???, ???))
       
       
Дијагонално распоређивање облика
--------------------------------

Кругови дуж дијагонале
''''''''''''''''''''''
   
.. questionnote::

   Напиши програм који дуж целе главне дијагонале прозора распоређује
   :math:`n=10` једнаких кругова.

Пречници кругова деле главну дијагоналу на :math:`n` једнаких делова.
Полупречник кругова можемо израчунати тако што дужину дијагонале
поделимо са :math:`2n`, а дужину дијагонале можемо израчунати
Питагорином теоремом као :math:`\sqrt{s^2 + v^2}`, где су :math:`s` и
:math:`v` ширина тј. висина прозора. На основу Талесове теореме
пројекције центара кругова на x осу и на y осу
деле ивице прозора у истом односу у ком центри кругова деле 
дијагоналу. Ако са :math:`k_x` означимо :math:`n`-ти део ширине
прозора, а са :math:`k_y` означимо :math:`n`-ти део висине прозора,
тада прва тачка има координате :math:`(\frac{k_x}{2}, \frac{k_y}{2})`,
друга има координате :math:`(\frac{k_x}{2} + k_x, \frac{k_y}{2} +
k_y)`, трећа има координате :math:`(\frac{k_x}{2} + 2k_x,
\frac{k_y}{2} + 2k_y)` итд. На основу овога допуни наредни програм.
         
.. activecode:: krugovi_na_dijagonali
   :nocodelens:
   :modaloutput: 
   :enablecopy:
   :playtask:
   :includexsrc: _includes/krugovi_na_dijagonali.py

   # broj krugova
   n = 10
   # dužina dijagonale		
   d = round(???)
   # poluprečnik krugova
   r = round(???)
   # razmak između centara krugova po x i y osi
   kx = round(???)
   ky = round(???)
    
   # bojimo pozadinu prozora u belo
   prozor.fill(pg.Color("white"))
   # crtamo krugove
   for i in range(n):
       pg.draw.circle(prozor, pg.Color("red"), (???*kx, ???*ky), r, 3)

Правилно распоређивање боја
===========================

Чињеница да су нијансе боја одређене бројевима између 0 и 255 нам
омогућава и да аутоматски израчунавамо нијансе боја тако да боје буду
распоређене дуж неког дела спектра боја. Прикажимо ову технику кроз неколико
примера.


Квадрати у нијансама црвене боје
''''''''''''''''''''''''''''''''

.. questionnote::
   
   Напиши програм који црта шест квадрата обојених у различите,
   правилно распоређене нијансе црвене боје (све дефинисане помоћу RGB
   система).

Нијансе црвене боје су одређене тиме да садрже само црвену компоненту
боје, док су зелена и плава на нули. Боје иду од чисте црвене (``[255,
0, 0]``), па до црне (``[0, 0, 0]``). Претпоставићемо да је разлика
количине светлости између сваке две суседне нијансе иста. Ако је та
разлика ``r``, тада је црвена компонента у нашим бојама редом
:math:`5r`, :math:`4r`, :math:`3r`, :math:`2r`, :math:`r` и
:math:`0`. Пошто прва боја треба да буде најсветлија могућа, важи да
је :math:`5r = 255`, тј. да је :math:`r = 51`. Дакле, боје су редом
одређене са ``[255, 0, 0]``, ``[204, 0, 0]``, ``[153, 0, 0]``, ``[102,
0, 0]``, ``[51, 0, 0]`` и ``[0, 0, 0]``. Опет претпостављамо да су
димензије квадрта 50 пута 50 пиксела, тако да квадрате редом
распоређујемо дуж прозора димензије 300 пута 50 пиксела.


.. activecode:: sest_nijansi_crvene
   :nocodelens:		
   :modaloutput:
   :enablecopy:
   :playtask:
   :includexsrc: _includes/sest_boja_osvetljenje.py
		 
   # crtamo 6 kvadrata
   pg.draw.rect(prozor, [???, 0, 0], (???, 0, 50, 50))
   pg.draw.rect(prozor, [???, 0, 0], (???, 0, 50, 50))
   pg.draw.rect(prozor, [???, 0, 0], (???, 0, 50, 50))
   pg.draw.rect(prozor, [???, 0, 0], (???, 0, 50, 50))
   pg.draw.rect(prozor, [???, 0, 0], (???, 0, 50, 50))
   pg.draw.rect(prozor, [0,   0, 0], (???, 0, 50, 50))

Наравно, бољи кôд добијамо ако задатак решимо уз помоћ петље.

.. activecode:: sest_nijansi_crvene_petlja
   :nocodelens:		
   :modaloutput:
   :enablecopy:
   :playtask:
   :includexsrc: _includes/sest_boja_osvetljenje.py
		 
   broj_kvadrata = 6
   razmak = 255 / (broj_kvadrata -  1) # razmak između dve susedne nijanse
   ???


Оптичка варка
'''''''''''''

.. questionnote::

   Позадину прозора обоји у нијансе сиве боје које се постепено мењају
   од црне на левој ивици прозора до беле на десној ивици. Након тога
   у средини прозора нацртај правоугаоник сиве боје висине 50 пиксела
   и ширине једанке три четвртине ширине прозора. Видећеш интересантну
   оптичку варку.

Ефекат градијента ћеш постићи тако што ћеш ширином прозора распоредити
256 једнаких правоуганика, сваки обојен у различитну нијансу сиве
боје.
   
.. activecode:: gradijent
   :playtask:
   :nocodelens:
   :modaloutput: 
   :enablecopy:
   :includexsrc: _includes/gradijent.py

   # bojimo pozadinu gradijentom tako što iscrtavamo 256 jednakih pravougaonika
   ???

   # crtamo jednobojni sivi pravougaonik u sredini 
   sx = 0.75 * sirina  # širina pravougaonika je 3/4 širine prozora
   sy = 50             # visina pravougaonika je 50 piksela
   ???

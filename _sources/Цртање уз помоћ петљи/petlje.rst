11.2. Цртање облика помоћу петљи
================================

Мердевине
'''''''''

.. questionnote::

   Измени наредни програм тако да се пречаге мердевина цртају у
   петљи.

Пажљиво проучи које се вредности мењају кроз позиве функције
``pg.draw.line``, шта је почетна вредност, шта је крајња вредност и
који је корак, па на основу тога позови функцију ``range`` у оквиру
петље ``for``.

.. reveal:: мердевине_помоћ
   :showtitle: Помоћ
   :hidetitle: Сакриј помоћ

   .. infonote::
      Можемо приметити да се при цртању пречага заправо мења само висина пречага, а све остало је исто.
      Да би мењали висину пречаге потребно је да код цртања леве и десне њене тачке
      мењамо ``y`` коррдинату (чиме се мења висина) у корацима 50, 100, 150, 200, 250. 
      То можемо искористити у ``range`` делу у оквиру петље ``for``. 
   
.. activecode:: PyGame_loop__ladder
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :playtask:
    :includexsrc: _includes/merdevine.py

    prozor.fill(pg.Color("beige")) # bojimo pozadinu ekrana u bež

    # leva strana
    pg.draw.line(prozor, pg.Color("brown"), (100, 10), (100, visina - 10), 10)
    # desna strana    
    pg.draw.line(prozor, pg.Color("brown"), (200, 10), (200, visina - 10), 10)

    # ovaj deo prepraviti
    pg.draw.line(prozor, pg.Color("brown"), (100,  50), (200, 50), 10)  # prečaga
    pg.draw.line(prozor, pg.Color("brown"), (100, 100), (200, 100), 10) # prečaga
    pg.draw.line(prozor, pg.Color("brown"), (100, 150), (200, 150), 10) # prečaga
    pg.draw.line(prozor, pg.Color("brown"), (100, 200), (200, 200), 10) # prečaga
    pg.draw.line(prozor, pg.Color("brown"), (100, 250), (200, 250), 10) # prečaga
   
.. reveal:: PyGame_loop__ladder_reveal
    :showtitle: Прикажи решење
    :hidetitle: Сакриј решење
    
    Једно могуће решење је:
    
    .. activecode:: PyGame_loop__ladder_solution
        :nocodelens:
        :enablecopy:
        :modaloutput:
        :includesrc: _includes/merdevine.py

Правилно распоређени бројеви
----------------------------

.. infonote::
   У оба претходна примера било је потребно да набројимо неки низ
   правилно распоређених бројева. У задатку са круговима то су били
   бројеви 10, 20, ..., 100, а у задатку са мердевинама то су били
   бројеви 50, 100, 150, 200, 250.

У решењима задатка видели смо да је један од начина да се то уради петља облика:

.. activecode:: petlja1
   :passivecode: true

      for x in range(pocetni_x, najveci_x+1, korak):
            ...

При томе је било потребно обратити пажњу на то да десни крај интервала никада није
укључен у набрајање па зато узимамо ``najveci_x+1`` да би и највећи ``х`` био укључен у петљу.

Провери да ли ово разумеш тако што ћеш одговорити на следеће питање.

.. dragndrop:: pygame_quiz_upari_petlje_i_aritmeticke_nizove
    :feedback: Покушај поново!
    :match_1: 15, 30, 45, 60, 75|||for i in range(15, 75+1, 15)
    :match_2: 100, 350, 600|||for i in range(100, 600+1, 250)
    :match_3: 5, 10, 15, 20, 25, 30|||for i in range(5, 30+1, 5)
    :match_4: 100, 200, 300, 400, 500, 600|||for i in range(100, 600+1, 100)

    Упари низ бројева са петљом која га генерише:
      
Наведимо још неколико начина да се исти ефекат постигне 
.......................................................

Ако сада почетак обележимо са :math:`x_0`, а корак са :math:`d_x`, тада су вредности
које исписујемо :math:`x_0`, :math:`x_0 + d_x`, :math:`x_0+2d_x`,
:math:`x_0+3d_x` итд. Ако желимо да набројимо :math:`n` ових вредности,
тада можемо употребити петљу облика:

.. activecode:: petlja2
   :passivecode: true

   for i in range(n):
       x = x0 + i * dx
       ...

Још један начин је да променљиву `x` ажурирамо кроз сваки корак петље,
тако што је увећавамо за `dx`.

.. infonote::
   **Важна напомена:** Израз `x += dx` једнак је изразу `x = x + dx`

       
.. activecode:: petlja3
   :passivecode: true

   x = x0
   for i in range(n):
       ...
       x += dx

Видећемо да се велики број задатака са цртањем правилно распоређених
облика може решити применом оваквих петљи.

.. infonote::
   Нагласимо још и да функција ``range`` са кораком (са три аргумента)
   прима обавезно целобројне аргументе, па у ситуацијама када корак није
   целобројан њено коришћење није могуће.

       
Хоризонтално и вертикално распоређивање облика
----------------------------------------------

Често у применама имамо потребу да распоредимо објекте тако да буду
један до другога, тако да су сви објекти равномерно распоређени,
тј. тако да су свака два узастопна објекта на истом растојању.


Хоризонтално распоређени кругови
''''''''''''''''''''''''''''''''

.. questionnote::

   Нацртај 10 кругова пречника 30 пиксела тако да буду равномерно
   распоређени ширином прозора и да се међусобно додирују.

Наредних пар питања ће ти помоћи да решиш овај задатак.

.. mchoice:: pygame_quiz_rastojanje_centara_krugova
   :answer_a: 2*r
   :answer_b: r
   :answer_c: r / 2
   :answer_d: 100
   :correct: a
   :feedback_a: Тачно
   :feedback_b: Покушај поново
   :feedback_c: Покушај поново
   :feedback_d: Покушај поново

   Ако се два круга полупречника :math:`r` додирују, тада је растојање
   између њихових центара једнако:

.. fillintheblank:: pygame_quiz_rastojanje_kruga_od_leve_ivice

    Ако круг полупречника :math:`r` додирује леву ивицу прозора, тада
    је x координата његовог центра једнака:

    - :[ ]*r[ ]*: Тачно!
      :.*: Покушај поново.

На основу овога, допуни наредни програм:
           
.. activecode:: krugovi_horizontalno
   :playtask:
   :nocodelens:
   :modaloutput: 
   :enablecopy:
   :includexsrc: _includes/krugovi_horizontalno.py
      
   # bojimo pozadinu prozora u belo
   prozor.fill(pg.Color("white"))   

   # crtamo 10 krugova
   r = 30  # poluprečnik krugova
   x = ???   # x koordinata centra kruga
   for i in range(10):
       # crtamo krug
       pg.draw.circle(prozor, pg.Color("black"), (x, visina // 2), r, 1)
       x += ???  # аžuriramo x tako da postane koordinata centra narednog kruga

Још један начин да се овај задатак реши је тај да се примети да су
координате центара кругова редом :math:`r`, :math:`r + 2r`, :math:`r +4r`, 
:math:`r + 6r` итд. Дакле, :math:`x` координата круга са редним бројем
:math:`i` је :math:`r + 2\cdot i\cdot r` тј. :math:`(2i+1)r`. Реши
задатак коришћењем ове формуле.

.. activecode:: krugovi_horizontalno_funkcija
   :playtask:
   :nocodelens:
   :modaloutput: 
   :enablecopy:
   :includexsrc: _includes/krugovi_horizontalno.py
      
   # bojimo pozadinu prozora u belo
   prozor.fill(pg.Color("white"))   

   # crtamo 10 krugova
   r = 30  # poluprečnik krugova
   for i in range(10):
       # crtamo krug
       pg.draw.circle(prozor, pg.Color("black"), (???, visina // 2), r, 1)

Трећи начин би могао искористити могућност да се функцијом ``range``
може вршити набрајање са кораком (нпр. ``range(r, r + 10*2*r + 1, 2*r)``).       

.. topic:: Погледај видео:

   Употреба петље за правилно распоређивање облика по хоризонтали прозора.

    .. ytpopup:: 3G8HEacrnyQ
        :width: 735
        :height: 415
        :align: center 

Вертикално распоређени кругови
''''''''''''''''''''''''''''''

Прикажимо сада како можемо распоредити кругове вертикално.

.. questionnote::

   Напиши програм који црта кругове полупречника 10 пиксела равномерно
   распоређене вертикално средином прозора, тако да су им центри
   удаљени 30 пиксела (нацртај све кругове који се виде). Висина
   прозора се мења приликом сваког покретања програма.

Овај задатак је сличан претходном, уз неколико важних разлика. То што
су кругови распоређени вертикално уместо хоризонтално не мења много -
само је потребно заменити улогу x и y координата. Растојање између
центара је овај пут фиксно (износи 30 пиксела) и не израчунава се
на основу полупречника. Кључна разлика је то што број кругова није
унапред задат већ је кругове потребно цртати све док се бар неки њихов
делић види у прозору. Зато имамо две могућности. Или ћемо некако на
основу висине прозора израчунати број кругова који се виде или ћемо
уместо бројачке петље ``for`` употребити условну петљу ``while``.
Ово друго може бити једноставније.

.. activecode:: krugovi_vertikalno
   :playtask:
   :nocodelens:
   :modaloutput: 
   :enablecopy:
   :includexsrc: _includes/krugovi_vertikalno.py
      
   # bojimo pozadinu prozora u belo
   prozor.fill(pg.Color("white"))   

   r = 10  # poluprečnik krugova
   dy = 30 # vertikalni razmak između centara dva uzastopna kruga
   y = ???   # y koordinata centra tekućeg kruga
   while ???:
       pg.draw.circle(prozor, pg.Color("red"), (sirina // 2, y), r)  # crtamo krug
       y += ???  # centar narednog kruga je udaljen za dy od centra tekućeg kruga 


       

   

                    

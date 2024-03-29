10.1. Слике и текст
===================

.. infonote::
   Поред цртања облика, Пајгејм омогућава да се у програме укључе и слике, 
   као и да се исписује текст. У овој лекцији научићете да у своје програме укључите слике и 
   прикажете текст у прозору.


Приказ слика
------------

Сада сте научили да цртате помоћу геометријских облика, па можемо да
вам откријемо једну тајну. Ако сте раније користили Scratch, знате
колико је интересантно било када сте ликове у прозору могли да
представљате сличицама (било унапред понуђеним, било преузетим са
интернета). И Пајгејм нуди ту могућност, што често бива
једноставније него да сами цртамо.

Претпоставићемо да имамо слику мачке у датотеци
``macka.png``. 

.. reveal:: слика_ИДЛЕ
   :showtitle: Ако радиш у програму IDLE
   :hidetitle: Сакриј

   .. technicalnote::
      Ако овај програм покрећеш на свом рачунару (на пример,
      из окружења IDLE) потребно је да слику преузмеш и снимиш на исто место
      на коме је снимљена и изворна датотека Python програма (датотека са
      екстензијом ``py``), тј. на место где си сачувао/сачувала фајл у коме пишеш програм.

.. image:: ../../_images/macka.png
   :align: center

Први корак је да се слика учита. То се ради помоћу функције
``pg.image.load`` којој се као параметар наводи назив датотеке са
сликом (то су обично датотеке са екстензијама ``png`` или ``jpg``).


.. learnmorenote:: Конвертовање слике

   После учитавања слике могуће је позвати ``convert()`` да би се слика
   превела из формата у којем је записана у датотеци у формат који је
   погодан за приказивање у прозору.

Други корак је приказ учитане сличице у прозору (једном учитана слика
се може приказивати и на више места). То радимо помоћу функције
``prozor.blit`` којој се као параметри наводе учитана слика и позиција
на коју ће се поставити њено горње лево теме (ако наведемо координате
:math:`(0, 0)`, слика ће бити приказана у горњем левом углу прозора).

.. activecode:: ucitavanje_i_prikaz_slike
   :passivecode: onlymain
   :autorun: 
   :includesrc: _includes/slika.py


.. topic:: Погледај овај видео и пробај да на свом рачунару напишеш програм који укључује слику. 
   Слику коју смо користили у овом видеу можеш преузети 
   са `овог линка <https://petljamediastorage.blob.core.windows.net/root/Media/Default/Kursevi/informatika_VII/raketa.png>`__ 

    .. ytpopup:: EMVPL3zczeg
        :width: 735
        :height: 415
        :align: center 


Приказ текста
-------------

.. infonote::
   Пајгејм омогућава и да се у прозору пише текст. Тексту је могуће
   задавати боју, фонт, величину и положај. Приказ текста захтева три корака.

**Прво**, потребно је одабрати фонт којим ће се текст исписивати. Најлакше је да употребимо 
функцију ``pg.font.SysFont`` 
која прима два параметра: назив фонта (инсталираног у оперативном систему) и његову величину. 

.. learnmorenote:: Датотека са фонтом

   Уместо системског фонта могуће је навести и неку датотеку са фонтом (то су обично ``.ttf`` или ``.otf``
   датотеке) и тада се користи функција ``pg.font.Font``, али то нећемо у наставку користити.

**Други корак** је да се креира сличица, која представља нацртани текст.
То можемо једноставно урадити функцијом ``font.render`` где је ``font``
креиран у претходном кораку, а параметри функције су редом текст који се исписује (ниска), 
логичка вредност која одређује да ли ће се цртати лепшим линијама (*True за ДА*) 
и на крају боја којом ће се текст исписивати.

Процедура је надаље потпуно идентична као и у случају слике. У **трећем кораку** добијену сличицу 
можемо поставити на било коју позицију у
прозору помоћу функције ``prozor.blit``, чији је први параметар сличица, а други координате на које 
ће бити постављен горњи леви угао слике, односно текста.


Размотримо наредни пример који у горњем левом углу прозора исписује поруку „Zdravo svete!“

.. activecode:: pisanje_teksta
   :passivecode: onlymain
   :autorun: 
   :includesrc: _includes/font.py

.. topic:: Из овог видеа можеш сазнати како да укључиш текст у своје програме. 

    .. ytpopup:: OyAm4ftHZg4
        :width: 735
        :height: 415
        :align: center 

Центрирана слика
----------------

Пошто су слике правоугаоног облика, оне се такође могу центрирати
унутар прозора на исти начин као и било који други правоугаоник.

.. questionnote::

   Прилагоди програм који у прозору приказује слику мачке учитану из
   датотеке ``macka.png`` тако да та слика буде центрирана на средини
   прозора.

.. image:: ../../_images/macka.png
   :align: center
   

Да би се слика приказала на средини прозора, очитавамо прво њене
димензије. То можемо урадити помоћу функција ``get_width()`` и
``get_height()``, које враћају ширину и висину слике. Координате се
онда добијају као половина разлике између димензија прозора и димензија
слике која се приказује (сличица је центрирана јер је центар слике у центру прозора).

.. activecode:: ucitavanje_i_prikaz_slike_sredina
   :passivecode: onlymain
   :autorun: 
   :includesrc: _includes/slika-sredina.py

   
Центрирани текст
----------------

.. questionnote::

   Прилагоди програм који у прозор исписује поруку „Zdravo svete!“ тако
   да тај текст буде центриран у средини прозора.

Када од текста направимо сличицу како смо описали, можемо поново
употребити функције ``get_width()`` и ``get_height()`` да бисмо је центрирали као и у случају
слике. Координате левог угла се онда одређују на исти начин као и у случају слике.


.. learnmorenote:: Други начин за одређивање ширине и висине текста

   За одређивање ширине и висине текста можемо употребити и функцију ``font.size()`` чији је
   параметар ниска чија се величина одређује. 

.. activecode:: font_sredina
   :nocodelens:
   :enablecopy:
   :modaloutput:
   :playtask:
   :includexsrc: _includes/font-sredina.py

   # font kojim će biti prikazan tekst
   font = pg.font.SysFont("Arial", 40)
   # poruka koja će se ispisivati
   poruka = "Zdravo svete!"
   # gradimo sličicu koja predstavlja tu poruku ispisanu crnom bojom
   tekst = font.render(poruka, True, pg.Color("black"))
   # određujemo veličinu tog teksta (da bismo mogli da ga centriramo)
   (sirina_teksta, visina_teksta) = (tekst.get_width(), tekst.get_height())
   # položaj određujemo tako da tekst bude centriran
   (x, y) = (???, ???)
   # prikazujemo sličicu na odgovarajućem mestu na ekranu
   prozor.blit(tekst, (x, y))
                 

Најважније из ове лекције:
--------------------------

* Слике се у Пајгејм програме учитавају помоћу функције ``pg.image.load``, којој се као аргумент прослеђује назив фајла у коме је слика сачувана.
* Слике се у Пајгејм програмима у прозору приказују помоћу функције ``prozor.blit()``, чији су аргументи учитана слика и координате горњег левог темена те слике у прозору. 
* Када приказујемо текст у прозору, потребно је да прво одаберемо фонт који ћемо користити и то се ради помоћу функције ``pg.font.SysFont`` којој се као аргументи прослеђују назив фонта и величина слова. 
* Да бисмо направили сличицу која садржи жељени текст, потребно је да употребимо функцију ``font.render`` која као аргументе узима текст (ниску) који желимо да прикажемо, логичку варијаблу која одређује изглед текста и боју текста.
* Да бисмо приказали текст, користимо функцију ``prozor.blit()`` која као аргумент узима сличицу у којој је текст и координате горњег левог темена те сличице у прозору.
* Да бисмо добили димензије слика и текста користимо функције ``get_width()`` i ``get_height()``. Те димензије можемо користити како бисмо позиционирали слике и текст.
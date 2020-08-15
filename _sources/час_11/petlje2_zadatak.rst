Петље 2 задатак
===============

Шума
''''

.. questionnote::

   Поред скијашке стазе постављена су два реда јелки. Напиши програм
   који исцртава ову скијашку стазу.

Претпоставићемо да на располагању имамо функцију која црта јелку. Овај
пут ће та функција примати координате сидра (средину дна стабла
јелке), али и димензију јелке. Да би цртеж реалније изгледао
претпоставићемо да неће све крошње бити у истој нијанси зелене боје,
већ да ће неке бити тамније, а неке светлије. Стога ћемо функцији за
цртање јелке прослеђивати и четврти параметар који ће представљати
фактор промене основне зелене боје. Промену боје ћемо постићи кроз
посебну функцију која сваку појединачну компоненту дате боје множи са
задатим коефицијентом. Ако је тај коефицијент број мањи од 1, тада боја
постаје тамнија, а ако је већи од 1, тада боја постаје
светлија. Приликом сваког позива функције фактор ћемо одређивати као
насумично одабран реалан број из интервала :math:`[0.2, 2]`, позивом
функције ``random.uniform(0.2, 2.0)``.

У главном делу програма распоредићемо 6 јелки левог и 6 јелки десног
дрвореда. У петљама ћемо одржавати координате сидра текуће јелке. Леви
дрворед ће кретати мало испод линије хоризонта и мало лево од
половине ширине прозора и свако дрво ће бити померено доле и лево у
односу на претходно. То ћемо постићи тако што ћемо у сваком кораку
петље умањивати x и увећавати y координату. Слично, десни дрворед ће
кретати мало испод линије хоризонта и мало десно од половине ширине
прозора и свако дрво ће бити померено доле и десно у односу на
претходно. То ћемо постићи тако што ћемо у сваком кораку петље
увећавати и x и y координату. Да би се постигао ефекат перспективе,
свако наредно дрво биће мало веће у односу на претходно. То ћемо
постићи тако што ћемо у сваком кораку петље увећавати и димензију
текућег дрвета.

Допуни наредни програм на основу претходне дискусије.

.. activecode:: suma2
   :playtask:
   :nocodelens:
   :modaloutput: 
   :enablecopy:
   :includexsrc: _includes/suma2.py

   def promeni_nijansu(boja, faktor):
       (r, g, b) = boja
       return (round(r*faktor), round(g*faktor), ???)
    
   def jelka(x, y, dim, faktor_promene_boje):
       # boje koje cemo koristiti
       CRNA  = (0, 0, 0)
       ZELENA = (0, 100, 36)
       BRAON = (97, 26, 9)
       nijansa_zelene = promeni_nijansu(ZELENA, faktor_promene_boje)
       
       j = dim / 300
       pg.draw.rect(prozor, BRAON, (x-20*j, y-50*j, 40*j, 50*j))
       # krošnja - trougao A
       Alevo = (x-100*j, y-50*j)
       Adesno = (x+100*j, y-50*j)
       Agore = (x, y-150*j)
       pg.draw.polygon(prozor, nijansa_zelene, [Alevo, Adesno, Agore])
       # krošnja - trougao B
       Blevo = (x-75*j, y-100*j)
       Bdesno = (x+75*j, y-100*j)
       Bgore = (x, y-200*j)
       pg.draw.polygon(prozor, nijansa_zelene, [Blevo, Bdesno, Bgore])
       # krošnja - trougao C
       ???
    
   # bojimo pozadinu u belo
   prozor.fill(pg.Color("white"))
   horizont_y = visina * 0.55         # visina linije horizonta
   # crtamo nebo i sunce
   pg.draw.rect(prozor, pg.Color("skyblue"), (0, 0, sirina, horizont_y))
   pg.draw.circle(prozor, pg.Color("yellow"), (150, 150), 65)
    
   broj_stabala = 6
    
   # crtatmo levi drvored
   x, y, dim = sirina / 2 - 0.1 * sirina, horizont_y + 0.1 * visina,  150
   for i in range(broj_stabala):
       jelka(x, y, dim, random.uniform(0.2, 2.0))
       x -= 0.075 * sirina
       y += 0.05 * visina
       dim += 20
    
   # crtamo desni drvored
   ???
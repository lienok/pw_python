print "I will now count my chicken:"

print "Kurky", 25 + 30 / 6 # = 30 pocet
print "deleni 75/4 = ", 75 / 4 # = 18. Ked pridam desatinnu ciarku 75.0, potom to vydeli presne...
print "zvysok po deleni 75/4 = ", 75 % 4 # = 3 co je zvysok po deleni
print "Kohutiky", 100 - 25 * 3 % 4 # % znamena zvysok po deleni cisla pred % cislom za %. Tzn. 10 deleno 3 = 3 a zvysok je 1 => vysledok je 1.

print "Pocitam vajka:"
print 3 + 2 + 1 - 5 + 4 % 2 - 1.0 / 4 + 6 # = 6.75 najskor sa pocitaju zatvorky, exponenty, nasobenie, delenie, sucet a nakoniec rozdiel
print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6 # = 7
print 7/4 # vznika nepresnost tym, ze vysledok sa nezaokruhluje, ale sa iba nezapise cast vysledku za desatinnou ciarkou. Zobrazi iba cele cisla (ked su pre vypocet pouzite cele cisla bez desatinnej ciarky).
print 7.0/4.0 # presny vysledok
print 10.0/3.0 # presny vysledok s 11-timi desatinnymi miestami.

print "\je to pravda?"
print 3 + 2 < 5 - 7 # False
print
print "Kolko je 3+2?", 3 + 2
print "Kolko je 5-7?", 5 - 7

print "Oh, that's why it's False."

print "How about some more."

print "Je to vacsie?", 5 > -2 # True
print "Is it greater or equal?", 5 >= -2 # = True '=' musi byt za sipkou
print "Is it less or equal?", 5 <= -2# False
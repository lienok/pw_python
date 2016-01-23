my_name = 'Zed A. Shaw' # premenna nesmie zacinat cislom a nesmie byt cislo
my_age = 35# not a lie
my_height = 74.66 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'
my_height_in_cm = my_height * 2.54 

print "Let's talk about %s." % my_name
print "He's %d inches tall. And it means in %.2f cm." % (my_height, my_height_in_cm)
print "He's %d pounds heavy." % my_weight
print "Actually that's not to heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# tricky line
print "If I add %d, %d, and %d I get %f." % (my_age, my_height, my_weight, round (my_age + my_height + my_weight, 1)) # je mozne pouzivat matematicke funkcie pre print cislenych (decimal) premennych



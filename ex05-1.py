name = "Zed A. Shaw"
age = 35 # not lie
height = 74.0 / 0.4 # CM
weight = 180.0 * 2.2 # KG
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %r." % name
print "He's %r centimeters tall." % height
print "He's %r kilograms heavy." % weight
print "Actually that's not too heavy."
print "He's got %r eyes and %r hair ." % (eyes,hair )
print "His teeth are usually %r depending on the coffee." % teeth
# This line is tricky, try to get it excatly right.
print "If I add %r ,%r ,and %r I get %r." %(age, height ,weight ,age + height + weight )

my_name = 'Fritz Heider'
my_age = 34 #not a lie
my_height = 74 #inches
my_weight = 220
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %r inches tall." % my_height
print "He's %r pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %r eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

#this line is trickier try to get it exactly right
print "If I add %d, %d, and %d, i get %d." % ( my_age, my_weight, my_height, my_age + my_weight + my_height)

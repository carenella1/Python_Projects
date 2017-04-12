name = 'Chase S. Arenella'
age = 26 # soon to be 27
height = 6 #feet
weight = 185 # lbs
eyes = 'Green'
teeth = 'White'
hair = 'Brown'

print "Lets talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy"
print "He's got %s eyes and %s hair. " % (eyes, hair)
print "Hist teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
age, height, weight, age + height + weight)



inches = 2.54 #centimeters

centimeters = int(input("Enter a number of centimeters"))

print "Enter number of %s centimeters is equal to %s inches" % (centimeters, centimeters / inches )


pounds = .453592 # Kilograms

kilograms = int(input("Enter a number for Kilograms"))

print "Inputted number of %s Kilograms is equal to %s pounds" % (kilograms, kilograms / pounds)

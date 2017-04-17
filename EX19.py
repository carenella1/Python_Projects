def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You had %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

def milk_and_cereal():
    print "Enter a milk amount in cups:"
    milk_amount = raw_input()
    print "You type %r cups of milk" % milk_amount

print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)


print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese,amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10+20, 5+6)

print "And we can comine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

for num in range(0,10):
    milk_and_cereal()
    

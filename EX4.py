# Number of cars
cars = 100
# Used to calculate carpool_capacity
space_in_car = 4.0

drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_car
# In the excersise, carpool_capacity was not delcaredin line 7 throwing an error
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport" , carpool_capacity, "people today."
print "We have", passengers, "to carpool today"
print "We need to put about", average_passengers_per_car, "in each car"



i = 91.0
j = 12.0
x = i/j

print x + j + i / j

#variable and naming in python
cars  = 200
space_in_car = 4.0
drivers  = 60
passengers = 130
cars_not_driven  = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_car
average_passengers_per_car = passengers / cars_driven

#does the calculation and prints the output
print "There are", cars, "cars available"
print "There are only", drivers, "drivers available"
print "There will be ", cars_not_driven, "empty cars today"
print "We can transport", carpool_capacity, "people today"
print "We have", passengers, "to carpool today"
print "We need to put about", average_passengers_per_car, "people in each car"

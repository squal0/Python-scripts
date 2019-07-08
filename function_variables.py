#defines a function that takes 2 arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"

#giving the function numbers directly
print "We can just give the function numbers directly:"
cheese_and_crackers( 30, 50)

#using variables to pass to the function
print "OR, we can use variables from our script:"
amount_of_cheese = 45
amount_of_crackers = 60

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#doing math inside a function
print "We can even do math inside too:"
cheese_and_crackers( 43 + 17, 65 + 15)

#combining both variables and math within a function
print "And we can combine the, two variables and math:"
cheese_and_crackers(amount_of_cheese + 130, amount_of_crackers + 360)
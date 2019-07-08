people  = 30
cars = 40
buses = 15

if cars > people:
	print "We should take the cars."
elif cars < people:
	print "We should not take the cars."
else:
	print "We can't decide."

if buses > cars:
	print "That's too many buses."
elif buses < cars:
	print "Maybe we could take the buses instead."
else:
	print "We still can't decide"

if people > buses:
	print "Alright, let's just take the buses."
else:
	print "Fine, let's stay home then."

if (cars > people and buses < cars):
	print "We can always take both the cars and buses."
	print "It's really not that big of a deal."
else:
	print "Or we can always just walk there,"
	print "walking short distances is great exercise."

if (people > cars or cars < buses):
	print """People should take the buses if they want
			to be comfortable during the journey, since the 
			buses have the capacity to carry a lot of people
			"""
else:
	print "The management will decide on how people will be transported"
	print "Kindly wait for further instructions."

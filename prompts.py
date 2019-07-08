y = raw_input("Name? ")
yob = int(raw_input("Year of Birth? "))
cy = int(raw_input("Enter the current Year "))
age = cy - yob
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "Mr %r, So you are %d yrs old, %r tall and weigh %r" % (y, age, height, weight)
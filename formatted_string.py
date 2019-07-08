#script demonstrates the use of formatted strings
name = 'Raymond Allie'
age = 32 # definitely a  lie
height = 75.0 #inches
weight = 70.0 # kgs
eyes = 'brown'
teeth = 'white'
hair = 'black'

print "Today I'll be introducing %s." % name
print "His age is classified but the current age he uses is %d." % age
print "He is %d inches tall." % height
print "And weighs %d kilograms." % weight
print "Believe it or not he used to weigh more than this"
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on his frequency with the tooth brush" % teeth

#complex formatting, but I got the hang of it so not so complex
print "If we add %d, %d and %d we get %d" % (age, height, weight, age + height + weight)

weight_pounds = weight * 2.205
height_centimeters = height * 2.54

#print the output of the calculation
print "%s weight in pounds is %.2f lbs and height in centimeters is %.2f cm" % (name, weight_pounds, height_centimeters) 
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

# prints the formatted string based on the variables
print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

# prints a boolean to determine whether the joke was funny
hilarious  = False
joke_evaluation = "Isn't that joke so funny? ! %r"

print joke_evaluation % hilarious

w = "This is the left side of......"
e = " a string with a right side"

#uses the + sign to concatenate 2 strings
print w + e
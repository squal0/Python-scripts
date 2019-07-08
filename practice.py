print "Here I am practicing everything I have learnt in python"
print "You\'d need to know \' bout escapes with \\ that do \n newlines and \t tabs"

opinion = """
\t Truth be told I love this language \n
It\'s an easy to grasp and most of it just involves loose typing \n
I see why they call them scripting languages, compared to java python \n
is incredible. I feel like it will take me places.
\t Let\'s hope I get to learn more of this wonderful language \n
"""

print "=================================================="
print opinion
print "=================================================="

ten = 60 / 3 - 10
print "This should evaluate to ten: %s" % ten

def powerpuff_formular(ingredients):
	sugar = ingredients * 233
	spice = sugar * float(10.09)
	ev_nice = sugar / spice * 12

	return sugar,spice, ev_nice

powerpuff = 3000
sugar, spice, ev_nice = powerpuff_formular(powerpuff)

print "Proffessor Utonium wanted to create the girls by using the powerpuff formular of value %d" % powerpuff
print "He use %d sugar, %.2f spice, %.2f ev_nice." % (sugar, spice, ev_nice)

powerpuff /= 3
print "For the formula to work he'd require:"
print "%d sugar, %.2f spice, %.2f ev_nice" % powerpuff_formular(powerpuff)
print "for each girl."
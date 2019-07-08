from sys import exit

#function that starts the script
def start():
	print "\n======================================================================\n"
	print "\nYou've come to realization that You live in a virtual reality....."
	print "\nWith this realization agents are sent by the Matrix to kill you...!!!"
	print "\nLucky enough Morpheus and Trinity manage to save you."
	print """\nThey give you an option to join them in the war(redpill) or \ncontinue living in the virtual reality(bluepill).\n """
	print "How do you respond.....???\n"

	print "=======================================================================\n"

	response  = raw_input('> ')

	if ( response == "bluepill"):
		virtual_reality()
	elif( response == "redpill"):
		rabbit_hole()
	else:
		death("Agents caught up to you and you were erased")

#should the user choose the blue pill following function executes
def virtual_reality():
	print "\n======================================================================\n"
	print "You decided to get back to your normal life(virtual reality)"
	print "This is a world based on algorithms and not chance"
	print "The Matrix inserts you back into its code"
	print "Though it gives you 3 choices as long as you cooperate\n"

	choices = ["1. Erase Memory", "2. New Start", "3. Family"]

	for choice in choices:
		print "%s " % choice

	print "\n======================================================================\n"

	cooperation = False
	while True:

		decision  = int(raw_input('> '))

		if(decision == 1):
			memory_erase()
		elif(decision == 2):
			new_start()
		elif(decision == 3):
			family()
		else:
			death("Indecisiveness lead to your death")
			print "\n======================================================================\n"

def memory_erase():
	print "With option 1: You have chosen a memory wipe.\n"
	print "This will be based on how much you know about the Matrix...!!!"
	print """Note: A new identity will be created by default. 
	With the addition of false memories\n."""
	print "This calculation is based as follows:\n"

	#use lambdas to declare a functions
	yearWipe5 = lambda:"Memory of 5 years wiped."
	yearWipe10 = lambda:"Memory of 10 years wiped."
	yearWipe15 = lambda:"Memory of 15 years wiped."
	yearWipe20 = lambda:"Memory of 20 years wiped."
	indefiniteWipe = lambda:"Indefinite memory wipe."

	#declaring a dictionary of functions
	duration = {'5': yearWipe5,
				'10':yearWipe10,
				'15':yearWipe15,
				'20':yearWipe20,
			    'Indefinite': indefiniteWipe
				   }

	print "Enter the number of years you've know about the Matrix:\n"
	print"""
		Enter 5 for the range of (0 - 5) years
		Enter 10 for the range of (6 - 10) years
		Enter 15 for the range of (11 - 15) years
		Enter 20 for the range of (16 - 20) years
		Enter 0 for more than 20 years
	"""
	years = int(raw_input('> '))

	#using the if...else to call functions based on the user input
	if ( years == 5):
		print "\n", duration['5']() , "\n"
	elif( years == 10):
		print "\n", duration['10'](), "\n"
	elif(years == 15):
		print "\n", duration['15'](), "\n"
	elif( years == 20):
		print "\n", duration['20'](), "\n"
	elif(years == 0):
		print "\n", duration['Indefinite'](), "\n"
	else:
		print "\nThat option was not on the given instructions\n"
		print "Option List is: [5, 10, 15, 20 and 0] \n"


def new_start():
	print "Here the Matrix gives you the option to start a fresh."
	print "Though there is a catch."
	memory_erase()
	print "************************************************************************"
	print "\nA new start requires forgetting everything about the Matrix"
	print "\nBut you will be given the option to choose your own name."
	print "\nEverything else will be created according to the Matrix's algorithm.\n"

	name = raw_input('> ')
	print "\nHello ", name, ", Welcome to the new world...!!!\n"
	print "*************************************************************************\n"

	exit(0)
#when a user dies this function executes
def death(reason):
	print reason, "\nHow unfortunate\n"
	exit(0)

start()
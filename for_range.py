#represting the while.py as both a function and uses the for loop
def while_loop(nums, incr):
	numbers = []

	for i in range(nums):
		print "At the top i is %d" % i
		numbers.append(i)

		i += incr
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

	print "The numbers: "

	for num in numbers:
		print num

no = while_loop(10, 2)
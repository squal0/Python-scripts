def break_words(stuff):
	"""This function will break up words for us."""
	words =stuff.split(' ')
	return words

def sort_words(words):
	"""Sort the words"""
	return sorted(words)

def print_first_word(words):
	"""prints the first word after popping it off."""
	word = words.pop(0)
	return word

def print_last_word(words):
	"""Prints the last word after popping it off"""
	word = words.pop(-1)
	print word

def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words"""
	words = break_words(sentence) #calls the break_words function
	return sort_words(sentence) #calls the sort_words function

def print_first_and_last(sentence):
	"""Prints the first and the last words of a sentence."""
	words = break_words(sentence)
	#function calls 2 other functions print_first_word
	# and print_last_word
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentence):
	"""Sorts the words and then prints the first and the last one."""
	words =sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)


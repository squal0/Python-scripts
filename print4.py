"I am 6'2\" tall." # escape double quote inside a string
'I am 6\'2" tall.' # escape single quote inside a string

tabby_cat = "\tI'm tabbed in." #prints a tab space 
persian_cat = "I'm split \non a line." #splits the string on a line
backslash_cat = "I'm \\ a\\ cat." #escape a backslash inside a string

fat_cat = '''
I'll do a  list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

while True:
		for i in ["/", "-", "|", "\\", "|"]:
				print "%s\r" % i,
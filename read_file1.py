from sys import argv

script, filename = argv

#open the file for writing
print "Opening the file........"
target = open(filename, 'w')

#write to the file
print "I'll now write to the file whatever you print"
text = raw_input("> ")

target.write(text)
target.write("\n")
print "Closing the file"
target.close()
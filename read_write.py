from sys import argv

script, filename = argv

print "We are going to erase %r." % filename
print "If you dont want that, Hit CTRL_C (^C)."
print "If you dont want that hit return."

raw_input("?")

print "Opening the file......."
target = open(filename, 'w') #opens a file in write mode

print "Truncating the file. Goodbye!"
target.truncate() #truncates a file

print "Now I'm going to ask you for three lines."

line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

print "I'm going to write these to the file"

#uses the write method to write to the file
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally we close the file"
target.close() #function closes the file
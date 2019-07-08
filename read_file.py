from sys import argv
script, filename = argv

#opens a file
txt = open(filename)
print "Here is your file %r" % filename
print txt.read() #reads the file
print txt.close()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)
print txt_again.read()
print txt_again.close()

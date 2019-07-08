from sys import argv

script , user_name, job = argv
prompt = '-->'

print "Hi %s I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes  = raw_input(prompt)

print "Where do you live %s? " % user_name
lives = raw_input(prompt)

print "I heard you were a %s, that's so cool. " % job
print "If you dont mind me asking %s, what languages do you know? " % user_name
languages = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright so you have said %r about liking me.
You live in %r. Not really sure where that is.
You have a %r computer.
And know how to code in %r. Sweet.
""" % (likes, lives, computer, languages)
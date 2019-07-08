#script combines raw_input and argv to prompt for input from a user
from sys import argv

studentDetails, firstName, lastName, gender, age, course = argv

#prompting the user for input
firstName = raw_input("Please enter your First Name: ")
lastName = raw_input("Please enter your Last Name: ")
gender = raw_input("Enter your age: ")
course =raw_input("Please enter the current course you are doing: ")

#print
print "Script Name: ", studentDetails
print "First Name: ", firstName
print "Last Name ", lastName
print "Gender: ", gender
print "Age: ", age
print "Course: ", course
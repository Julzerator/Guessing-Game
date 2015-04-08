#Sets variables x, binary, do_not, and y.
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

#Prints to screen two of the variables set previously in the program.
print x
print y

#Prints to the screen the raw data (%r) and the string (%s)
print "I said: %r." % x
print "I also said: '%s'." % y

#Sets new variables.
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

#prints the new variables substitutes the formatted data in the 
#variable string with the variable set above.
print joke_evaluation % hilarious

#Sets even more variables! 
w = "This is the left side of..."
e = "a string with a right side."

#Concatenates the two variables.
print w + e
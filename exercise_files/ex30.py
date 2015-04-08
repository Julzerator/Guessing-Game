# Set variables
people = 40
cars = 40
trucks = 15

# if cars are greater than people.
if cars > people:
    print "We should take the cars."
# Else if cars are less than people.
elif cars < people:
    print "We should not take the cars."
# If both are false, print this:
else:
    print "We can't decide."

# If trucks are greater than cars.
if trucks > cars:
    print "That's too many trucks."
# Else if trucks are less than cars.
elif trucks < cars:
    print "Maybe we could take the trucks."
# If both are false, print this:
else:
    print "We still can't decide."

# If people are greater than trucks.
if people > trucks:
    print "Alright, let's just take the trucks."
# If above is not true, print this:
else:
    print "Fine, let's stay home then."
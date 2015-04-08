import random
# Put your code here
# greet player
print "Hello Numbers Master!"
# get player name
print "What's your name?",
name = raw_input()
# choose random number between 1 and 100
print "I've chosen a number between 1 and 100."
num = int(random.randrange(100))

print name + ", guess what number I've chosen!",

# while True:
#   get guess
#   if guess is incorrect:
#       give hint
#   else:
#       congratulate player
while True:
    guess = int(raw_input())
    if guess > num:
        print "Your guess is too high. Try again.",

    elif guess < num:
        print "Your guess is too low. Try again.",

    else:
        break

print "Congratulations! You are now the Numbers Master!!"
import random
# Put your code here
# greet player
print "Hello Numbers Master!"
# get player name
print "What's your name?",
name = raw_input()
# choose random number between 1 and 100
while True:
    print "I've chosen a number between 1 and 100."
    num = int(random.randrange(100)) + 1

    print "%s, guess what number I've chosen!" % name, 

# while True:
#   get guess
#   if guess is incorrect:
#       give hint
#   else:
#       congratulate player

    while True:
        try:
            guess = int(raw_input())
            if guess > 100:
                print "Your guess must be between 1 and 100. Dolt. Please try again."
            elif guess < num:
                print "Your guess is too low. Try again.",
            elif guess > num:
                print "Your guess is too high. Try again.",
            else:
                print "Congratulations! You are now the Numbers Master!!"
                break
        except ValueError:
            print "I do not compute anything but numbers. What is this garbage?"
            print "Please try again."

    print "Would you like to play again? Yes or No:",
    answer = raw_input()
    if answer != "Yes" and answer != "No":
        print "Please answer Yes or No:"
    elif answer == "Yes":
        print "Yay! Let's Play!"
    elif answer == "No":
        break

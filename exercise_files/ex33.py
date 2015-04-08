numbers = []

def looper(top, inc):
    for i in range(top):
        print "At the top i is %d" % i
        numbers.append(i)
        i = i + inc
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

looper(9, 3)

print "The numbers: "

for num in numbers:
    print num
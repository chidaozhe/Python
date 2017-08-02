def love():
    print "You must be very beautiful and have a boyfriend."
    print "What's your boyfriend of name?"
	
    next = raw_input("> ")
	
    if next == "liujigang":
	    print "Your boyfriend is very happy, because you remember his name."
	    #exit(0)
    else:
	    print "I can't belief you forget boyfriend's name!"
	
print "What's your name?"
next = raw_input("> ")

if next == "wulei":
    print "wulei is a beautiful girl!\n"
else:
    print "You write a wrong name!"
	
print "How old are you?"
age = [24, 25, 26]
for young in age:
    print " You are %d?" % young
	
next = raw_input("> ")

while next > 20:
    if next == "25":
        print "You are very young!\n"
        love()
    else:
        print "HeHe, You forget your real age."
        next = raw_input("Try again> ")

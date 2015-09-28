""" LET'S DO THIS """

#age = -18

#assert age > 0, "How is your age negative?\n"

#print "Your age is %d" % age


"""Assert try except finally raise"""

while True:

	try:

		numer = float(input("Enter a number:"))
		denom = float(input("Enter another number:"))

		print "After diving the numerator against the demoninator, the number you have is %f" % (numer/denom)
		break

	except ZeroDivisionError:

		print "An Error has occurred!"


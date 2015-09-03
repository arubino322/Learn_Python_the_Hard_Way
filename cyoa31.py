print "Do you want to play a game? (y/n)"

answer = raw_input("> ")

if answer == "y":
	print "You have a choice"
	print "1. Choose your own adventure."
	print "2. Riddle"

	choice = raw_input("> ")

	if choice == "1":
		print "You enter the castle silently. In front of you are guards. Do you:"
		print "1. Take them down quietly."
		print "2. Sneak past them."

		castle = raw_input("> ")

		if castle == "1":
			print "You've alarmed other guards and LOST THE GAME GOOD JOB DUDE"
		elif castle == "2":
			print "Like Legend of Zelda, you've found the princess and beat the game in \n an hour."
		else:
			print "Not a choice, you lose anyways."

	elif choice == "2":
		print "What's black and white and read all over?"

		riddle = raw_input("> ")

		if riddle == "newspaper":
			print "Hooray"
		else:
			print "Nice try, you lose"

	else:
		print "NOT AN OPTION GOODBYE"

elif answer == "n":
	print "Fine. Let's play tomorrow. You're not my mother."

else:
	print "You don't read good."

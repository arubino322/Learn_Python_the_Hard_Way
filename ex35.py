from sys import exit

def gold_room():
	print "This room is full of gold. How much do you take?"

	choice = raw_input("> ")

	if "0" in choice or "1" in choice:
		how_much = int(choice)
	else:
		dead("Man, learn to type a number.")

	if how_much < 50:
		print "Nice, you're not greedy, you win!"
		exit(0) #you imported this module at the top
	else:
		dead("You greedy bastard!")


def bear_room():
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	bear_moved = False

	while True:
		choice = raw_input("> ")

		if choice == "take honey":
			dead("The bear looks at you then slaps your face off.")
		elif choice == "taunt bear" and not bear_moved:
			print "The bear has moved from the door. You can go through it now."
			bear_moved = True
		elif choice == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		elif choice == "open door" and bear_moved:
			gold_room()
		else:
			print "I got no idea what that means."


def cthulhu_room():
	print "Here you see the great evil Cthulhu."
	print "He, it, whatever stares at you and you go insane."
	print "Do you flee for your life or eat your head?"

	choice = raw_input("> ")

	if "flee" in choice:
		start()
	elif "head" in choice:
		dead("Well that was tasty!")
	else:
		cthulhu_room()


def chess():
	print "You enter a room with Satan."
	print "He is sitting across a table with a chess board."
	print "Do you play or do you leave"

	choice = raw_input("> ")

	if "play" in choice:
		dead("Satan is a terrible chess player, but so are you")
	elif "leave" in choice:
		start()
	else:
		print "The devil wants to dance, and now you are best friends and live in hell."

def dead(why):
	print why, "Good job!"
	exit(1)


def start():
	print "You are in a dark room."
	print "There are three doors: door 1, door 2, door 3."
	print "Which one do you take?"

	choice = raw_input("> ")

	if choice == "1":
		bear_room()
	elif choice == "2":	
		cthulhu_room()
	elif choice == "3":
		chess()
	else:
		dead("You stumble around the room until you starve.")

start()
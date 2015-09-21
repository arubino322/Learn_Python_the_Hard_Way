#Incorporate a list into your "game"
#How bout we ask the user to input 3 of their favorite foods using raw_input.
#After, we will go on a series of functions determing what they would like to do with 
#their food. Use nested if statements, for loops, and a while loops (while True:).
#What kind of sequence/game do we want to write for the user to interact with?
#Cook/food fight/leave in your grocery bag for a really long time
from sys import exit
from sys import argv

script, name, event = argv

def grocery_list():
	print "You're at the market"
	print "You're having a party later, you need some appetizers."
	print "You only have money for 3 items. What do you buy?"

	grocery = []
	while True:
		i = raw_input("Enter item, or type done when done: ")
		
		if i != 'done':	
			grocery.append(i)
			print "Added %s to list" % i
		else:
			break

	print grocery
	print "You're pretty productive, now let's clean this joint."
	clean()

def clean():
	print "Man, this place is a mess."
	print "We better start to clean up."
	print "What should we do first?"

	choice = raw_input("> ")

	if "trash" in choice:
		print "Nice. Well let's drink. Oh no, you drank to much and passed out."
		end("Good job.")
	elif "dish" in choice:
		print "Nah, let's wait for your roommate to do them since it's his mess."
		procrastinate()
	else:
		procrastinate()


def procrastinate():
	print "We still have an hour before the party. Plenty of time to watch an episode of Narcos"
	print "You've always been better under pressure too."
	print "Uh oh, you fell asleep and ppl came over and now all your furniture is gone. Again. Great job."
	end("Why do I always do this.")

#more functions! make this a game.
def start():
	print "Hello %s, I hear you're going to have a %s, and you need to prepare." % (name, event)
	print "You can do three things: Grocery shop, clean the apartment, procrastinate."
	print "What do you choose?"

	choice = raw_input("> ")

	if "grocery" in choice:
		grocery_list()
	elif "clean" in choice:
		clean()
	elif "procrastinate" in choice:
		procrastinate()
	else:
		end("Worst. Party. Ever.")

def end(because):
	print because, "Good day sir!"
	exit(0)


start()
class Song(object):

	def __init__(self, lyrics, band):
		self.lyrics = lyrics
		self.band = band

	def sing_me_a_song(self, band):
		for line in self.lyrics:
			print line
		print "by " + self.band

#This would create the first INSTANCE object of the Song class
happy_bday = Song(["\nHappy birthday to you",
					"I don't want to get sued",
					"So I'll stop right here"], 'birthday')

#2nd instance object
bulls_on_parade = Song(["\nThey rally around tha family",
						"With pockets full of shells"], 'rage')

#3rd object
smile = Song(["\nSmile though your heart is aching",
				"Smile even though it's breaking",
				"When there's no clouds in the sky you'll get by"], 'chaplin')

#4th
screen_door = Song(["\nJesus Christ, I'm 26",
					"All the people I graduated with",
					"blah blah blah"], 'wonder years')

#Accessing object's attributes using the dot operator with object
happy_bday.sing_me_a_song('birthday')

bulls_on_parade.sing_me_a_song('rage')

smile.sing_me_a_song('chaplin')

screen_door.sing_me_a_song('wonder years')
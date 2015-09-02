def break_words(stuff):
	"""This function will break up words for us."""
	words = stuff.split(' ')
	return words
#Note: sorting the words only works after you split it and turn the sentence string into a list
def sort_words(words):
	"""Sorts the words."""
	return sorted(words)
#sorts the list. If you sort the string sentence, it words the punctuations and letters
def print_first_word(words):
	"""Prints the first word after popping it off."""
	word = words.pop(0)
	print word
#Again, .pop function only works for lists, no strings. It pops the word outta the list.
def print_last_word(words):
	"""Prints the last word after popping it off"""
	word = words.pop(-1)
	print word

def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words)

def print_first_and_last(sentence):
	"""Prints the first and last words fo the sentence."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)
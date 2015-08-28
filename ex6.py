#declaring x var, formatted to pull a variable
x = "There are %d types of people" % 10
#binary and do_not are sre string variables
binary = "binary"
do_not = "don't"
#y var is a string formatted to pull in other strings
y = "Those who know %s and those who %s" % (binary, do_not)

#printing them
print x
print y

#%r puts the string in quotes, and is the same as '%s'
print "I said: %r" % x
print "I also said: '%s'." % y

#more vars, joke_eval formatted to pull in hilarious,
#which is a boolean? but how come it doens't put it in
#quote? Let's test.
hilarious = False
#if you put quotes around it, joke_eval will print
#with the quotes
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "this is the left side of..."
e = "a string with a ride side."

#print the strings on same line
print w + e
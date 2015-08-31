#import argv module
from sys import argv
#define arguments
script, filename = argv
#open file, assign to object txt. .open makes a file object
txt = open(filename)
#read your object txt file using the .read command with no parameters/arguments. Print what you've read.
print "here's your file %r:" % filename
print txt.read()
#do it again, this time assigning the file_again var to the raw input you input
print "Type the filename again:"
file_again = raw_input("> ")
#open file again
txt_again = open(file_again)
#print again using .read() function
print txt_again.read()

txt.close()
txt_again.close()
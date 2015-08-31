from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")
#the paramenter 'w' in open stands for writing, and truncates the file if it already exists
print "Opening the file..."
target = open(filename, 'w')
#the .truncate() function seems repetitive since we already truncated the file with 'w' in open
print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1); target.write("\n"); target.write(line2); target.write("\n"); target.write(line3); target.write("\n")
#.close is basically 'Save As'
print "And finally, we close it."
target.close()
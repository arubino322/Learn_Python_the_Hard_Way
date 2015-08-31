from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "copying from %s to %s" % (from_file, to_file)

#we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()
#indata = open(from_file).read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()

#you can always copy files using UNIX commands (much easier).

#in one line:
#in_data = open(from_file).read(); out_data = open(to_file, 'w').write(in_data)
#note that this line closes the file as well, so no need for .close()
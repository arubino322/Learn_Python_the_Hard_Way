animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']

print animals

for i in animals:
	print i

for i in range(len(animals)):
	print "Index %d in the list is %s" % (i, animals[i])

another = [24, 'octopus', 'jesus', 'TRUE', 3, 18]

print another

for i in range(len(another)):
	print "Index %d in the list is %r" % (i, another[i])
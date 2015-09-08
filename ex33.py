i = 0
numbers = []

while i < 6:
	print "At the top i is %d" % i
	numbers.append(i)

	i = i + 1
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i

print "The numbers: "

for num in numbers:
	print num

#####
print "\nDo the same thing but with a function"

def practice(x,y):
	j = 0
	numbers1 = []
	while j < x:
		print "At the top j is %d" % j
		numbers1.append(j)
		j += y
		print "Numbers now: ", numbers1
		print "At the bottom j is %d" % j
	print "The numbers:"
	for num1 in numbers1:
		print num1

practice(21,3)

###
print "\nNow rewrite it, but with a for loop"

def practice2(n,s):
	i = 0
	numbers3 = range(0,n,s)
	for i in numbers3:
		print "At the top i is %d" % i
	print numbers3

practice2(10,2)
i = 0
numbers = []

def count_print(numzs, inc):
	
	for i in range(0, numzs):
		print "at the top i is %d" % i
		numbers.append(i)
		
		i = i + inc
		print "Numbers now:", numbers
		print "At the bottom i is %d" % i


	print "The numbers: "

	for cats in numbers:
		print cats
		
count_print(10, 3)
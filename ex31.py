print "You enter a dark room with two doors. Do you go through door #1 or door #2"

door = raw_input("> ")

if door == "1":
	print "There's a giant bear here eating a cheese cake. What do you do?"
	print "1, Take the cake."
	print "2, Scream at the bear."
	
	bear = raw_input("> ")
	
	if bear == "1":
		print "The bear eats your face off. Good Job!"
	elif bear == "2":
		print "The bear eats your legs off. Good Job!"
	else:
		print "well, doing %s is probably better. Bear runs away." % bear
	
elif door == "2":
	print "You stare into the endless abyss at Chtulu's retina."
	print "1. Blueberries."
	print "2. Yellow jacket clothespins"
	print "3, Understanding revolvers yelling melodies."
	
	insanity = raw_input("pick a number> ")
	
	if insanity == '1' or insanity == '2':
		print "Your body survives powered by a mind of jello! good job!"
	else:
		print "The insanity rots your eyes into a pool of suck. good job!"
		print "Now that you're slime, which way do you want to go? north or south?"
		
		move = raw_input("north or south? ")
		if move == 'n':
			print "You move north into a room with chandelliers and lava.\n"
			print "There are beautiful babes everywhere. YOu see some money on the ground"
		elif move == 's':
			print "You walk and walk untill you reach a great and vast desert."
			print "You see a giant wall of swords and guns."
		else:
			print "i dont understand"
		
else:
	print "You stunble around and fall on a knife and die. Good job!"
	
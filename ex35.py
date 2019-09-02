from sys import exit

def gold_room():
	print "This room is full of gold. How much do you take?"
	
	next = int(raw_input("> "))
	if next > 0 or "1" in next:
		how_much = int(next)
	else:
		dead("Man, learn to type a numbner.")
		
	if how_much < int(50):
		print "nice, you're not greedy, you win!"
		exit(0)
	else: 
		dead("You greedy bastard!")


def cosmic_horror():
	print "You stumble blindly in to a darkly lit room"
	print "looking to the right you find a small lamp and light it"
	print "Light washes the walls ahead of you and you see the most terrifying creature"
	print "its head like a rabid garfield the cat cartoon monster"
	print "Its body resembling a giant land squid."
	print "You may: attack, hide, flee"
	x2 = False

	while True:
		next = raw_input("WTF are you gonna do?!?  ")
	
		if next == "attack" and x2:
			win("you attack the creature bravely, but it muches you down and swallows your sould")
			dead("you shouldnt have messed with garfield")
		elif next == "attack" and not x2:
			print "your attack yields little affect"
			x2 = True
		elif next == "hide" and x2:
			print "this is a good time to hide, you slip away"
			cthulhu_room()
		elif next == "hide" and not x2:
			print "good idea hiding !!!!!"
			gold_room()
		else:
			dead("finally something else")
			
			
			
		
def bear_room():
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "how are you going to move the bear?"
	bear_moved = False
	
	while True:
		next = raw_input("> ")
		
		if next == "Take honey":
			dead("The bear looks at you then slaps your face off.")
		elif next == "taunt bear" and not bear_moved:
			print "The bear has moved from the door. You can go through it now."
			bear_moved = True
		elif next == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		elif next == "open door" and bear_moved:
			gold_room()
		elif next == "open door" and not bear_moved:
			win("this could be a serious problem")
			dead("the bear pulls out a 50 caliber and blasts you to pieces?")
		else:
			print "I got no idea what that means."
	
	
def cthulhu_room():
	print "Here you see the great evil Cthulhu."
	print "He, it, whatever stares at you and you go insanse."
	print "Do you flee for your life or eat your head?"
	print "You may: flee, head, or attack."

	next = raw_input("> ")
	
	
	if "flee" in next:
		start()
	elif "head" in next:
		win("so it doesnt look so good for you !!!!!!!")
		dead("Well that was tasty!")
	elif "attack" in next:
		print "you jump into the fray stabbing to little avail."
		cthulhu_room()
	else:
		cthulhu_room()

def win(why):
	print why, "we all win victories in our own ways"
	


def dead(why):
	print why, "Good job!"
	exit(0)
	
def start():
	print "You are in a dark room."
	print "There is a door to your right and lieft."
	print "Which one do oyu take? try going down"
	
	next = raw_input("> ")
	
	if next == "left":
		bear_room()
	elif next == "right":
		cthulhu_room()
	elif next == "down":
		cosmic_horror()
	else:
		dead("You stumble around the room until you starve.")
		
		
start()









	
	
	
	
	
	
		
		
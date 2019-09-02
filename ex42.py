## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass
	
## Dog is-a Animal
class Dog(Animal):
	
	def __init__(self, name):
		## Self has a name
		self.name = name
	
	## Cat is a Animal
class Cat(Animal):
	
	def __init__(self, name):
		## self has a name called name
		self.name = name
		
# Class Person is an object
class Person(object):

		def __init__(self,name):
			# name has a name
			self.name = name
			
			## Person has-a pet of some kind
			self.pet = name
			
##class employee is a person
class Employee(Person):
	
	def __init__(self, name, salary):
		## ?? what is this strange magic
		super(Employee, self).__init__(name)
		###
		self.salary = salary

## ??
class Fish(object):
	pass

## salmon is a fish
class Salmon(Fish):
	pass

## Halibut is a FISH
class Halibut(Fish):
	pass
	
	
## rover is a dog
rover = Dog("Rover")

## Satan is a cat
satan = Cat("Satan")

#mary is aperson
mary = Person("Mary")

#mary has a pet equal to satan
mary.pet = satan

## frank is an instance of employee class
frank = Employee("Frank", 120000)

#frank is a person and has a pet equal to rover
frank.pet = rover

##
flipper = Fish()

##crouse is an instance of salmon
crous = Salmon()


harry = Halibut()

print harry
print crous

print mary.name

print frank.pet

pet = frank.pet.name
print "franks bet is %s " % pet

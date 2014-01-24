import random

''' Class to hold profile of attributes of a single unique cat '''	
class Cat:
	name = "Kitty"
	sex = "Bastard"
	age = 0
	lives = 9
	strength = 0
	agility = 0
	attack = 0
	defense = 0
	cats_to_create = random.randint(1, 3)

	''' Function to create a single unique kitten and its attributes'''
	def create_kitten(self):
		while self.cats_to_create > 0:
			print "Kittens in new litter: " + str(self.cats_to_create)
			self.name = raw_input("Enter your new kitten's name: ")
			#self.sex = self.sex_of_kitten()
			self.age = 1
			self.lives = 9
			self.strength = random.randint(1, 3) # NEED TO add logic to assign starting strength
			self.agility = random.randint(1, 3) # NEED TO add logic to assign starting agility
			self.attack = random.randint(1, 3) # NEED TO add logic to assign starting attack
			self.defense = random.randint(1, 3) # NEED TO add logic to assign starting defense
			self.cats_to_create -= 1
			self.to_print()
			self.name = raw_input("Press enter to continue")
			print "====================================="
			#self.cats_to_create -= 1

	''' Function to determine the sex of the new kitten'''	
	def sex_of_kitten(self):
		boygirl = "Bastard"
		self.boygirl = 1 # Change to self.random.randint(1, 2)

		if self.boygirl == 1:
			self.sex = "Male"
		if self.boygirl == 2:
			self.sex = "Female"	

	def to_print(self):	
		print "====================================="
		print "Cat's Name: " + new_cat.name
		#print "Sex: " + new_cat.sex
		print "Age: " + str(new_cat.age)
		print "Lives: " + str(new_cat.lives)
		print "Strength: " + str(new_cat.strength)
		print "Agility: " + str(new_cat.agility)
		print "Attack: " + str(new_cat.attack)
		print "Defense: " + str(new_cat.defense)
		print "====================================="

	''' Cat Profile to hold all cat attributes'''
	cat_profile = {
		"Name": 0,
		"Sex": 0,
		"Age": 0,
		"Lives": 0,
		"Strength": 0,
		"Agility": 0,
		"Attack": 0,
		"Defense": 0,
	}

''' GAME LOOP '''

new_cat = Cat()
new_cat.create_kitten()

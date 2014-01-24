import random


class Litter:
	cats_litter_size = 0
		
	def litter_size(self):
		 self.cats_litter_size = random.randint(1, 10)
		 print self.cats_litter_size

''' Game Loop '''
new_litter = Litter()
new_litter.litter_size()
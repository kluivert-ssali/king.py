from random import randint
import time
class Poultry:
	sizes = {'Baby': 15.0, 'Adult': 45.0, 'Mature': 55.0 }
	number_of_eggs = 0
	x = 0
	y = 0
	def __init__(self):
		self.size = Poultry.sizes['Baby']
		self.rate_of_laying = 0 
		self.egg = 0 
		self.egg_layed = False
	def grow(self):
		rate_of_growth = self.size**0.1 if self.size < Poultry.sizes['Adult'] else self.size**0.01
		Poultry.x += 1
		print('Day {}'.format(Poultry.x))
		if self.size >= Poultry.sizes['Adult']:
			self.rate_of_laying = (1 - 0.002*Poultry.y)
			Poultry.y += 1
		self.size += rate_of_growth
		self.egg += self.rate_of_laying if self.rate_of_laying > 0 else 0
		if self.egg >= 1:
			self.egg_layed = True
			Poultry.number_of_eggs += 1 
			self.egg -= 1  
class feed:
	pass
Layer_1 = Poultry()
while True:
	Layer_1.grow()
	time.sleep(5)
	if Layer_1.egg_layed:
		print(Poultry.number_of_eggs)
		Layer_1.egg_layed = False
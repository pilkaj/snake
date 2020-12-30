"""
snakegame.py
v0.1

Description:
File contains main snake game classes and functionalities

Changelog:
v0.1 - initial version
"""

from Graphics.graphics import Graphics	#visualisation of the game
import time
import random

class Joint:
	"""
	Joint class
	"""
	def __init__(self, x, y):
		self.posx = x
		self.posy = y

class Snake:
	"""
	Snake class
	"""
	def __init__(self, length, x, y):
		self.length = length
		self.joints = []
		
	def updatejoints(self, newjoint):
		"""
		Goes through joints list and updates its joints
		"""
		print("<updatejoints> ToDo")
		if not self.isjointdistancevalid(self.joints[0], newjoint):
			# print("updatejoints: New position is not valid. Current x, y = %d, %d. New x, y = %d, %d.", joints[0].x, joints[0].y, x, y)
			return False
		# for joint in self.joints:
		# 	pass
			
	def isjointdistancevalid(self, jointa, jointb):
		print("<isjointdistancevalid>")
		# if self.jointdistance(jointa, jointb) == 1.0:
		# 	return True
		return False
		
	def jointdistance(self, jointa, jointb):
		print("<jointdistance> ToDo")
		return 0.0

class SnakeGame:
	""" 
	SnakeGame class
	Performs snake game. It counts snake length and game time.
	Returns a tuple (snake_length, game_time).
	"""
	def __init__(self, mode):
		self.mode = mode
		if self.mode == "graphical":
			self.screen = Graphics(800, 800, 16, 16)	#for some reason size 800x800 - 15x15 is displayed not properly, IDK...
		self.running = True
		

	def playgame(self):
		"""
		Runs the game. Allows to set up initial values.
		Or holds space for adding menu.
		"""

		initial_length = 3
		initial_speed = 3		
		fruits_amount = 2

		(total_length, total_time) = self.rungame(initial_length, initial_speed, fruits_amount)

		return (total_length, total_time)
	
	def rungame(self, init_length, init_speed, fruits_no):
		"""
		Runs the game.
		"""
		print("Runing new game.")

		# Samples only
		self.snakeSample = Snake(3, 500, 500)
		self.fruits = []
		self.snakeSample.joints = [Joint(5,8), Joint(4,8), Joint(3,8)]
		for i in range(fruits_no):
			self.fruits.append(Joint(random.randrange(16), random.randrange(16)))
		
		while self.running:
			# if inputfromplayer:
			# 	playerinput = # get input from player
			# 	applyinput()
			# dostep(snake)
			# wait(1.0/init_speed)
			self.running = self.screen.drawScreen(self.snakeSample, self.fruits)

			# code below is only demo to show working visualisation, it should be handled somehow more intelligent
			time.sleep(1)	
			for joint in self.snakeSample.joints:
				joint.posx += 1
		
		print("Game finished.")
		
		return "total_length_to_return", "total_time_to_return"
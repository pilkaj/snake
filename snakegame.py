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
import queue
import keyboard
from directions import Directions

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
		self.directionenum = Directions()
		self.length = length
		self.direction = self.directionenum.RIGHT
		self.joints = []

	def applyPlayerInput(self, input):
		print("<applyPlayerInput>", input)
		# TODO: work on this

	def updateSnakePosition(self, fruits):
		print("<updateSnakePosition>")
		# TODO: Work on this
		for joint in self.joints:
			joint.posx += 1
		
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
	
	def updateDirection(self, direction):
		print("<updateDirection>")
		self.direction = direction
			
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

		# keyboard input variables
		self.playerInput = queue.Queue()	# FIFO queue
		self.lastRecordedInput = None
		self.keyWasPressed = False
		self.lastInputChanged = False
		

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

	def recordPlayerInput(self):
		if not self.keyWasPressed:
			self.lastInputChanged = False
			if keyboard.is_pressed('up') and self.lastRecordedInput != Directions().UP: # if arrow 'up' is pressed 
				self.lastRecordedInput = Directions().UP
				self.lastInputChanged = True
			elif keyboard.is_pressed('down') and self.lastRecordedInput != Directions().DOWN:  # if arrow 'down' is pressed 
				self.lastRecordedInput = Directions().DOWN
				self.lastInputChanged = True
			elif keyboard.is_pressed('left') and self.lastRecordedInput != Directions().LEFT:  # if arrow 'left' is pressed 
				self.lastRecordedInput = Directions().LEFT
				self.lastInputChanged = True
			elif keyboard.is_pressed('RIGHT') and self.lastRecordedInput != Directions().RIGHT:  # if arrow 'right' is pressed 
				self.lastRecordedInput = Directions().RIGHT
				self.lastInputChanged = True

			if self.lastInputChanged:
				self.keyWasPressed = True
				self.playerInput.put(self.lastRecordedInput)

	def getPlayerLastInput(self):
		self.keyWasPressed = False	# reset flag for next loop
		if not self.playerInput.empty():
			return self.playerInput.get()
		else:
			return None

	
	def rungame(self, init_length, init_speed, fruits_no):
		"""
		Runs the game.
		"""
		print("Runing new game.")

		# Samples only
		snake = Snake(3, 500, 500)
		fruits = []
		snake.joints = [Joint(5,8), Joint(4,8), Joint(3,8)]
		for _ in range(fruits_no):
			fruits.append(Joint(random.randrange(16), random.randrange(16)))
		speed = init_speed

		while self.running:
			period = 1 / speed
			time_stamp = time.monotonic()
			while time.monotonic() - time_stamp < period:
				self.recordPlayerInput()

			key = self.getPlayerLastInput()
			if key != None:
				snake.applyPlayerInput(key)
				
			snake.updateSnakePosition(fruits)
			self.running = self.screen.drawScreen(snake, fruits)
		
		print("Game finished.")
		
		return "total_length_to_return", "total_time_to_return"

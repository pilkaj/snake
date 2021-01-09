"""
snakegame.py
v0.1

Description:
File contains main snake game classes and functionalities

Changelog:
v0.1 - initial version
"""

from Graphics.graphics import Graphics	#visualisation of the game
from Logic.directions import Directions
from Logic.joint import Joint
from Logic.snake import Snake
import time
import random
import queue
from pynput import keyboard

class SnakeGame:
	""" 
	SnakeGame class
	Performs snake game. It counts snake length and game time.
	Returns a tuple (snake_length, game_time).
	"""
	def __init__(self, mode, screenSize_x, screenSize_y, fieldSize_x, fieldSize_y):
		self.mode = mode
		self.screenSizeX = screenSize_x
		self.screenSizeY = screenSize_y
		self.fieldSizeX = fieldSize_x
		self.fieldSizeY = fieldSize_y
		if self.mode == "graphical":
			self.screen = Graphics(self.screenSizeX, self.screenSizeY, self.fieldSizeX, self.fieldSizeY)
		self.running = True

		# keyboard input variables
		self.playerInputsSize = 2	# max size of queue which stores player input
		self.playerInputsQueue = queue.Queue(self.playerInputsSize)	# FIFO queue
		self.keyDown = {keyboard.Key.up: False, keyboard.Key.down: False, keyboard.Key.right: False, keyboard.Key.left: False}	# state of key - true = key is pressed down, false = key is released
		self.lastRecordedInput = None
		# Listener thread to catch key strokes
		listener = keyboard.Listener(on_press=self.key_press, on_release=self.key_release)
		listener.start()
		
	def key_press(self, key):
		try:
			if key != self.lastRecordedInput and not self.keyDown[key] and not self.playerInputsQueue.full():	# if key is different than last one and was pressed for the first time and queue is not full
				self.keyDown[key] = True
				self.lastRecordedInput = key
				# add enum into playerInputsQueue
				self.addToPlayerInputs(key)
		except:
			print("key", key, "is not being recorded")
			
	def key_release(self, key):
		self.keyDown[key] = False
		# print("Key released", key)

	def addToPlayerInputs(self, key):
		direction = None
		if key == keyboard.Key.up:
			direction = Directions.UP
		elif key == keyboard.Key.down:
			direction = Directions.DOWN
		elif key == keyboard.Key.right:
			direction = Directions.RIGHT
		elif key == keyboard.Key.left:
			direction = Directions.LEFT
		if direction is not None:
			self.playerInputsQueue.put(direction)

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

	def getPlayerLastInput(self):
		if not self.playerInputsQueue.empty():
			return self.playerInputsQueue.get()
		else:
			return None

	
	def rungame(self, init_length, init_speed, fruits_no):
		"""
		Runs the game.
		"""
		print("Runing new game.")

		# Game init
		snake = Snake()
		snake.joints = [Joint(5,8), Joint(4,8), Joint(3,8)]
		fruits = []
		for _ in range(fruits_no):
			fruits.append(Joint(random.randrange(self.fieldSizeX), random.randrange(self.fieldSizeY)))
		walls = []
		for i in range(self.fieldSizeX):
			walls.append(Joint(i, 0))
			walls.append(Joint(i, self.fieldSizeY - 1))
		for i in range(self.fieldSizeY - 2):
			walls.append(Joint(0, i + 1))
			walls.append(Joint(self.fieldSizeX - 1, i + 1))
		speed = init_speed

		period = 1 / speed
		
		time_stamp = time.monotonic()

		while self.running:

			if time.monotonic() - time_stamp > period:
					
				time_stamp = time.monotonic()

				key = self.getPlayerLastInput()
				if key != None:
					snake.applyPlayerInput(key)
					
				snake.updateSnakePosition()

				if snake.isInCollisionWith(snake.joints[1:]) or snake.isInCollisionWith(walls):
					self.running = False
					break
				elif snake.isInCollisionWith(fruits):
					snake.enlarge()

			self.running = self.screen.drawScreen(snake, fruits, walls)
		
		print("Game finished.")
		
		return "total_length_to_return", "total_time_to_return"

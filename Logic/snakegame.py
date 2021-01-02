"""
snakegame.py
v0.1

Description:
File contains main snake game classes and functionalities

Changelog:
v0.1 - initial version
"""

from Graphics.graphics import Graphics	#visualisation of the game
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
	def __init__(self, mode):
		self.mode = mode
		if self.mode == "graphical":
			self.screen = Graphics(800, 800, 16, 16)	# for some reason size 800x800 - 15x15 is displayed not properly, IDK...
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
		initial_speed = 13
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
		snake = Snake(3, 500, 500)
		snake.joints = [Joint(5,8), Joint(4,8), Joint(3,8)]
		fruits = []
		for _ in range(fruits_no):
			fruits.append(Joint(random.randrange(16), random.randrange(16)))
		speed = init_speed

		while self.running:
			period = 1 / speed
			time.sleep(period)

			key = self.getPlayerLastInput()
			if key != None:
				snake.applyPlayerInput(key)
				
			snake.updateSnakePosition()
			self.running = self.screen.drawScreen(snake, fruits)
		
		print("Game finished.")
		
		return "total_length_to_return", "total_time_to_return"

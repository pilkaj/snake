from .directions import Directions
from copy import deepcopy

class Snake:
	"""
	Snake class
	"""
	def __init__(self, length, x, y):
		self.directionenum = Directions
		self.length = length
		self.direction = self.directionenum.UP
		self.joints = []
		self.lastTail = None

	def applyPlayerInput(self, input):
		print("<applyPlayerInput>", input)
		if self.direction == Directions.UP and input == Directions.DOWN:
			return
		if self.direction == Directions.DOWN and input == Directions.UP:
			return
		if self.direction == Directions.RIGHT and input == Directions.LEFT:
			return
		if self.direction == Directions.LEFT and input == Directions.RIGHT:
			return
		# else input is valid and apply it
		self.direction = input

	def updateSnakePosition(self):
		print("<updateSnakePosition>")

		head = self.joints[0]     # get pointer to snake head
		tail = self.joints.pop()  # pop snake tail
		self.lastTail = deepcopy(tail)

		if self.direction == Directions.UP:
			tail.posx = head.posx
			tail.posy = head.posy - 1
		elif self.direction == Directions.DOWN:
			tail.posx = head.posx
			tail.posy = head.posy + 1
		elif self.direction == Directions.LEFT:
			tail.posx = head.posx - 1
			tail.posy = head.posy
		elif self.direction == Directions.RIGHT:
			tail.posx = head.posx + 1
			tail.posy = head.posy

		self.joints.insert(0, tail) # inserts poped and updated tail as the new head at the beginning of joints list

	def isInCollisionWith(self, obj_list):
		head = self.joints[0]
		for item in obj_list:
			if head.posx == item.posx and head.posy == item.posy:
				print("Snake <isInCollisionWith>", item.posx, item.posy)
				return True
		return False

	def enlarge(self):
		self.joints.append(self.lastTail)
class Joint:
	"""
	Joint class
	"""
	def __init__(self, x, y):
		self.posx = x
		self.posy = y

	def __eq__(self, other):
		if self.posx == other.posx and self.posy == other.posy:
			return True

		return False

	def __str__(self):
		return str(self.posx) + " " + str(self.posy)

	__repr__ = __str__
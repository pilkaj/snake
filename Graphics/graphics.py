import pygame
from .colors import Colors

class Graphics:
  """
	__init__() 
  
  Parameters:
    width_pixels: width in pixels
    height_pixels: height in pixels
    width_size: number of rectangles on X axis
    height_size: number of rectangles on Y axis
	"""
  def __init__(self, width_pixels, height_pixels, width_size, height_size):
    self.game_size = [width_size, height_size]
    self.screen_size = [width_pixels, height_pixels]
    self.rect_dimensions = [self.screen_size[0]/self.game_size[0], self.screen_size[1]/self.game_size[1]]
    self.screen = pygame.display.set_mode([width_pixels, height_pixels])  # Set up the drawing window
    self.running = True
    self.colors = Colors()
    pygame.init()

  def drawRectangle(self, posx, posy, color):
    pygame.draw.rect(self.screen, color, (*self.posToPix(posx, posy), self.rect_dimensions[0], self.rect_dimensions[1])) #https://stackoverflow.com/questions/1993727/expanding-tuples-into-arguments

  def checkEvent(self):
    # Did the user click the window close button?
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.running = False

  def posToPix(self, posx, posy):
    return posx*self.rect_dimensions[0], posy*self.rect_dimensions[1]

  def drawBackground(self):
    for x in range(self.game_size[0]):
      for y in range(self.game_size[1]):
        color = self.colors.BG_FIELD_DARK if ((x+y) % 2 == 0) else self.colors.BG_FIELD_LIGHT # create background grid - if sum of coordinates even, than dark color
        self.drawRectangle(x, y, color)

  def drawSnake(self, snake):
    # Draw head
    self.drawRectangle(snake.joints[0].posx, snake.joints[0].posy, self.colors.SNAKE_HEAD)
    # Draw body
    for part in snake.joints[1:]:
      self.drawRectangle(part.posx, part.posy, self.colors.SNAKE_BODY)

  def drawFruit(self, fruit):
    self.drawRectangle(fruit.posx, fruit.posy, self.colors.FRUIT)

  """
  drawScreen()

  Parameters:
    snake: object Snake (head is joint[0])
    fruit: object Joint

  Return value:
    True: game is running
    False: user closed a window
  """
  def drawScreen(self, snake, fruit):
    self.checkEvent() # check if user pressed "close window" button
    if self.running:    
      self.drawBackground() #draw static background of playing area
      self.drawSnake(snake)
      self.drawFruit(fruit)
      pygame.display.update() # Updates the display  
      return True
    else:
      pygame.quit()
      return False


  
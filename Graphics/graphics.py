import pygame
# from pygame.locals import * 
from .colors import Colors

class Graphics:
  """
	__init__() 
  parameters:
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
    self.events = []
    self.running = True
    self.colors = Colors()
    pygame.init()

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
        color = self.colors.BG_DARK if ((x+y) % 2 == 0) else self.colors.BG_LIGHT
        pygame.draw.rect(self.screen,  color, (*self.posToPix(x, y), self.rect_dimensions[0], self.rect_dimensions[1])) #https://stackoverflow.com/questions/1993727/expanding-tuples-into-arguments

  
  def drawSnake(self, snake):
    # Draw head
    pygame.draw.rect(self.screen, self.colors.SNAKE_HEAD, (*self.posToPix(snake.joints[0].posx, snake.joints[0].posy), self.rect_dimensions[0], self.rect_dimensions[1]))

    # Draw tail
    for part in snake.joints[1:]:
      pygame.draw.rect(self.screen, self.colors.SNAKE_TAIL, (*self.posToPix(part.posx, part.posy), self.rect_dimensions[0], self.rect_dimensions[1]))


  def drawScreen(self, snake, fruit):

    self.checkEvent() # check if user pressed "close window" button

    if self.running:    
      self.drawBackground() #draw static background of playing area
      self.drawSnake(snake)
      pygame.display.update() # Updates the display  
      return True

    else:
      pygame.quit()
      return False


  
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

  def drawBackground(self):
    # self.screen.fill((255, 255, 255)) # Fill the background with white

    # Draw grid
    for x in range(self.game_size[0]):
      for y in range(self.game_size[1]):
        color = self.colors.BG_DARK if ((x+y) % 2 == 0) else self.colors.BG_LIGHT
        pygame.draw.rect(self.screen,  color, (x*self.rect_dimensions[0], y*self.rect_dimensions[1], self.rect_dimensions[0], self.rect_dimensions[1]))

  
  def drawSnake(self):
    # Draw a solid blue circle in the center
    pygame.draw.circle(self.screen, (0, 90, 30), (250, 250), 75)

  def drawScreen(self, snake, fruit):

    self.checkEvent() # check if user pressed "close window" button

    if self.running:    
      self.drawBackground() #draw static background of playing area
      self.drawSnake()
      pygame.display.update() # Updates the display  
      return True

    else:
      pygame.quit()
      return False


  
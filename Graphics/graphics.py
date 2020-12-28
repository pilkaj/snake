"""
high level support for doing this and that.
"""

import pygame
from pygame.locals import *


class Graphics:
  def __init__(self):
    pygame.init()    
    self.screen = pygame.display.set_mode([800, 800])  # Set up the drawing window
    self.events = []
    self.running = True

  def checkEvent(self):
    # Did the user click the window close button?
    for event in pygame.event.get():
      if event.type == QUIT:
        self.running = False

  def drawBackground(self):
    # Fill the background with white
    self.screen.fill((255, 255, 255))
  
  def drawSnake(self):
    # Draw a solid blue circle in the center
    pygame.draw.circle(self.screen, (0, 0, 255), (250, 250), 75)

  def drawScreen(self, snake):

    self.checkEvent() # check if user pressed "close window" button

    if self.running:    
      self.drawBackground() #draw static background of playing area
      self.drawSnake()
      pygame.display.update() # Updates the display  
      return True

    else:
      pygame.quit()
      return False


  
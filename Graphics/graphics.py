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

  def drawScreen(self):
    self.checkEvent()
    if self.running:    
      # Fill the background with white
      self.screen.fill((255, 255, 255))

      # Draw a solid blue circle in the center
      pygame.draw.circle(self.screen, (0, 0, 255), (250, 250), 75)

      # Updates the display
      pygame.display.update()

    else:
      # Done! Time to quit.
      pygame.quit()


  
# https://stackoverflow.com/questions/36932/how-can-i-represent-an-enum-in-python
from enum import Enum

class Directions(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
    QUIT = 10
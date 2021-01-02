from .Logic.snakegame import SnakeGame #see https://www.geeksforgeeks.org/why-import-star-in-python-is-a-bad-idea/

def main():
  ''' 
  python my memory dust eraser application
  '''
  print("This is a memory dust eraser application")
  print("Let's try to write a snake game")

  ''' play snake '''
  mygame = SnakeGame("graphical")
  (snake_length, game_time) = mygame.playgame()

  print("You played a snake game.")
  print("Your snake reached length", snake_length, "in total time", game_time, "seconds.")


if __name__ == "__main__":  #see https://www.freecodecamp.org/news/if-name-main-python-example/
  main()


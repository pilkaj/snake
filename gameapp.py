from snakegame import SnakeGame

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


if __name__ == "__main__":
  main()


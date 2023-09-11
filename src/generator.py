from maze import Maze
import sys

if len(sys.argv)>1:
  size = int(sys.argv[1]) #gets CLI parameter for size
else:
  size=20 #default

maze = Maze(size)
maze.generate_maze()
maze.print()
print("Welcome to 2D maze")

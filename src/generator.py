from maze import Maze

if len(sys.argv>1):
  size = sys.argv[1]
else:
  size=20

maze = Maze(size)
maze.generate_maze()
maze.print()
print("Welcome to 2D maze")

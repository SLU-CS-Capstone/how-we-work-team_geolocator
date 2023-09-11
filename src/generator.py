from maze import Maze

size = sys.argv[1]

maze = Maze(size)
maze.generate_maze()
maze.print()
print("Welcome to 2D maze")

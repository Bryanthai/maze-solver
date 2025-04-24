from tk import *
from cell import Cell
from maze import Maze
def main():
    win = Window(1100, 1100)
    maze = Maze(10,10,10,10,50,50,win)
    maze.break_entrance_and_exit()
    maze.break_walls(0,0)
    maze.reset_cell()
    maze.draw_head()
    maze._solve_re(0,0)
    maze.draw_end()
    print("Solved the maze !!!")
    win.wait_for_close()
    pass

main()
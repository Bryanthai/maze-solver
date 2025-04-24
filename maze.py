from cell import Cell
from tk import Line, Point
import time
import random
class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win = None, seed = None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        if seed != None:
            self.seed = random.seed(seed)
        self.create_cells()
    
    def create_cells(self):
        self.cells = []
        x1 = self.x1
        x2 = self.x1 + self.cell_size_x
        y1 = self.y1
        y2 = self.y1 + self.cell_size_y
        for j in range(self.num_cols):
            new_list = []
            y1 = self.y1
            y2 = self.y1 + self.cell_size_y
            for i in range(self.num_rows):
                new_list.append(Cell(x1,y1,x2,y2,self.win))
                y1 += self.cell_size_y
                y2 += self.cell_size_y
            self.cells.append(new_list)
            x1 += self.cell_size_x
            x2 += self.cell_size_x
            for list in self.cells:
                for cell in list:
                    cell.draw()
                    self.win.redraw()
                    time.sleep(0.0005)
        return
    
    def draw_cells(self):
        for list in self.cells:
            for cell in list:
                cell.draw()
                self.animate()
    
    def animate(self):
        self.win.redraw()
        time.sleep(0.08)

    def break_entrance_and_exit(self):
        first_cell = self.cells[0][0]
        last_cell = self.cells[-1][-1]
        first_cell.remove_walls(left=True)
        last_cell.remove_walls(bottom=True)
    
    def break_walls(self, i ,j):
        current_cell = self.cells[i][j]
        current_cell.visited = True
        while 1:
            directions = []
            if i > 0 and self.cells[i-1][j].visited == False:
                directions.append((i-1, j))
            if j > 0 and self.cells[i][j-1].visited == False:
                directions.append((i, j-1))
            if i < self.num_cols - 1 and self.cells[i+1][j].visited == False:
                directions.append((i+1, j))
            if j < self.num_rows -1 and self.cells[i][j+1].visited == False:
                directions.append((i, j+1))
            if directions == []:
                return
            randnum = random.randint(1,4)%len(directions)
            chose_cell = directions[randnum]
            if chose_cell[0] == i-1:
                current_cell.remove_walls(left=True)
                self.cells[i-1][j].remove_walls(right=True)
            elif chose_cell[1] == j-1:
                current_cell.remove_walls(top=True)
                self.cells[i][j-1].remove_walls(bottom=True)
            elif chose_cell[0] == i+1:
                current_cell.remove_walls(right=True)
                self.cells[i+1][j].remove_walls(left=True)
            elif chose_cell[1] == j+1:
                current_cell.remove_walls(bottom=True)
                self.cells[i][j+1].remove_walls(top=True)
            self.animate()
            self.break_walls(chose_cell[0],chose_cell[1])
        pass

    def reset_cell(self):
        for lists in self.cells:
            for cell in lists:
                cell.visited = False
        return
    
    def _solve_re(self, i ,j):
        self.animate()
        current_cell = self.cells[i][j]
        current_cell.visited = True
        if current_cell == self.cells[-1][-1]:
            return True
        if i > 0 and self.cells[i-1][j].visited == False and current_cell.has_left_wall == False and self.cells[i-1][j].has_right_wall == False:
            current_cell.draw_move(self.cells[i-1][j])
            result = self._solve_re(i-1,j)
            if result:
                return True
            else:
                current_cell.draw_move(self.cells[i-1][j], True)
        if j > 0 and self.cells[i][j-1].visited == False and current_cell.has_top_wall == False and self.cells[i][j-1].has_bottom_wall == False:
            current_cell.draw_move(self.cells[i][j-1])
            result = self._solve_re(i,j-1)
            if result:
                return True
            else:
                current_cell.draw_move(self.cells[i][j-1], True)
        if i < self.num_cols - 1 and self.cells[i+1][j].visited == False and current_cell.has_right_wall == False and self.cells[i+1][j].has_left_wall == False:
            current_cell.draw_move(self.cells[i+1][j])
            result = self._solve_re(i+1,j)
            if result:
                return True
            else:
                current_cell.draw_move(self.cells[i+1][j], True)
        if j < self.num_rows -1 and self.cells[i][j+1].visited == False and current_cell.has_bottom_wall == False and self.cells[i][j+1].has_top_wall == False:
            current_cell.draw_move(self.cells[i][j+1])
            result = self._solve_re(i,j+1)
            if result:
                return True
            else:
                current_cell.draw_move(self.cells[i][j+1], True)
        return False
    
    def draw_head(self):
        head = self.cells[0][0]
        starting_point = Point(self.x1 , self.y1 + (self.cell_size_y)//2)
        middle_point = Point((head.x1 + head.x2)//2, (head.y1+head.y2)//2)
        line = Line(starting_point, middle_point)
        self.win.draw_line(line, "red")
        return

    def draw_end(self):
        end = self.cells[-1][-1]
        ending_point = Point(self.x1 + self.cell_size_x * self.num_cols - (self.cell_size_x)//2, self.y1 + self.cell_size_y * self.num_rows)
        middle_point = Point((end.x1 + end.x2)//2, (end.y1+end.y2)//2)
        line = Line(ending_point, middle_point)
        self.win.draw_line(line, "red")
        return

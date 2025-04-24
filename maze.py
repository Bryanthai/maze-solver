from cell import Cell
import time
class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
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
                self.animate()
        return
    
    def animate(self):
        self.win.redraw()
        time.sleep(0.05)
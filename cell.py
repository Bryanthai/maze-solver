from tk import *

class Cell():
    def __init__(self, x1, y1, x2, y2, win = None, has_left_wall = True, has_right_wall = True, has_top_wall = True, has_bottom_wall = True):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.win = win
        self.visited = False

    def draw(self):
        if self.has_left_wall == True:
            line = Line(Point(self.x1, self.y1), Point(self.x1, self.y2))
            self.win.draw_line(line, "black")
        if self.has_right_wall == True:
            line = Line(Point(self.x2, self.y1), Point(self.x2, self.y2))
            self.win.draw_line(line, "black")
        if self.has_top_wall == True:
            line = Line(Point(self.x1, self.y1), Point(self.x2, self.y1))
            self.win.draw_line(line, "black")
        if self.has_bottom_wall == True:
            line = Line(Point(self.x1, self.y2), Point(self.x2, self.y2))
            self.win.draw_line(line, "black")
        return
    
    def draw_move(self, to_cell, undo = False):
        mid = Point((self.x1 + self.x2)//2, (self.y1 + self.y2)//2)
        to_mid = Point((to_cell.x1 + to_cell.x2)//2, (to_cell.y1 + to_cell.y2)//2)
        line = Line(mid, to_mid)
        if undo == True:
            self.win.draw_line(line, "#d9d9d9")
        else:
            self.win.draw_line(line, "red")
        return
    
    def remove_walls(self,left=False,right=False,top=False,bottom=False):
        if left == True:
            self.has_left_wall = False
            line = Line(Point(self.x1, self.y1), Point(self.x1, self.y2))
            self.win.draw_line(line, "#d9d9d9")
        if right == True:
            self.has_right_wall = False
            line = Line(Point(self.x2, self.y1), Point(self.x2, self.y2))
            self.win.draw_line(line, "#d9d9d9")
        if top == True:
            self.has_top_wall=False
            line = Line(Point(self.x1, self.y1), Point(self.x2, self.y1))
            self.win.draw_line(line, "#d9d9d9")
        if bottom == True:
            self.has_bottom_wall=False
            line = Line(Point(self.x1, self.y2), Point(self.x2, self.y2))
            self.win.draw_line(line, "#d9d9d9")
        return

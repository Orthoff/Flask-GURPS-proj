#!/bin/python3

from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return "get solvers here!!!"
app.run(host="0.0.0.0", port=80)

class RegionGrid:
    def __init__(self, size):
        self.grid = []
        for i in range(size):
            self.row = []
            for j in range(size):
                
                self.row.append()
            self.grid.append(self.row)
    class Cell:
        def __init__(self, x, y, lWall:bool, uWall:bool, rWall:bool,dWall:bool):
            self.rWall = rWall
            self.dWall = dWall
            self.x = x
            self.y = y
            if x == len(self.grid) - 1:
                self.rWall = True
            if x == 0:
                self.lWall = True
            if y == len(self.grid) - 1:
                self.dWall = True
            if y == 0:
                self.uWall = True
    def checkForRegions(self):
        for cell in self.grid:
            if cell == ".":
                return False
        return True
    

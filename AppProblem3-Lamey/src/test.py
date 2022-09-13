from grid import Grid
from column import Column
from stone import Stone
from enum import Enum


height = 7
grid = Grid(height=height)
connected = False

while True:
    print(grid)
    print(f"Status: {connected}")
    col = int(input("What col? "))
    if col == 'q':
        exit(0)
    try:
        connected = grid.drop("Red", col)
    except Exception:
        print("There aren't that many columns")

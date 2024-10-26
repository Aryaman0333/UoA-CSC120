"""
    File: word_grid.py
    Author: Aryaman Mehra
    Course: CSC 120, Spring 2024
    Purpose: To create a grid of size N*N of randomly generated lower-case letters.
"""

import random


def init():
    """
    This function takes the grid size as input from the user.
  
    Parameters: None.
  
    Returns: Grid size.
    """
    grid_size=int(input())
    seed_value=input()
    random.seed(seed_value)
    return grid_size

def make_grid(grid_size):
    """
    This function generates random letters for the grid.
  
    Parameters:
      grid_size: contains the size for the grid.
  
    Returns: A 2D list as a grid.
    """
    grid=[]
    for i in range(grid_size):
        r=[]
        for j in range(grid_size):
            r.append(chr(random.randint(97,122)))
        grid.append(r)
    return grid

def print_grid(grid):
    """
    This function prints the grid.
  
    Parameters: 
      grid: It is the list of letters which needs to be printed as a grid.
  
    """
    for i in grid:
        print(",".join(i))
    
def main():
    """
    This function calls every function.
    """
    grid_size=init()
    grid=make_grid(grid_size)
    print_grid(grid)

main()





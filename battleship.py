"""
    File: battleship.py
    Author: Aryaman Mehra
    Course: CSc120, Spring 2024
    Purpose: This program simulates the game of Battleship. It reads 
             ship placements and guesses from input files, evaluates 
             the guesses, and determines when all ships have been sunk.
"""

import sys

class GridPos:
    """Represents a position on the game grid."""

    def __init__(self, x, y, ship):
        """
        Initializes a GridPos object.

        Parameters:
            x: The x-coordinate of the position.
            y: The y-coordinate of the position.
            ship: The ship object occupying the position, if any.
        """
        self._x_cord = x
        self._y_cord = y
        self._ship_obj = ship
        self._prev_guess = False

    def __str__(self):
        if self._ship_obj == None:
            return "None"
        return self._ship_obj._kind + " at (" + self._x_cord + ","\
            + self._y_cord + ")"
    
class Board:
    """Represents the game board."""

    def __init__(self, grid, ships):
        """Initializes a Board object.

        Parameters:
            grid : A 2D list representing the grid of positions.
            ships : A list of Ship objects on the board.
        """
        self._grid = grid
        self._ships =ships
 
    def guess(self, x, y):
        """Processes a guess at the specified position.
        
        Parameters:
            x : The x-coordinate of the guessed position.
            y : The y-coordinate of the guessed position.

        Prints:
            Analyzes the guess and prints message accordingly.
        """
        if x<0 or x>9 or y>9 or y<0:
            print("illegal guess")
        else:
            position = self._grid[x][y]
            if position._ship_obj == None:
                if position._prev_guess:
                    print("miss (again)")
                else:
                    print("miss")
                    position._prev_guess = True
            else:
                if position._prev_guess:
                    print("hit (again)")
                else:
                    position._ship_obj._unhit -= 1
                    if position._ship_obj._unhit == 0:
                        print("{} sunk".format(position._ship_obj._kind))
                    else: 
                        print("hit")
                    position._prev_guess = True

    def __str__(self):
        return "grid:" + self._grid + " list of ship objects:" + self._ships
    
class Ship:
    """Represents a ship on the game board."""

    def __init__(self, line):
        """Initializes a Ship object.

        Parameters:
            line : A line containing the ship's properties.
                
        """
        self._line= line
        self._position = []
        self._kind = line[0]
        self._x1 = int(line[1])
        self._y1 = int(line[2])
        self._x2 = int(line[3])
        self._y2 = int(line[4])
        self._unhit = self._size = self.find_size()
        self.gridpos()
        self.is_move_valid()

    def find_size(self):
        """Calculates the size of the ship.

        Parameters: 
            None
        
        Returns:
            The size of the ship.
        """

        if (self._x1 != self._x2) and (self._y1 != self._y2):
            print("ERROR: ship not horizontal or vertical: " +\
                   " ".join(self._line))
            sys.exit(0)

        if self._x1 == self._x2:
            return abs(self._y1 - self._y2) + 1
        else:
            return abs(self._x1 - self._x2) + 1
        
    
    def gridpos(self):
        """Calculates the positions occupied by the ship.

        Parameters:
            None

        Returns:
            Nothing
        """
        if (self._x1 != self._x2) and (self._y1 != self._y2):
            print("ERROR: ship not horizontal or vertical: " + \
                  " ".join(self._line))
            sys.exit(0)

        if self._x1 == self._x2:
            for i in range(self._size):
                if self._y1 < self._y2:
                    self._position.append((self._x1,self._y1 + i))
                else:
                    self._position.append((self._x2, self._y2 + i))

        else:
            for i in range(self._size):
                if self._x1 < self._x2:
                    self._position.append((self._x1 + i,self._y1))
                else:
                    self._position.append((self._x2 + i, self._y2))
    
            
    def is_move_valid(self):
        """Checks if the ship's properties are valid.
        
        Parameters: None
        
        Prints:
            Prints a message with the line if move is invalid.
        """
        if (self._kind == 'A' and self._size != 5) \
            or (self._kind == 'B' and self._size != 4) \
            or (self._kind == 'S' and self._size != 3) \
            or (self._kind == 'D' and self._size != 3) \
            or (self._kind == 'P' and self._size != 2):
            print( "ERROR: incorrect ship size: " + " ".join(self._line))
            sys.exit(0)

def read(placement):
    """Reads ship placements from a file.

    Parameters:
        placement : The file containing ship placements.

    Returns:
        A list of Ship objects representing the placed ships.
    """
    list_ships = []
    for data in placement:
        data = data.split()
        ship = Ship(data)
        for number in data[1:5]:
            if int(number) < 0 or int(number) > 9:
                print("ERROR: ship out-of-bounds: " + " ".join(ship._line))
                sys.exit(0)
        if ship not in list_ships:
            list_ships.append(ship)
        elif ship in list_ships:
            print("ERROR: fleet composition incorrect")
            sys.exit(0)

    if len(list_ships) != 5:
        print("ERROR: fleet composition incorrect")
        sys.exit(0)

    return list_ships


def make_grid(list_ships):
    """Creates a grid representation of the game board.

    Parameters:
        list_ships : A list of Ship objects.

    Returns:
        A 2D list representing the grid
    """
    grid = []
    for i in range(10):
        col = []
        for j in range(10):
            data_pos = None
            for ship in list_ships:
                if (i, j) in ship._position:
                    if data_pos is not None:
                        print("ERROR: overlapping ship: " + \
                              " ".join(ship._line))
                        sys.exit(0)
                    data_pos = GridPos(i, j, ship)
            if data_pos is None:
                data_pos = GridPos(i, j, None)
            col.append(data_pos)
        grid.append(col)
    return grid

def evaluate_guess(list_ships, guess):
    """Evaluates the guesses made by the player and updates the attributes 
    accordingly.

    Parameters:
        list_ships: A list of Ship objects representing the fleet of ships.
        guess: A file object containing the guesses made by the player.

    Prints:
        A message when all ships have sunk.
    """
    grid = make_grid(list_ships)
    board = Board(grid, list_ships)  
    for data in guess:
        data = data.split()
        board.guess(int(data[0]),int(data[1]))
        ships_alive = 0
        for ship in list_ships:
            if ship._unhit != 0:
                ships_alive += 1
        if ships_alive == 0:
            print("all ships sunk: game over")
            sys.exit(0)

def main():
    """Main function to execute the Battleship game by calling 
    other functions accordingly."""

    placement_file = input()
    guess_file = input()
    placements = open(placement_file, "r")
    guesses = open(guess_file, "r")
    list_ships = read(placements)
    evaluate_guess(list_ships, guesses)
    placements.close()
    guesses.close()

main()
    


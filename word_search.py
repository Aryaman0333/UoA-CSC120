"""
    File: word_search.py
    Author: Aryaman Mehra
    Course: CSC 120, Spring 2024
    Purpose:The purpose of this program is to create a game called word search.
            It searches words in a random grid horizontally and vertically from both sides,
            and also diagonally from upper-left to lower-right.
"""
def get_word_list():
    """
    This function reads the file and makes a list of the words.
  
    Returns: A list of words.
    """
    file = input()
    f=open(file, 'r')
    words = []
    for i in f:
        words.append(i.strip().lower())
    return words


def read_letters_file():
    """
    This function reads the file and makes a grid.  
    
    Returns: A grid of letters in the form of 2D list.
    """
    file = input()
    f=open(file, 'r')
    letters = []
    for i in f:
        letters.append(i.split())
    return letters


def occurs_in(substr,word_list):
    """
    Checks if the substring is in the list of words or not.
  
    Parameters: 
        substr: contains the substring to be checked.
        word_list: it is the list of valid words.
  
    Returns: True or False.
    """
    return substr in word_list
        

def in_horizontal(letters_grid, word_list):
    """
    Checks the grid horizonatally from both sides for legal words.
  
    Parameters: 
        letters_grid: it is the grid of letters.
        word_list: it is the list of all legal words.
  
    Returns: The legal words found in the grid.
    """
    w = []
    #To check words from left to right.
    for row in range(len(letters_grid)):
        for column in range(len(letters_grid[row])):
            for stop in range(3, len(letters_grid[row]) - column + 1):
                substr = "".join(letters_grid[row][column:column + stop]).lower()
                if occurs_in(substr, word_list):
                    w.append(substr)

    #To check words from right to left.
    for row in range(len(letters_grid)):
        reverse = letters_grid[row][::-1]
        for column in range(len(reverse)):
            for stop in range(3, len(letters_grid[row]) - column + 1):
                substr = "".join(reverse[column:column + stop]).lower()
                if occurs_in(substr, word_list):
                    w.append(substr)

    return w

def in_vertical(letters_grid, word_list):
    """
    Checks the grid vertically from both sides for legal words.
  
    Parameters: 
        letters_grid: it is the grid of letters.
        word_list: it is the list of all legal words.
  
    Returns: The legal words found in the grid.
    """
    w = []
    #To check words from top to bottom.
    for column in range(len(letters_grid)):   # iterates over each column
        for s in range(len(letters_grid[column][0])):   # takes first row
            c = [row[column] for row in letters_grid]   # all column values
            for start in range(len(c)):   # starting position 
                length = 3
                while length <= len(c) - start:
                    substr = ''.join(c[start:start + length]).lower()
                    if occurs_in(substr, word_list):
                        w.append(substr)
                    length += 1

    #To check words from bottom to top.
    for column in range(len(letters_grid)):   # iterates over each column
        for s in range(len(letters_grid[column][0])):   # takes first row
            reverse = [row[column] for row in letters_grid][::-1]    # all column values
            for start in range(len(reverse)):   # starting position 
                length = 3
                while length <= len(reverse) - start:
                    substr = ''.join(reverse[start:start + length]).lower()
                    if occurs_in(substr, word_list):
                        w.append(substr)
                    length += 1

    return w


def in_diagonal(letters_grid, word_list):
    """
    Checks the grid diagonally from top left to bottom right.
  
    Parameters: 
        letters_grid: it is the grid of letters.
        word_list: it is the list of all legal words.
  
    Returns: The legal words found in the grid.
    """
    w=[]

    for row in range(len(letters_grid)):   # through every row
        for column in range(len(letters_grid[0])):   # through every column
            for length in range(3,min(len(letters_grid)-row,len(letters_grid[0])-column)+1):   
            # check for words diagonally with min length 3
                    word = [letters_grid[row + a][column + a] for a in range(length)]   # extracts the word
                    substr=''.join(word)
                    if occurs_in(substr,word_list):   # checks for valid word
                        w.append(substr)
    
    return w
    


def prints(words):
    """
    Prints all the words that were founf in the grid.
  
    Parameters: 
        words: List of all the legal words found in the grid.
  
    Returns: The legal words found in the grid.
    """
    for i in words:
        print(i)


def main():
    """
    This function calls all the other functions.
    """
    word_list = get_word_list()
    letters_grid = read_letters_file() 
    # a list used to accumulate the valid words found
    all_words = []    
    all_words.extend(in_horizontal(letters_grid, word_list))
    all_words.extend(in_vertical(letters_grid, word_list))
    all_words.extend(in_diagonal(letters_grid, word_list))

    all_words.sort()
    prints(all_words)

main()
"""
File: huffman.py
Author: Aryaman Mehra
Course: CSc120, Spring 2024
Purpose: This program implements a binary tree decoder. It constructs 
a binary tree from pre-order and in-order traversals and then decodes 
a given binary sequence using the constructed tree, and also returns 
post-order traversal.
"""

class Tree:
    """Represents a binary tree node."""
    def __init__(self, value):
        """Initializes a Tree object with a given value."""
        self._value = value
        self._right  = None
        self._left = None

    def get_left(self):
        return self._left
    
    def get_right(self):
        return self._right
    
    def get_value(self):
        return self._value
    
    def set_left(self, left):
        self._left = left

    def set_right(self, right):
        self._right = right

    def set_value(self, value):
        self._value = value

def tree_construction(  PreOrd, InOrd):
    """Constructs a binary tree from pre-order and in-order traversals.
    
    Parameters:
        PreOrd: A list representing the pre-order traversal of the binary tree.
        InOrd: A list representing the in-order traversal of the binary tree.
    
    Returns:
        A Tree object representing the root of the constructed binary tree.
    """

    if len(PreOrd) == 0 or len(InOrd) == 0:
        return None
    root_value = PreOrd[0]
    tree = Tree(root_value)
    root_index = InOrd.index(root_value)
    tree.set_left(tree_construction(PreOrd[1:root_index + 1],\
                                     InOrd[:root_index]))
    tree.set_right(tree_construction(PreOrd[root_index + 1:],\
                                      InOrd[root_index + 1:]))
    return tree

    
def decoding_sequence(original_tree, tree, string):
    """Decodes a binary sequence using a binary tree.
    
    Parameters:
        original_tree: The original binary tree used for decoding.
        tree: The current subtree being examined.
        string: The binary sequence to decode.
    
    Returns:
        Leaf node according to the sequence.
    """

    if len(string) == 0:
        if tree.get_left() == None and tree.get_right() == None:
            return str(tree.get_value())
        else:
            return ''
    elif string[0] == '0':
        if tree.get_left() == None and tree.get_right() == None:
            return str(tree.get_value()) + \
                decoding_sequence(original_tree, original_tree, string)
        elif tree.get_left() != None:
            return decoding_sequence(original_tree, \
                                     tree.get_left(), string[1:])
        else:
            return decoding_sequence(original_tree, \
                                     original_tree, string[1:])
    else:
        if tree.get_right() == None and tree.get_left() == None:
            return str(tree.get_value()) + \
                decoding_sequence(original_tree, original_tree, string)
        elif tree.get_right() != None:
            return decoding_sequence(original_tree, tree.get_right(),\
                                     string[1:])
        else:
            return decoding_sequence(original_tree, original_tree, \
                                     string[1:])
        
def PostOrder(tree):
    """Performs post-order traversal on a binary tree.
    
    Parameters:
        tree: The root of the binary tree.
    
    Returns:
        A string representing the post-order traversal of the binary tree.
    """
    if tree == None:
        return ''
    return PostOrder(tree.get_left()) + PostOrder(tree.get_right())\
          + str(tree.get_value()) + ' '

def main():
    """Main function to execute the binary tree decoder."""
    file = open(input('Input file: '))
    PreOrd = file.readline().split()
    InOrd = file.readline().split()
    tree = tree_construction( PreOrd, InOrd)
    sequence = file.readline().strip()
    print(PostOrder(tree))
    print(decoding_sequence(tree, tree, sequence).strip())

main()
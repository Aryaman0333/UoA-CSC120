"""
    File: linkedlist_sort.py
    Author: Aryaman Mehra
    Course: CSC 120, Spring 2024
    Purpose: This program defines a linked list and provides methods for 
             sorting, adding, removing, and inserting nodes. The main function
             reads numbers from a file, creates a linked list, sorts the list,
             and prints the result.
    """

class LinkedList:
    """
    This class represents a linked list.
    The linked list has methods for sorting nodes, adding a node to the head,
    removing a node from the head, inserting a node after another node, and
    generating a string representation of the list.
    """

    def __init__(self):
        self._head = None
    
    
    def sort(self):
        """
        Sorts the nodes in the linked list in decreasing order.
        
        Parameters: None
        
        Returns: Nothing
        """
        sorted_list=LinkedList()
        while self._head != None:
            curr_element = self.remove()

            # Add at head if sorted is empty or first element is smaller
            if sorted_list._head==None or curr_element.value()>sorted_list._head.value():
                curr_element._next = sorted_list._head
                sorted_list._head = curr_element
            else:
                # E holds the node after which curr_element is added
                E = sorted_list._head
                while E._next!=None and E._next.value()>=curr_element.value():
                    E = E._next
                curr_element._next = E._next
                E._next = curr_element

        self._head = sorted_list._head 
    
    
    # add a node to the head of the list
    def add(self, node):
        node._next = self._head
        self._head = node
        
    # remove a node from the head of the list and return the node
    def remove(self):
        assert self._head != None
        _node = self._head
        self._head = _node._next
        _node._next = None
        return _node
    
    # insert node2 after node1
    def insert(self, node1, node2):
        assert node1 != None
        node2._next = node1._next
        node1._next = node2
    
    def __str__(self):
        string = 'List[ '
        curr_node = self._head
        while curr_node != None:
            string += str(curr_node)
            curr_node = curr_node.next()
        string += ']'
        return string

class Node:
    def __init__(self, value):
        self._value = value
        self._next = None
    
    def __str__(self):
        return str(self._value) + "; "
    
    def value(self):
        return self._value
    
    def next(self):
        return self._next
    
def main():
    """
    This is the main function that reads numbers from a file, creates a linked 
    list, sorts the list, and prints the sorted list.

    The function prompts the user for a file name, reads the numbers from the 
    file, adds them to a linked list, sorts the list, and prints the sorted 
    list.

    Parameters: None

    Returns: Nothing
    """
    file_name=input()
    file=open(file_name,"r")
    to_be_sorted=LinkedList()
    for line in file:
        numbers_list=line.strip().split()
        for number in numbers_list:
            to_be_sorted.add(Node(int(number)))
    to_be_sorted.sort()
    print(to_be_sorted)
    file.close()

main()
        
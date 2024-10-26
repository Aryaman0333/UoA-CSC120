"""
File: fake_news.py
Author: Aryaman Mehra
Course: CSC 200, Spring 2024
Purpose: This program analyzes a CSV file containing news articles
         and calculates the frequency of occurrence of different words. 
         It find the nth highest count word. Then sorts the words based
         on their frequency and prints out the top words. 
"""

import csv
import string

class Node:
    """Represents a node in a linked list."""

    def __init__(self, word):
        """Initializes a Node with a word and sets its count to 1
           and _next to None."""
        self._word=word
        self._count=1
        self._next=None

    def word(self):
        return self._word
    
    def count(self):
        return self._count
    
    def next(self):
        return self._next
    
    def set_next(self, target):
        """
        Sets the next node.
        Parameters: 
            target: new value of _next attribute.
        Returns:
            Nothing.
        """
        self._next=target

    def incr(self):
        """Increments the count of the word stored in the node."""
        self._count+=1

    def __str__(self):
        return "{} : {}".format(self._word, self._count)
    
class LinkedList:
    """Represents a linked list."""

    def __init__(self):
        """Initializes an empty linked list."""
        self._head=None

    def is_empty(self):
        """Checks if the linked list is empty."""
        return self._head==None
    
    def head(self):
        return self._head
    
    def update_count(self, word):
        """
        Updates the count of a word in the linked list.
        Parameter:
            word: The word whose count is to be increased
        Returns: 
            Nothing
        """
        current= self._head
        condition= True
        while current != None:
            if current._word==word:
                current._count+=1
                condition= False
                break
            current=current._next

        if condition:
            word=Node(word)
            word._next = self._head
            self._head=word


    def rm_from_hd(self):
        """Removes and returns the first node from the linked list."""
        if not self.is_empty():
            first = self._head
            self._head = first._next
            first._next = None
            return first
    
    
    def insert_after(self, node1, node2):
        """
        Inserts a node after a given node.
        Parameters:
            node1: reference to an existing node
            node2: reference to a new node
        Returns:
            Nothing
        """
        current= self._head
        while current != node1:
            current = current._next
        node2._next= current._next
        current._next=node2

    def sort(self):
        """
        Sorts the nodes in the linked list in decreasing order.
        
        Parameters: None
        
        Returns: Nothing
        """
        sorted_list=LinkedList()
        while self._head != None:
            curr_element = self.rm_from_hd()

            # Add at head if sorted_list is empty or first element is smaller
            if sorted_list._head == None or \
                curr_element.count() > sorted_list._head.count():
                curr_element._next = sorted_list._head
                sorted_list._head = curr_element
            else:
                # E holds the node after which curr_element is added
                E = sorted_list._head
                while E._next!=None and E._next.count()>=curr_element.count():
                    E = E._next
                curr_element._next = E._next
                E._next = curr_element

        self._head = sorted_list._head 

    def get_nth_highest_count(self, n):
        """
        Returns the node with the nth highest count.
        Parameter:
            n: holds the desired position of the node
        Returns:
            Count of the node at n
        """
        current = self._head
        if current!=None:
            for i in range(int(n)):
                if current._next != None:
                    current = current._next
            return current._count
    
    def print_upto_count(self, n):
        """
        Prints words with counts greater than or equal to n.
        Parameter:
            n: holds the count value
        Prints:
            Words with count greater than or equal to n
        """
        current = self._head
        while current != None:
            if current._count >= n:
                print(current._word + ":" + str(current._count))
            current = current._next

    def __str__(self):
        current = self._head
        output = ""
        while current != None:
            output+= current._word + " "
            current = current._next
        return output
    
def clean(list):
    """
    Cleans a list of words by removing punctuation and whitespace.
    Parameter:
        list: contains a line of the file
    Returns:
        list of cleaned words of the title
    """
    cleaned_list=[]
    words = list[4].lower().split()
    for i in words:
        word = ''
        for letter in i:
            if letter in string.punctuation or letter in string.whitespace:
                if len(word) > 2:
                    cleaned_list.append(word)
                word = ''
            else:
                word += letter
            
        if len(word) > 2:    
            cleaned_list.append(word)
    
    return cleaned_list

def main():
    """Main function to process input file and print results."""
    infilename = input()
    n = input()
    linked_list = LinkedList()
    infile = open(infilename)
    csvreader = csv.reader(infile)
    for itemlist in csvreader: 
        if itemlist[0][0]!="#":
            for word in clean(itemlist):
                linked_list.update_count(word)
    linked_list.sort()
    value = linked_list.get_nth_highest_count(n)
    linked_list.print_upto_count(value)
    infile.close()

main()

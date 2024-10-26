"""
    File: friends.py
    Author: Aryaman Mehra
    Course: CSc 120, Sprin2024
    Purpose: This program reads friendship data from a file, organizes
             it using linked lists, and finds common friends between 
             two given people.
"""

from linked_list import *

def add_friend(lines):
    """
     Add friends from the input lines to the linked list.

    Parameters:
        lines (list): A list of strings representing friendship relationships.

    Returns:
        A linked list containing the names and their friends.
    """
    friends_ll = Linked_List()

    for line in lines:
        line = line.split(" ")
        names = []
        for word in line:
            if word != "":
                names.append(word)
            names.sort()

        if names != []:
            friend1 = Node(names[0])
            friend2 = Node(names[1])

            friends_ll.add_person(friend1)
            friends_ll.add_person(friend2)

            friends_ll.add_friend(friend1, friend2)
            friends_ll.add_friend(friend2, friend1)
    
    friends_ll.sort()
    return friends_ll

def common_friends(friends_ll, name1, name2):
    """Find common friends between two given names.

    Parameters:
        friends_ll (LinkedList): The linked list containing 
        the names and their friends.
        name1 (str): The node of the first person.
        name2 (str): The node of the second person.
    """

    if not friends_ll.name_in_list(name1):
        print("ERROR: Unknown person " + name1)
    elif not friends_ll.name_in_list(name2):
        print("ERROR: Unknown person " + name2)
    else:
        friend_list = friends_ll.common_friends(name1, name2)
        
        if friend_list.head() is None:
            print('')
        else:
            print("Friends in common:")
            current = friend_list.head()
            while current is not None:
                print(current.get_name())
                current = current.get_next()

def main():
    """Main function to execute the program."""
    filename = input("Input file: ")
    file = open(filename)
    lines = file.read().split("\n")
    friends_ll = add_friend(lines)
    name1 = input("Name 1: ")
    name2 = input("Name 2: ")
    common_friends(friends_ll, name1, name2)
    file.close()

main()

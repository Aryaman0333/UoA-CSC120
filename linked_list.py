"""
    File: linked_list.py
    Author: Aryaman Mehra
    Course: CSc 120, Spring 2024
    Purpose: Implements LinkedList and Node classes for managing a 
             linked list of friends' names and their relationships. 
"""

class Node:
    """Represents a node in a linked list.
    
    Attributes:
        _name (str): The name stored in the node.
        _friends (Node): The linked list of friends for the current node.
        _next (Node): The reference to the next node in the linked list.
    """

    def __init__(self,name):
        """Initializes a node with the given name.

        Parameters:
            name (str): The name to be stored in the node.
        """
        self._name = name
        self._friends = None
        self._next = None

    def get_name(self):
        """Returns the name stored in the node.

        Returns:
            The name stored in the node.
        """
        return self._name
    
    def get_friends(self):
        """Returns the linked list of friends for the current node.

        Returns:
            The linked list of friends for the current node.
        """
        return self._friends
    
    def get_next(self):
        """Returns the reference to the next node in the linked list.

        Returns:
            The reference to the next node in the linked list.
        """
        return self._next
    
    def __str__(self):
        """Returns a string representation of the node.

        Returns:
            A string representation of the node.
        """
        return "Name: " + self._name + ", Friends: " + \
            str(self._friends)+ ", Next: "+ str(self._next) + "; "
    
class Linked_List:
    """Represents a linked list data structure. It implements methods 
    for adding nodes, finding common friends, sorting nodes, and more.
    """

    def __init__(self):
        """Initializes an empty linked list."""
        self._head=None

    def head(self):
        """Returns the head of the linked list.

        Returns:
            The head of the linked list.
        """
        return self._head
    
    def name_in_list(self, name):
        """Checks if a given name exists in the linked list.

        Parameters:
            name (str): The name to search for in the linked list.

        Returns:
            True if the name exists in the linked list, False otherwise.
        """
        current = self.head()
        while current != None:
            if current.get_name() == name:
                return True
            current = current.get_next()
        return False
    
    def add_person(self, node):
        """Adds a person to the linked list if it doesn't already exist.

        Parameters:
            node (Node): The node representing the person to be added.
        """
        if not self.name_in_list(node.get_name()):
            node._next = self.head()
            self._head = node

    def add_friend(self, node, friend_node):
        """Adds a friend to a person's linked list of friends.

        Parameters:
            node (Node): The node representing the person.
            friend_node (Node): The node representing the friend to be added.
        """

        new_node = Node(friend_node.get_name())
        current = self.head()
        while current != None:
            if current.get_name() == node.get_name():
                break
            current = current._next
        new_node._next = current.get_friends()
        current._friends = new_node

    def find_friends(self, name):
        """Finds the linked list of friends for a given name.

        Parameters:
            name (str): The name of the person whose friends are to be found.

        Returns:
            The linked list of friends for the given person.
        """
        current = self.head()
        while current != None:
            if current.get_name() == name:
                break
            current = current._next
        return current.get_friends()
    
    def common_friends(self, name1, name2):
        """Finds the common friends between two persons.

        Parameters:
            name1 (str): The name of the first person.
            name2 (str): The name of the second person.

        Returns:
            A Linked_List of common friends between the two persons.
        """
        common_list = Linked_List()
        self.sort()
        friends1 = self.find_friends(name1)
        friends2 = self.find_friends(name2)

        while friends1 is not None:
            current_friend2 = friends2
            while current_friend2 is not None:
                if friends1.get_name() == current_friend2.get_name():
                    common_list.add_person(Node(friends1.get_name()))
                    break
                current_friend2 = current_friend2.get_next()
        
            friends1 = friends1.get_next()
    
        common_list.sort()
        return common_list
    
    def sort(self):
        """
        source : PA-long 5
        Sorts the nodes in the linked list in ascending order.
        
        Parameters: None
        
        Returns: Nothing
        """
        sorted_list = Linked_List()
        while self._head is not None:
            curr_element = self.remove()

            # Add at head if sorted is empty or first element is greater
            if sorted_list._head is None or curr_element.get_name() < sorted_list._head.get_name():
                curr_element._next = sorted_list._head
                sorted_list._head = curr_element
            else:
                # E holds the node after which curr_element is added
                E = sorted_list._head
                while E._next is not None and E._next.get_name() < curr_element.get_name():
                    E = E._next
                curr_element._next = E._next
                E._next = curr_element

        self._head = sorted_list._head
    
    
    # add a node to the head of the list
    def add(self, node):
        """source : PA-long 5
        Adds a node to the head of the linked list.

        Parameters:
            node (Node): The node to be added.
        """
        node._next = self._head
        self._head = node
        
    # remove a node from the head of the list and return the node
    def remove(self):
        """source : PA-long 5
        Removes a node from the head of the linked list and returns it.

        Returns:
            The removed node.
        """
        assert self._head != None
        _node = self._head
        self._head = _node._next
        _node._next = None
        return _node
    
    def __str__(self):
        """Returns a string representation of the linked list.

        Returns:
            A string representation of the linked list.
        """
        string = 'List[ '
        curr_node = self._head
        while curr_node is not None:
            string += str(curr_node.get_name()) + ">"
            curr_node = curr_node._next
        string += ']'
        return string
    

    

    

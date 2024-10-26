"""
File: writer_bot_ht.py
Author: Aryaman Mehra
Course: CSc120, Spring 2024
Purpose: This program generates random text using a Markov chain algorithm
         implemented with a hash table ADT. It reads data from a file, 
         constructs a Markov dictionary based on a specified prefix length,
         and then generates a sequence of words based on the Markov chain. 
         The generated text is printed.
"""

import random
import sys

SEED = 8
NONWORD = "@"

class Hashtable:
    """Hash table ADT using linear probing to handle collisions."""

    def __init__(self, size):
        """
        Initialize the hash table with a specified size.
        
        Parameters: 
            size: The size of the hash table.

        Returns:
            None
        """
        self._pairs = [None] * size
        self._size = size

    def hash(self, key):
        """
        It hashes a string key to an integer.

        Parameters:
            key: The key to be hashed.

        Returns:
            The hashed value of the key.
        """
        p = 0
        for char in key:
            p = 31 * p + ord(char)
        return p % self._size

    def put(self, key, value):
        """
        Insert a key/value pair into the hash table.

        Parameters:
            key: The key to be inserted.
            value: The value corresponding to the key.

        Returns:
            None
        """
        index = self.hash(key)
        if self._pairs[index] is None:
            self._pairs[index] = [key, value]
        else:
            index -= 1
            while self._pairs[index] is not None:
                index = (index - 1) % len(self._pairs)
            self._pairs[index] = [key, value]

    def get(self, key):
        """
        Look up a key in the hash table and return its value.

        Parameters:
            key: The key to search.

        Returns:
            The value associated with the key, or None if key not found.
        """
        index = self.hash(key)
        if self._pairs[index] is None:
            return None
        elif self._pairs[index][0] == key:
            return self._pairs[index][1]
        index = (index - 1) % len(self._pairs)
        while self._pairs[index] is not None and index != self.hash(key):
            if self._pairs[index][0] == key:
                return self._pairs[index][1]
            index = (index - 1) % len(self._pairs)
        return None

    def __contains__(self, key):
        """
        Check if a key is contained in the hash table.

        Parameters:
            key: The key to check for existence.

        Returns:
             True if key is found, False otherwise.
        """
        if self.get(key) == None:
            return False
        return True 

    def __str__(self):
        """Return a string representation of the hash table."""
        return str(self._pairs)
    

def add_to_hash_table(markov_chain, prefix_size, num_words):
    """
    Generate random text based on the Markov chain.

    Parameters:
        markov_chain: Hashtable representing the Markov chain.
        prefix_size: Size of the prefix.
        num_words: Number of words to generate.

    Returns:
        List of generated words.
    """
    random.seed(SEED)
    generated_text = []
    prefix = [NONWORD] * prefix_size

    for m in range(num_words):
        prefix_key = " ".join(prefix)
        if prefix_key in markov_chain:
            suffixes = markov_chain.get(prefix_key)
            if len(suffixes) > 1:
                chosen_suffix = random.randint(0, len(suffixes) - 1)
                generated_text.append(suffixes[chosen_suffix])
            else:
                generated_text.append(suffixes[0])

            prefix = prefix[1:]
            prefix.append(generated_text[-1])
        else:
            break

    return generated_text

def generate_markov_list(text, prefix_size, table_size):
    """
    Construct a Markov chain from the input text.

    Parameters:
        text: Input text.
        prefix_size: Size of the prefix.
        table_size: Size of the hash table.

    Returns:
        Hashtable representing the Markov chain.
    """
    markov_chain = Hashtable(table_size)
    words = text.split()
    prefix = [NONWORD] * prefix_size

    for word in words:
        prefix_key = " ".join(prefix)
        if prefix_key not in markov_chain:
            markov_chain.put(prefix_key, [])

        markov_chain.get(prefix_key).append(word)

        prefix = prefix[1:]
        prefix.append(word)

    return markov_chain

def main():
    """
    Main function to execute the Markov chain text generator.
    """
    filename = input()
    table_size = int(input())
    prefix_size = int(input())
    num_words = int(input())

    if prefix_size < 1:
        print("ERROR: specified prefix size is less than one")
        sys.exit(0)

    if num_words < 1:
        print("ERROR: specified size of the generated text is less than one")
        sys.exit(0)

    file = open(filename, 'r') 
    text = file.read()

    markov_chain = generate_markov_list(text, prefix_size, table_size)

    generated_text = add_to_hash_table(markov_chain, prefix_size, num_words)

    for i in range(0, len(generated_text), 10):
        print(" ".join(generated_text[i:i+10]))
    
    file.close()


main()
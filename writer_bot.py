"""
File: markov_text_generator.py
Author: Aryaman Mehra
Course: CSc120, Spring 2024
Purpose: This program generates text using a Markov chain 
algorithm. It reads data from a file, constructs a Markov 
dictionary based on a specified prefix length, and then 
generates a sequence of words based on the Markov chain. 
The generated text is printed to the console.
"""
import random

SEED = 8
NONWORD = " "
     
def create_tuple(word, n):
    """Creates a tuple of length n with each element as word.
    
    Parameters:
        word (str): The word to be repeated in the tuple.
        n (int): The length of the tuple.
    
    Returns:
        tuple: A tuple containing n copies of the word.
    """
    tup = []
    for i in range(n):
        tup.append(word)
    return tuple(tup)

def shift_tuple(tup, value):
    """Shifts the elements of a tuple and appends a new value at the end.
    
    Parameters:
        tup (tuple): The tuple to be shifted.
        value: The new value to be appended.
    
    Returns:
        tuple: The shifted tuple with the new value appended.
    """
    t = tup[1:]
    t = t + (value,)
    return t

def make_prefix(text, prefix):
    """Creates a prefix tuple from the beginning of the text.
    
    Parameters:
        text (list): The list of words.
        prefix (int): The length of the prefix tuple.
    
    Returns:
        tuple: A tuple containing the first prefix elements of the text.
    """
    temp = []
    for items in text[:prefix]:
        temp.append(items)
    temp = tuple(temp)
    return temp

def read(file_name):
    """Reads data from a file and returns it as a list of words.
    
    Parameters:
        file_name (str): The name of the file to read from.
    
    Returns:
        list: A list containing all the words read from the file.
    """
    data = []
    file = open(file_name)
    for i in file:
        i = i.strip().split()
        data += i
    return data

def create_dict(data, prefix):
    """Creates a Markov dictionary from the given data and prefix length.
    
    Parameters:
        data (list): The list of words.
        prefix (int): The length of the prefix tuple.
    
    Returns:
        dict: A dictionary representing the Markov chain.
    """   
    word_dict = {}
    key = create_tuple(NONWORD, prefix)
    for word in range(len(data)):
        if key in word_dict:
            word_dict[key].append(data[word])
        else:
            word_dict[key] = [data[word]]
        key = shift_tuple(key, data[word])
    return word_dict

def prints(file_data, n, no_words, dic):
    """Prints the generated text.
    
    Parameters:
        file_data (list): The list of words.
        n (int): The length of the prefix tuple.
        no_words (int): The number of words to generate.
        dic (dict): The Markov dictionary.

    Prints:
       Generated text.
    """
    word = ''
    words = []
    counter = no_words
    for i in file_data[:n]:
        words.append(i)

    prefix = make_prefix(file_data, n)

    text = 0
    while text <= no_words:
        if prefix in dic:
            if len(dic[prefix]) > 1:
                word = dic[prefix][random.randint(0, len(dic[prefix]) - 1)]
            else:
                word = dic[prefix][0]
        words.append(word)
        prefix = shift_tuple(prefix, word)
        text += 1

    for i in range(0, no_words, 10):
        if counter >= 10:
            print(' '.join(words[i: i + 10]))
        else:
            print(' '.join(words[i: i + counter]))
        counter -= 10

def main():
    """Main function to execute the Markov chain text generator."""
    random.seed(SEED)
    sfile = input()
    n = int(input())
    no_words = int(input())

    file_data = read(sfile)
    markov_algo = create_dict(file_data, n)

    prints(file_data, n, no_words, markov_algo)

main()
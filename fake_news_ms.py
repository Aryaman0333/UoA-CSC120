import csv
import string

class Word:
    """
    Word
    An object of this class represents information about a word.
    _word: the word string.
    _count: a count of the number of occurrences of the word.
    """
    def __init__(self, word):
        """
        __init__
        initializes the object's attributes as follows: 
        _word is set to word; _count is set to 1.

        Parameters:
            self - object itself
            word - given word

        Returns: None
        """
        self._word = word
        self._count = 1

    def word(self):
        return self._word

    def count(self):
        return self._count

    def incr(self):
        self._count += 1

    def __lt__(self, other):
        return (self.count() > other.count()) or \
               (self.count() == other.count() and \
                self.word() < other.word())

    def __str__(self):
        return self._word + " " + str(self._count)

def file_formatter(data):
    '''
    file_formatter
    creates a list of words, formats
    a the data of the file as required

    Parameters:
        file: data from file

    Returns:
        list_words: list of words
    '''
    list_words = []
    str = ""
    for item in data:
        if item[0][0] != "#":
            str += " "
            for char in item[4]:
                if char not in string.punctuation:
                    str += char
                else:
                    str += " "
    list_words = str.lower().split(" ")
    for element in list_words[:]:
        if len(element) < 3:
            list_words.remove(element)
    return list_words

def add_words(list_words):
    """
    add_words
    function responsible for adding words
    increments the count whenever word repeated

    Parameters:
        list_words - list of words passed

    Returns:
        list - new list formed
    """
    list = []
    for word in list_words:
        found = False
        for i in list:
            if word == i.word():
                i.incr()
                found = True
        if not found:
            list.append(Word(word))
    return list

def print_upto(L, N):
    """
    print_upto
    function responsible for finding words
    with count of N

    Parameters:
        L - List
        N - number

    Returns: None
    """
    N_count = L[N].count()
    for item in L:
        if item.count() >= N_count:
            print ("{} : {:d}".format(item.word(), item.count()))
        else:
            break

def merge_sort(L):
    """
    merge_sort implementation of the list

    Parameters:
        L - List passed to sort

    Returns: 
        Sorted List
    """
    if len(L) <= 1:
        return L
    else:
        mid = len(L) // 2
        L1 = L[:mid]
        L2 = L[mid:]
        sortedL1 = merge_sort(L1)
        sortedL2 = merge_sort(L2)
        return merge(sortedL1, sortedL2)

def merge(L1, L2):
    """
    Helper function for merge_sort
    Merges on basis of count and alphabets

    Parameters:
        L1 - List passed to sort
        L2 - List passed to sort
    Returns: 
        Sorted List
    """
    if not L1:
        return L2
    if not L2:
        return L1
    
    if L1[0].count() > L2[0].count():
        return [L1[0]] + merge(L1[1:], L2)
    elif L1[0].count() < L2[0].count():
        return [L2[0]] + merge(L1, L2[1:])
    else:
        if L1[0].word() < L2[0].word():
            return [L1[0]] + merge(L1[1:], L2)
        else:
            return [L2[0]] + merge(L1, L2[1:])

def main():
    filename = open(input("File: "))
    N = int(input("N: "))
    data = csv.reader(filename)
    list_words = file_formatter(data)
    list2_words = add_words(list_words)
    print_upto(merge_sort(list2_words), N)

main()

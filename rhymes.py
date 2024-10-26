"""
    File: rhymes.py
    Author: Aryaman Mehra
    Course: CSC 120, Spring 2024
    Purpose: The user inputs a word, and the program finds rhymes from
             a dictionary of words and their pronunciations, by comparing
             the word's phonemes and principal stress.
    """

def check(pfile,word):
    """
    Checks the rhyming words of 'word' in 'pfile'.
    Parameters: pfile- It is the dictionary containg all the words
                       and their pronounciation.
                word- It is the word whose rhyming words need to be found.
    Returns: A list of all the rhyming words.
    """
    rhyming=[]
    phoneme={}
    #dictionary of the word's principal stress and phonemes
    #first loop iterates through alternate pronounciations
    for a in pfile[word]:
        #iterates through the list containing pronounciation
        for z in range(len(a)):
            #finds the primary stress
            if a[z][-1]=='1':
                if a[z] not in phoneme:
                    phoneme[a[z]]=[[a[z-1],a[(z+1):]]]
                else:
                    phoneme[a[z]].append([a[z-1],a[(z+1):]])
   #compares the principal stress and phenomes 
    for i,j in pfile.items():
        for b in j:
            #iterates through the list containing pronounciation
            for x in range(len(b)):
                #finds the primary stress and checks all conditions
                if b[x][-1]=='1':
                    if b[x] in phoneme:
                        for o in phoneme[b[x]]:
                            if o[0]!=b[x-1] and o[1]==b[(x+1):]:
                               rhyming.append(i)
    return rhyming


def main():
    """
    Takes input values from the user and calls other functions.
    Prints: All the rhyming words found in the file.
    """
    rhymes_dict={}
    pfile=input()
    line= open(pfile,'r')
    for i in line:
        temp= i.strip().split()
        if temp[0] in rhymes_dict:
            rhymes_dict[temp[0]].append(temp[1:])
        else:
            rhymes_dict[temp[0]]= [temp[1:]]
    line.close()
    word=input()
    if word!="":
        t=check(rhymes_dict,word.upper())
        for a in sorted(t):
            print(a)

main()

"""
    File: pokemon.py
    Author: Aryaman Mehra
    Course: CSC 120, Spring 2024
    Purpose: This program analyzes a Pokemon file that includes details about
             Pokemon types and their attributes. It computes the average
             values for each type's attributes and subsequently addresses a
             series of queries regarding Pokemon properties. The responses
             involve printing the Pokemon type(s) with the highest average
             value for a given attribute.
"""

def  process_input(file):
    """
    This function reads the data file and prepares a 2D dictionary with
    pokemon types as key of the outer dictionary, names as the key of the
    inner dictionary and their attributes as the values.
  
    Parameters: 
        file: It is the data file containing all information about pokemons.
  
    Returns:
         A 2D dictionary of pokemons and their attributes.
    """
    dict={}
    read=open(file,'r')
    for line in read:
        if line[0]!='#':
            temp=line.strip().split(',')
            name= temp[1]
            type=temp[2]
            if temp[2] not in dict:
                dict[type]={}
                dict[type][name]=[]
            else:
                dict[type][name]=[]
            #to slice the attributes from the entire list. 
            for i in temp[4:11]:
                dict[type][name].append(i)
    return dict


def user_query(pokemon):
    """
    This function accepts queries from the user and processes them.
  
    Parameters: 
        pokemon: It is the the 2D list containing pokemon and their types.
  
    Prints:
        It prints the type of pokemon and the max_average, of the corresponding
        query as given by the user.
    """
    query_list=[]
    #takes queries till user enters empty line, and stores them in a list.
    while True:
        query=input()
        if query=="":
            break
        query_list.append(query)
    #checks each query in the list and processes it.
    for q in query_list:
        d={'total':0,'hp':1,'attack':2,'defense':3,'specialattack':4,
           'specialdefense':5,'speed':6}
        if q.lower() in d:
            output=(average(pokemon,d[q.lower()]))
            print_result(output)


def average(pokemon,index):
    """
    This function calculates the average value of a particular attribute
    and returns the maximum average value with the type/types of pokemon.
  
    Parameters: 
        pokemon: It is the the 2D list containing pokemon and their types.
        index: It is the index of the attribute that neds to be evaluated.
  
    Returns:
        A 2D list of type/types of pokemon having the maximum average value
        and the value itself.
    """
    all_average={}
    for type in pokemon:
        sum=0
        c=0
        for name in pokemon[type]:
            #stores sum of attribute value of all pokemons in a type
            sum+=int(pokemon[type][name][index])
            c+=1
        #assigns the average attribute value to the type in a dictionary
        all_average[type]=sum/c
    max_average={}
    output=[]
    #finds the maximum values in all_average
    max_val=max(all_average.values())
    #stores the maximum values and its key in a new dictionary  
    for key, val in all_average.items():
        if val==max_val:
            max_average[key]=val
    #sorts the maximum values in a new list
    for x in sorted(max_average.keys()):
        output.append([x,max_average[x]])
    return output


def print_result(output):
    """
    This function prints the type of pokemon having the maximum average value
    of a particular attribute, with the value itself, in a specific format.
  
    Parameters: 
        output: A 2D list of type/types of pokemon having the maximum average
                value and the value itself.
  
    Prints:
        The type of pokemon having the maximum average value of a particular
        attribute, with the value itself, in a specific format.
    """
    for i in output:
        print("{}: {}".format(i[0], i[1]))   


def main():
    """
    This function takes the data file as input and 
    calls other functions of the program.
    """
    a=input()
    pokemon=process_input(a)
    user_query(pokemon)


main()

# LAB1
# REMINDER: The work in this assignment must be your own original work and must be completed alone

def frequency(txt):
    '''
        >>> frequency('mama')
        {'m': 2, 'a': 2}
        >>> answer = frequency('We ARE Penn State!!!')
        >>> answer
        {'w': 1, 'e': 4, 'a': 2, 'r': 1, 'p': 1, 'n': 2, 's': 1, 't': 2}
        >>> frequency('One who IS being Trained')
        {'o': 2, 'n': 3, 'e': 3, 'w': 1, 'h': 1, 'i': 3, 's': 1, 'b': 1, 'g': 1, 't': 1, 'r': 1, 'a': 1, 'd': 1}
    '''
    # - YOUR CODE STARTS HERE -
    freq_dict = {} #creates the empyt dictionary 
    for char in txt.lower(): #iterates through the characxters in the txt
        if char.isalpha(): #checks if the charcheter is a letter
            if char in freq_dict: #checks if the character is already in the new dictionary
                freq_dict[char] += 1 # if yes then it adds 1 to the current count
            else:
                freq_dict[char] = 1#if not then it adds the character with a value of 1
    return freq_dict
    pass 



def invert(d):
    """
        >>> invert({'one':1, 'two':2,  'three':3, 'four':4})
        {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
        >>> invert({'one':1, 'two':2, 'uno':1, 'dos':2, 'three':3})
        {3: 'three'}
        >>> invert({'123-456-78':'Sara', '987-12-585':'Alex', '258715':'sara', '00000':'Alex'}) 
        {'Sara': '123-456-78', 'sara': '258715'}
    """
    # - YOUR CODE STARTS HERE -
    inverted_dict = {} #creates new dictionary
    for key, value in d.items():#iterates through the key value pairs in original dictionary
        if value not in inverted_dict:#if the value is not in the new dictionary 
            inverted_dict[value] = key #adds it but flips the key value pair
        else:
            if value in inverted_dict:# if value is alreay in dictionary
                del inverted_dict[value] #remove it all together
    return inverted_dict
    pass




def employee_update(d, bonus, year):
    """
        >>> records = {2020:{"John":["Managing Director","Full-time",65000],"Sally":["HR Director","Full-time",60000],"Max":["Sales Associate","Part-time",20000]}, 2021:{"John":["Managing Director","Full-time",70000],"Sally":["HR Director","Full-time",65000],"Max":["Sales Associate","Part-time",25000]}}
        >>> employee_update(records,7500,2022)
        {2020: {'John': ['Managing Director', 'Full-time', 65000], 'Sally': ['HR Director', 'Full-time', 60000], 'Max': ['Sales Associate', 'Part-time', 20000]}, 2021: {'John': ['Managing Director', 'Full-time', 70000], 'Sally': ['HR Director', 'Full-time', 65000], 'Max': ['Sales Associate', 'Part-time', 25000]}, 2022: {'John': ['Managing Director', 'Full-time', 77500], 'Sally': ['HR Director', 'Full-time', 72500], 'Max': ['Sales Associate', 'Part-time', 32500]}}
    """
    # - YOUR CODE STARTS HERE -
    if year not in d:#checks if the year is already in the dictionary
        d[year] = {} #creats new empty dictionary for that year 
        for employee, details in d[year - 1].items():#iterates through the previous year employee details
            new_salary = details[2] + bonus #updates the salaray by adding the bonus
            d[year][employee] = [details[0], details[1], new_salary]#adds the updated details to the new year dictionary
    return d
    pass



def run_tests():
    import doctest

    # Run start tests in all docstrings
    #doctest.testmod(verbose=True)
    
    # Run start tests per function - Uncomment the next line to run doctest by function. Replace frequency with the name of the function you want to test
    doctest.run_docstring_examples(employee_update, globals(), name='LAB1',verbose=True)   

if __name__ == "__main__":
    run_tests()


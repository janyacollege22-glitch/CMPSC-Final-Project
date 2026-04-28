# HW1
# REMINDER: The work in this assignment must be your own original work and must be completed alone.

def get_path(file_name):
    """
        Returns a string with the absolute path of a given file_name located in the same directory as this script

        # Do not modify this function in any way

        >>> get_path('words.txt')   # HW1.py and words.txt located in HW1 folder
        'G:\My Drive\CMPSC132\HW1\words.txt'
    """
    import os
    target_path = os.path.join(os.path.dirname(__file__), file_name)
    return target_path

def rectangle(perimeter,area):
    """
        >>> rectangle(14, 10)
        5
        >>> rectangle(12, 5)
        5
        >>> rectangle(25, 25)
        False
        >>> rectangle(50, 100)
        20
        >>> rectangle(11, 5)
        False
        >>> rectangle(11, 4)
        False
    """
    #- YOUR CODE STARTS HERE
    if perimeter.is_integer() == False or area.is_integer() == False: #checks if the inputs are integers
        return False
    if perimeter % 2 != 0:#checks if the perimeter is odd
        return False
    for length in range(1, perimeter//2):#iterates through possible lengths
        width = (perimeter // 2) - length #calculates the width based on the length
        if length * width == area: #checks if the area matches
            if length >= width:#checks if length is greater than or equal to width
                return length
    return False #if no valid length is found
    pass


def to_decimal(oct_num):
    """
        >>> to_decimal(237) 
        159
        >>> to_decimal(35) 
        29
        >>> to_decimal(600) 
        384
        >>> to_decimal(420) 
        272
    """
    #- YOUR CODE STARTS HERE
    decimal_value = 0 #initializes the decimal value
    num_counter = 0 #initializes the counter for the position of the digit
    while oct_num > 0: #checks if the input is 0
        current_num = oct_num % 10 #gets the current digit
        decimal_value += current_num * (8 ** num_counter) #calculates the decimal value
        oct_num = oct_num // 10 #removes the last digit from the octal number
        num_counter += 1 #increments the position counter       
    return decimal_value
    pass



def has_hoagie(num):
    """
        >>> has_hoagie(737) 
        True
        >>> has_hoagie(35) 
        False
        >>> has_hoagie(-6060) 
        True
        >>> has_hoagie(-111) 
        True
        >>> has_hoagie(6945) 
        False
        >>> has_hoagie(123132)
        True
    """
    #- YOUR CODE STARTS HERE
    num = abs(num) #takes the absolute value of the number
    if num < 100: #checks if the number has less than 3 digits
        return False
    while num >= 3: #iterates through the digits of the number
        previous_digit = num % 10 #stores the current number
        num = num // 10 #removes the last digit
        current_digit = num // 10 % 10  #gets the digit every other place

        if current_digit == previous_digit: #checks if the two digits are equal to eachother
            return True
        else:
            return False
        num = num // 10 #removes the last digit
    pass


def is_identical(num_1, num_2):
    """
        >>> is_identical(51111315, 51315)
        True
        >>> is_identical(7006600, 7706000)
        True
        >>> is_identical(135, 765) 
        False
        >>> is_identical(2023, 20) 
        False
    """
    #- YOUR CODE STARTS HERE
    if num_1 == 0 and num_2 == 0: #if both numbers are 0, they are identical
           return True
    elif num_1 == 0 or num_2 == 0: #if one number is 0 and the other is not, they are not identical
           return False
    result_1 = 0#initializes the result for num_1
    result_2 = 0#initializes the result for num_2

    place_1 = 1#initializes the place value for both numbers
    place_2 = 1#initializes the place value for both numbers

    previous_place1 = -1#initializes the previous place value for both numbers
    previous_place2 = -1#initializes the previous place value for both numbers

    while num_1 > 0: #iterates through the digits of both numbers
        digit_1 = num_1 % 10 #gets the last digit of num_1

        if digit_1 != previous_place1:#checks if the digit is not a duplicate
            result_1 += digit_1 * place_1 #adds the digit to the result if it is not a duplicate
            place_1 *= 10 #increments the place value
            previous_place1 = digit_1 #updates the previous place value
        
        num_1 = num_1 // 10 #removes the last digit from num_1      
        
        
    while num_2 > 0:#iterates through the digits of both numbers
        digit_2 = num_2 % 10 #gets the last digit of num_2

        if digit_2 != previous_place2: #checks if the digit is not a duplicate
            result_2 += digit_2 * place_2 #adds the digit to the result if it is not a duplicate
            place_2 *= 10 #increments the place value
            previous_place2 = digit_2 #updates the previous place value

        num_2 = num_2 // 10 #removes the last digit from num_2
     
    if result_1 == result_2: #checks if the results are equal
        return True
    else:
        return False
    pass


def hailstone(num):
    """
        >>> hailstone(10)
        [10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(1)
        [1]
        >>> hailstone(27)
        [27, 82, 41, 124, 62, 31, 94, 47, 142, 71, 214, 107, 322, 161, 484, 242, 121, 364, 182, 91, 274, 137, 412, 206, 103, 310, 155, 466, 233, 700, 350, 175, 526, 263, 790, 395, 1186, 593, 1780, 890, 445, 1336, 668, 334, 167, 502, 251, 754, 377, 1132, 566, 283, 850, 425, 1276, 638, 319, 958, 479, 1438, 719, 2158, 1079, 3238, 1619, 4858, 2429, 7288, 3644, 1822, 911, 2734, 1367, 4102, 2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732, 866, 433, 1300, 650, 325, 976, 488, 244, 122, 61, 184, 92, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(7)
        [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(19)
        [19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    """
    #- YOUR CODE STARTS HERE
    sequence = [num] #initializes the sequence with the starting number
    while num != 1: #continues until the number reaches 1
        if num % 2 == 0: #checks if the number is even
            num = num // 2 #divides the number by 2
        else:
            num = 3 * num + 1 #multiplies the number by 3 and adds 1
        sequence.append(num) #adds the new number to the sequence
    return sequence
    pass



def overloaded_add(d, key, value):
    """
        Adds the key value pair to the dictionary. If the key is already in the dictionary, the value is made a list and the new value is appended to it.
        >>> d = {"Alice": "Engineer"}
        >>> overloaded_add(d, "Bob", "Manager")
        >>> overloaded_add(d, "Alice", "Sales")
        >>> d == {"Alice": ["Engineer", "Sales"], "Bob": "Manager"}
        True
    """
    #- YOUR CODE STARTS HERE
    if key in d: #checks if the key is already in the dictionary
        if type(d[key]) == list: #checks if the value is already a list
            d[key].append(value) #appends the new value to the list
        else:
            d[key] = [d[key], value] #creates a list with the old and new values
    else:
        d[key] = value #adds the key value pair to the dictionary
        return d
    
    pass


def by_department(d):
    """
        >>> employees = {
        ...    1: {'name': 'John Doe', 'position': 'Manager', 'department': 'Sales'},
        ...    2: {'position': 'Budget Advisor', 'name': 'Sara Miller', 'department': 'Finance'},
        ...    3: {'name': 'Jane Smith', 'position': 'Engineer', 'department': 'Engineering'},
        ...    4: {'name': 'Bob Johnson', 'department': 'Finance', 'position': 'Analyst'},
        ...    5: {'position': 'Senior Developer', 'department': 'Engineering', 'name': 'Clark Wayne'}
        ...    }

        >>> by_department(employees)
        {'Sales': [{'emp_id': 1, 'name': 'John Doe', 'position': 'Manager'}], 'Finance': [{'emp_id': 2, 'name': 'Sara Miller', 'position': 'Budget Advisor'}, {'emp_id': 4, 'name': 'Bob Johnson', 'position': 'Analyst'}], 'Engineering': [{'emp_id': 3, 'name': 'Jane Smith', 'position': 'Engineer'}, {'emp_id': 5, 'name': 'Clark Wayne', 'position': 'Senior Developer'}]}
    """
    #- YOUR CODE STARTS HERE
    department_dict = {} #initializes the department dictionary
    for emp_id, info in d.items(): #iterates through the employees
        department = info['department'] #gets the department of the employee
        emp_info = {'emp_id': emp_id, 'name': info['name'], 'position': info['position']} #creates a dictionary with the employee's information

        if department in department_dict: #checks if the department is already in the dictionary
            department_dict[department].append(emp_info) #appends the employee's information to the list
        else:
            department_dict[department] = [emp_info] #creates a new list with the employee's information
    return department_dict
    pass


def successors(file_name):
    """
        >>> expected = {'.': ['We', 'Maybe'], 'We': ['came'], 'came': ['to'], 'to': ['learn', 'have', 'make'], 'learn': [',', 'how'], ',': ['eat'], 'eat': ['some'], 'some': ['pizza'], 'pizza': ['and', 'too'], 'and': ['to'], 'have': ['fun'], 'fun': ['.'], 'Maybe': ['to'], 'how': ['to'], 'make': ['pizza'], 'too': ['!']}
        >>> returnedDict = successors('items.txt')
        >>> expected == returnedDict
        True
        >>> returnedDict['.']
        ['We', 'Maybe']
        >>> returnedDict['to']
        ['learn', 'have', 'make']
        >>> returnedDict['fun']
        ['.']
        >>> returnedDict[',']
        ['eat']
    """
    file_path = get_path(file_name)
    with open(file_path, 'r') as file:   
        contents = file.read()  # You might change .read() for .readlines() if it suits your implementation better
    # --- YOU CODE STARTS HERE
    if not contents: #checks if the file is empty
        return {}
    words = contents.split() #splits the contents into a list of words
    successor_dict = {} #initializes the successor dictionary
    for i in range(len(words) - 1): #iterates through the words
        current_word = words[i] #gets the current word
        next_word = words[i + 1] #gets the next word

        if current_word in successor_dict: #checks if the current word is already in the dictionary
            successor_dict[current_word].append(next_word) #appends the next word to the list
        else:
            successor_dict[current_word] = [next_word] #creates a new list with the next word
    return successor_dict
    pass




def addToTrie(trie, word):
    """
        The following dictionary represents the trie of the words "A", "I", "Apple":
            {'a' : {'word' : True, 'p' : {'p' : {'l' : {'e' : {'word' : True}}}}, 'i' : {'word' : True}}}}
       
        >>> trie_dict = {'a' : {'word' : True, 'p' : {'p' : {'l' : {'e' : {'word' : True}}}}, 'i' : {'word' : True}}} 
        >>> addToTrie(trie_dict, 'art')
        >>> trie_dict
        {'a': {'word': True, 'p': {'p': {'l': {'e': {'word': True}}}}, 'i': {'word': True}, 'r': {'t': {'word': True}}}}
        >>> addToTrie(trie_dict, 'moon') 
        >>> trie_dict
        {'a': {'word': True, 'p': {'p': {'l': {'e': {'word': True}}}}, 'i': {'word': True}, 'r': {'t': {'word': True}}}, 'm': {'o': {'o': {'n': {'word': True}}}}}
    """
    #- YOUR CODE STARTS HERE
    current_dict = trie #initializes the current dictionary to the trie
    for char in word: #iterates through the characters in the word
        if char not in current_dict: #checks if the character is not in the current dictionary
            current_dict[char] = {} #creates a new dictionary for the character
        current_dict = current_dict[char] #updates the current dictionary to the character's dictionary
    current_dict['word'] = True #marks the end of the word

    pass



def createDictionaryTrie(file_name):
    """        
        >>> trie = createDictionaryTrie("words.txt")
        >>> trie == {'b': {'a': {'l': {'l': {'word': True}}, 't': {'s': {'word': True}}}, 'i': {'r': {'d': {'word': True}},\
                     'n': {'word': True}}, 'o': {'y': {'word': True}}}, 't': {'o': {'y': {'s': {'word': True}}},\
                     'r': {'e': {'a': {'t': {'word': True}}, 'e': {'word': True}}}}}
        True
    """
    file_path = get_path(file_name)
    with open(file_path, 'r') as file:   
        contents = file.readlines()  # You might change .read() for .readlines() if it suits your implementation better 
    #- YOUR CODE STARTS HERE
    trie = {} #initializes the trie
    words = [line.strip() for line in contents] #splits the contents into a list of words
    for word in words: #iterates through the words
        addToTrie(trie, word.lower()) #adds the word to the trie
    return trie
    pass




def wordExists(trie, word):
    """
        >>> trie_dict = {'a' : {'word' : True, 'p' : {'p' : {'l' : {'e' : {'word' : True}}}}, 'i' : {'word' : True}}} 
        >>> wordExists(trie_dict, 'armor')
        False
        >>> wordExists(trie_dict, 'apple')
        True
        >>> wordExists(trie_dict, 'apples')
        False
        >>> wordExists(trie_dict, 'a')
        True
        >>> wordExists(trie_dict, 'as')
        False
        >>> wordExists(trie_dict, 'tt')
        False
    """
    #- YOUR CODE STARTS HERE
    current_dict = trie #initializes the current dictionary to the trie
    for char in word: #iterates through the characters in the word
        if char not in current_dict: #checks if the character is not in the current dictionary
            return False #returns False if the character is not found
        current_dict = current_dict[char] #updates the current dictionary to the character's dictionary
    return 'word' in current_dict #checks if the end of the word is marked

    pass




def run_tests():
    import doctest
    # Run start tests in all docstrings
    # doctest.testmod(verbose=True)
    
    # Run start tests per function - Uncomment the next line to run doctest by function. Replace rectangle with the name of the function you want to test
    doctest.run_docstring_examples(createDictionaryTrie, globals(), name='HW1',verbose=True)   

if __name__ == "__main__":
    run_tests()
#Assignment 3: Simplified Scrabble
#Laurine Aldairy
#260886886
import doctest

def create_board(x, y):
    """
    (int, int) --> list
    
    takes in two int and returns 2D list of x length
    with each list having y elements
    
    >>> create_board(4, 2)
    [[' ', ' '], [' ', ' '], [' ', ' '], [' ', ' ']]
    >>> create_board(2, 5)
    [[' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ']]
    >>> create_board(-1, 8)
    Traceback (most recent call last):
    ValueError: Inputs must be positive
    """
    #first raise appropriate errors
    if not ((x > 0) and (y > 0)):
        raise ValueError("Inputs must be positive")
    #create empty list
    new_list = []
    #iterate through x lists in new_list
    for sublist in range(x):
        #create sublist
        new_sublist = []
        #iterate through y elements in sublist
        for element in range(y):
            #add all y space characters
            new_sublist.append(' ')
        #add each sublist
        new_list.append(new_sublist)
    return new_list

def display_line(my_list):
    """
    (2d list) --> None
    
    takes in 2D list and prints line with four dashes
    representing each element in the first sublist,
    marked with a + on each end
    
    >>> b = [[' ', 'a', 'p', 'p', 'l', 'e'], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ']]
    >>> display_line(b)
      +-----------------------+
    >>> b = create_board(3, 3)
    >>> display_line(b)
      +-----------+
    >>> b = create_board(4, 2)
    >>> display_line(b)
      +-------+
    """
    #print first + character
    print("  +", end = "")
    #iterate through elements in the board
    for i in range(len(my_list[0])):
        #the last column
        if i == (len(my_list[0]) - 1):
            print("-" * 3 + "+")
        else:
            print("-" * 4, end = "")

def display_row(sublist):
    """
    (list) --> None
    
    takes in 1D list and prints the correct number of
    spaces, marked on each side with |
    
    >>> b = [" ", " ", " "]
    >>> display_row(b)
    |   |   |   |
    >>> b = ['a', 'p', 'p', 'l', 'e']
    >>> display_row(b)
    | A | P | P | L | E |
    >>> b = [" ", " ", " ", " ", " ", " "]
    >>> display_row(b)
    |   |   |   |   |   |   |
    """
    #print first line
    print("|", end = "")
    #iterate through elements in the list
    for element in sublist:
        print(" " + element.upper(), end = " |")

def display_board(my_list):
    """
    (2d list) --> None
    
    displays 2D list as board with one row per line
    
    >>> b = create_board(4, 5)
    >>> display_board(b)
        0   1   2   3   4
      +-------------------+
    0 |   |   |   |   |   |
      +-------------------+
    1 |   |   |   |   |   |
      +-------------------+
    2 |   |   |   |   |   |
      +-------------------+
    3 |   |   |   |   |   |
      +-------------------+
    >>> b = [[' ', 'a', 'p', 'p', 'l', 'e'], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ']]
    >>> display_board(b)
        0   1   2   3   4   5
      +-----------------------+
    0 |   | A | P | P | L | E |
      +-----------------------+
    1 |   |   |   |   |   |   |
      +-----------------------+
    2 |   |   |   |   |   |   |
      +-----------------------+
    >>> b = create_board(6, 6)
    >>> display_board(b)
        0   1   2   3   4   5
      +-----------------------+
    0 |   |   |   |   |   |   |
      +-----------------------+
    1 |   |   |   |   |   |   |
      +-----------------------+
    2 |   |   |   |   |   |   |
      +-----------------------+
    3 |   |   |   |   |   |   |
      +-----------------------+
    4 |   |   |   |   |   |   |
      +-----------------------+
    5 |   |   |   |   |   |   |
      +-----------------------+
    """
    #numbers along the top (columns)
    for i in range(len(my_list[0])):
        if i == 0:
            print(" " * 4 + "0", end = "")
        else:
            print(" " * 3 + str(i), end = "")
    #new line
    print()
    #print first line
    display_line(my_list)
    #iterate through elements in my_list (rows)
    for i in range(len(my_list)):
        #row number
        print(i, end = " ")
        #spaces
        display_row(my_list[i])
        #new line
        print()
        #bottom line
        display_line(my_list)

def get_vertical_axis(board, column):
    """
    (2d list, int) --> list
    
    takes in 2d list and column number and returns list
    of elements in column number of board
    
    >>> b = [['c', 'a', 't', ' '], [' ', 'a', 'r', 't'], [' ', ' ', 'a', ' '], [' ', ' ', 'i', ' '], [' ', ' ', 'n', ' ']]
    >>> get_vertical_axis(b, 2)
    ['t', 'r', 'a', 'i', 'n']
    >>> b = [[' ', 'a', 'p', 'p', 'l', 'e'], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ']]
    >>> get_vertical_axis(b, 4)
    ['l', ' ', ' ']
    >>> b = [['h', 'i', 'p',], ['i', ' ', ' '], ['y', ' ', ' '], ['a', ' ', ' ']]
    >>> get_vertical_axis(b, 0)
    ['h', 'i', 'y', 'a']
    """
    #create empty list
    vertical_list = []
    #iterate through lists for nth element
    for sublist in board:
        vertical_list.append(sublist[column])
    return vertical_list

def find_word(my_list, position):
    """
    (list, int) --> str
    
    takes in list of strings and int position, returns
    string of consecutive nonspace characters including
    character at given position, returns empty string
    if position is space character
    
    >>> find_word(['c', 'c', 'a', 't', ' ', 'a', 'p', 'p', 'l', 'e'], 2)
    'ccat'
    >>> find_word(['c', 'c', ' ', 't', '', 'a', 'p', 'ped', ' ', 'e'], 4)
    'tapped'
    >>> find_word(['c', ' ', 'l', 'i', 'ly', ' ', 'p', 'p', 'l', ' '], 3)
    'lily'
    """
    #create empty string
    new_word = ""
    #create counter variable
    counter = position
    #check if position holds space character
    if my_list[counter] == ' ':
        return new_word
    #check for space on left of position
    if counter != 0:
        while my_list[counter - 1] != ' ':
            counter -= 1
            if counter == 0:
                break
    #iterate through list
    while (counter != (len(my_list)) and (my_list[counter] != ' ')):
        new_word = new_word + my_list[counter]
        counter += 1
    return new_word

def available_space(my_list, position):
    """
    (list, int) --> int
    
    takes in list of str representing row/column and
    position, returns number of spaces in list starting
    at given position
    
    >>> available_space(['c', 'c', ' ', 't', ' ', 'a', 'p', 'p', 'l', 'e'], 2)
    2
    >>> available_space(['c', 'c', ' ', 't', ' ', ' ', ' ', ' ', 'l', 'e'], 4)
    4
    >>> available_space(['c', 'c', ' ', 't', ' ', ' ', ' ', ' ', 'l', 'e'], 8)
    0
    """
    #create counter variable
    counter = 0
    #initialise i with the given position
    i = position
    #iterate through list starting at position
    while i in range(len(my_list)):
        if my_list[i] == ' ':
            counter += 1
        i += 1
    return counter

def fit_on_board(my_list, my_word, position):
    """
    (list, str, int) --> bool
    
    takes in list of strings representing row or column
    on board, a string, and a given position
    returns True if the given string can fit in this
    place on the board, False otherwise
    
    >>> fit_on_board(['c', 'c', ' ', 't', ' ', ' ', ' ', ' ', 'l', 'e'], "apple", 3)
    False
    >>> fit_on_board([" ", " ", " ", " ", " ", " "], 'sand', 1)
    True
    >>> fit_on_board([" ", " ", " ", " ", "k", " "], 'ink', 0)
    True
    """
    spaces = available_space(my_list, position)
    if my_list[position] != ' ':
        return False
    return spaces >= len(my_word)

if __name__ == "__main__":
    doctest.testmod()

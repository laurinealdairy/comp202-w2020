#Assignment 2: Craps
#Laurine Aldairy
#260886886
#import doctest
import random

def one_roll():
    """
    () --> int
    
    takes no input and return random integer
    between 1 and 6 inclusive
    
    >>> random.seed(12)
    >>> one_roll()
    4
    >>> one_roll()
    3
    """
    result = random.randint(1, 6)
    return result

def dice_roll():
    """
    () --> int
    
    takes no input and returns sum of two dice rolls
    
    >>> random.seed(12)
    >>> dice_roll()
    7
    >>> dice_roll()
    11
    >>> dice_roll()
    9
    """
    #create roll variables
    roll1 = one_roll()
    roll2 = one_roll()
    return roll1 + roll2

def second_stage(n):
    """
    (int) --> int
    
    takes point as input and returns either point or 7
    
    >>> random.seed(5)
    >>> r = second_stage(6)
    8 9 12 11 5 8 3 4 6 
    >>> r
    6
    >>> random.seed(12)
    >>> r = second_stage(9)
    7 
    >>> r
    7
    >>> random.seed(34)
    >>> r = second_stage(10)
    8 6 3 7 
    >>> r
    7
    """
    #roll die
    next_roll = dice_roll()
    #iterate until n or 7 is reached
    while next_roll not in [n, 7]:
        print(next_roll, end = " ")
        next_roll = dice_roll()
    
    #if you reach n
    if next_roll == n:
        print(next_roll, end = " ")
        return n
    if next_roll == 7:
        print(next_roll, end = " ")
        return 7

def can_play(bank, bet):
    """
    (float, float) --> bool
    
    takes input of amount and bet and returns True
    if the player bets more than 0 and within what they
    own and False if not
    
    >>> can_play(0.0, 4.0)
    False
    >>> can_play(5.6, 3.2)
    True
    >>> can_play(2.4, -2.5)
    False
    >>> can_play(3.8, 4.0)
    False
    """
    if bank <= 0:
        return False
    elif bet <= 0:
        return False
    elif bet > bank:
        return False
    else:
        return True

def pass_line_bet(bank, bet):
    """
    (float, float) --> float
    
    takes in amount and bet and returns new amount
    of money the player has
    
    >>> random.seed(12)
    >>> pass_line_bet(14.0, 4.0)
    The first roll was 7
    You win!
    18.0
    >>> random.seed(34)
    >>> pass_line_bet(16.0, 2.0)
    The first roll was 8
    Roll again!
    6 3 7
    You Lose!
    14.0
    """
    #the initial roll of the dice
    initial_roll = dice_roll()
    print("A", initial_roll, "has been rolled.", end = " ")
    #if player wins on first roll
    if initial_roll in [7, 11]:
        print("You win!")
        return bank + bet
    #if player loses on first roll
    elif initial_roll in [2, 3, 12]:
        print("You lose!")
        return bank - bet
    #if game continues
    else:
        print("Roll again!")
        next_result = second_stage(initial_roll)
        print()
        if next_result == initial_roll:
            print("You win!")
            return bank + bet
        else:
            print("You Lose!")
            return bank - bet

def play():
    """
    (NoneType) --> NoneType
    
    retrieves two inputs from the user and displays
    a message if the user has insufficient funds to play
    and runs pass_line_bet if the user can play
    
    >>> random.seed(45)
    >>> play()
    Please enter your money here: 2
    How much do you want to bet? 1
    The first roll was 7
    You win!
    You now have 3.0
    >>> random.seed(678)
    >>> play()
    Please enter your money here: 14.0001
    How much do you want to bet? 3.44
    The first roll was 4
    Roll again!
    4
    You win!
    You now have 17.44
    >>> random.seed(1978)
    >>> play()
    Please enter your money here: 15
    How much do you want to bet? 7.2
    The first roll was 5
    Roll again!
    9 4 8 10 4 6 11 6 8 3 10 7 
    You Lose!
    You now have 7.8
    """
    #retrieve inputs from user
    player_bank = round(float(input("Please enter your money here: ")), 2)
    player_bet = round(float(input("How much do you want to bet? ")), 2)
    #check if they can play
    if can_play(player_bank, player_bet) == False:
        print("Insufficient funds. You cannot play.")
    else:
        new_bank = pass_line_bet(player_bank, player_bet)
        print("You now have", new_bank)

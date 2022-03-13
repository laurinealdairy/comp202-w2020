#Assignment 1 - Vending Machine
#written by Laurine Aldairy
#ID: 260886886

"""
TO DO
>>>rename and submit
"""

#numbers of each type of coin:
TOONIES = 1000 // 200
LOONIES = 500 // 100
QUARTERS = 500 // 25
DIMES = 300 // 10
NICKELS = 200 // 5
TOTAL = 2500

def display_welcome_menu():
    """
    NoneType --> NoneType
    
    Prints welcome message and 5 options with prices.
    returns no value
    """
    print("Welcome to the COMP 202 online vending machine.")
    print("Here are your options:")
    print("1. Candy bar $2.95")
    print("2. Cookies $3.90")
    print("3. Soda $4.00")
    print("4. Chips $3.90")
    print("5. No snacks for me today!")
    
#display_welcome_menu()

def get_snack_price(x):
    """
    (int) --> int
    
    retrieves input from user and returns price of
    object selected
    
    >>>get_snack_price(1)
    295
    >>>get_snack_price(2)
    390
    >>>get_snack_price(3)
    400
    >>>get_snack_price(4)
    390
    >>>get_snack_price(5)
    0
    >>>get_snack_price(-8)
    0
    """
    
    if (x == 1):
        return 295
    elif ((x == 2) or (x == 4)):
        return 390
    elif (x == 3):
        return 400
    else:
        return 0
    
#print(get_snack_price())

def get_num_of_coins(x, y, z):
    """
    (int, int, int) --> int
    
    takes in three inputs and calculates the number
    of a certain type of coin that can be used to
    pay up to the amount specified as input
    returns number of coins as integer
    
    >>>get_num_of_coins(500, 100, 8)
    5
    >>>get_num_of_coins(550, 25, 4)
    4
    >>> get_num_of_coins(123, 14, 16)
    8
    """
    if (x // y >= z):
        return z
    else:
        return x // y

#print(get_num_of_coins(234, 30, 20))
    
def compute_and_display_change(x):
    """
    (pos int) --> bool
    
    function takes input of change needed and displays
    breakdown of said change in toonies, loonies,
    quarters, dimes, and nickels, and returns boolean
    
    >> b = compute_and_display_change(185)
    Here is your change:
    toonies x 0
    loonies x 1
    quarters x 3
    dimes x 1
    nickels x 0
    >>> b
    True
    
    >> b = compute_and_display_change(70)
    Here is your change:
    toonies x 0
    loonies x 0
    quarters x 2
    dimes x 2
    nickels x 0
    >>> b
    True
    
    >>> b = compute_and_display_change(570)
    Here is your change:
    toonies x 2
    loonies x 1
    quarters x 2
    dimes x 2
    nickels x 0
    >>> b
    True
    
    >>> b = compute_and_display_change(2800)
    >>> b
    False
    
    >>> b = compute_and_display_change(114)
    >>> b
    False
    """
    
    if (x % 5 != 0):
        return False
    elif (x <= TOTAL):
        
        num_toonies = get_num_of_coins(x, 200, TOONIES)
        change_left = x - num_toonies * 200
        
        num_loonies = get_num_of_coins(change_left, 100, LOONIES)
        change_left = change_left - num_loonies * 100
        
        num_quarters = get_num_of_coins(change_left, 25, QUARTERS)
        change_left = change_left - num_quarters * 25
        
        num_dimes = get_num_of_coins(change_left, 10, DIMES)
        change_left = change_left - num_dimes * 10
        
        num_nickels = get_num_of_coins(change_left, 5, NICKELS)
        change_left = change_left - num_nickels * 5
        
        if (change_left == 0):
            print("Here is your change:")
            print("toonies x", num_toonies)
            print("loonies x", num_loonies)
            print("quarters x", num_quarters)
            print("dimes x", num_dimes)
            print("nickels x", num_nickels)
            
            return True
        else:
            return False
    else:
        return False
    
# b = compute_and_display_change(70)
#print(b)

def operate_machine():
    """
    NoneType --> NoneType
    
    takes no input and displays menu, then based on user
    choice either terminates or displays price
    user can input money and the machine returns change if
    it can and returns an error message and terminates if
    it cannot
    returns no value
    
    >>>operate_machine()
    Welcome to the COMP 202 virtual Vending Machine.
    Here are your options:
    1. Candy bar $2.95
    2. Cookies $3.90
    3. Soda $4.00
    4. Chips $3.90
    5. No snacks for me today!
    
    Please select your choice: 3
    
    The item of your choice costs 400 cents
    Enter your money: $4.0211111111
    
    You inserted 402 cents
    
    We do not accept pennies. Come by another time!
    
    >>> operate_machine()
    Welcome to the COMP 202 virtual Vending Machine.
    Here are your options:
    1. Candy bar $2.95
    2. Cookies $3.90
    3. Soda $4.00
    4. Chips $3.90
    5. No snacks for me today!
    
    Please select your choice: 3
    
    The item of your choice costs 400 cents
    Enter your money: $2.4999999
    
    You inserted 250 cents
    
    You do not have enough money. Come by another time!
    
    >>> operate_machine()
    Welcome to the COMP 202 virtual Vending Machine.
    Here are your options:
    1. Candy bar $2.95
    2. Cookies $3.90
    3. Soda $4.00
    4. Chips $3.90
    5. No snacks for me today!
    
    Please select your choice: 4
    
    The item of your choice costs 390 cents
    Enter your money: $7.55
    
    You inserted 755 cents
    You should receive back 365 cents
    
    Here is your change:
    toonies x 1
    loonies x 1
    quarters x 2
    dimes x 1
    nickels x 1
    
    It was a pleasure doing business with you!
    
    >>> operate_machine()
    Welcome to the COMP 202 virtual Vending Machine.
    Here are your options:
    1. Candy bar $2.95
    2. Cookies $3.90
    3. Soda $4.00
    4. Chips $3.90
    5. No snacks for me today!
    
    Please select your choice: 4
    
    The item of your choice costs 390 cents
    Enter your money: $30.90
    
    You inserted 3090 cents
    You should receive back 2700 cents
    
    The machine does not have enough coins for your change.
    Come by another time!
    """
    display_welcome_menu()
    
    #retrieve selection from user
    order = int(input("What would you like to order? "))
    price = get_snack_price(order)
    
    if (price != 0):
        print("\n")
        print("Your item will cost", price, "cents.")
        
        money_inserted = int(round(float(input("Enter your money (in dollars): ")), 2) * 100)
        
        print("\n")
        print("You inserted", money_inserted, "cents.")
        
        if (money_inserted % 5 == 0):
            if (money_inserted < price):
                print("You do not have enough money. Come by another time!")
            else:
                change = money_inserted - price
                print("You should receive back", change, "cents.")
                
                if (change == 0):
                    print("You paid exactly! The machine will not give you change.")
                elif (change <= TOTAL):
                    print("\n")
                    compute_and_display_change(change)
                    
                    print("\n")
                    print("It was a pleasure doing business with you!")
                else:
                    print("\n")
                    print("The machine does not have enough coins for your change.")
                    print("Come by another time!")
        else:
            print("\n")
            print("We do not accept pennies. Come by another time!")
    else:
        print("\n")
        print("Nothing for you today. Thanks for stopping by!")

if __name__ == "__main__":
    operate_machine()

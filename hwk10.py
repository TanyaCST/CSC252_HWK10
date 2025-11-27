# Name:  - Tanya Chen & Emily Wang
# Peers:  - N/A
# References:  - https://www.geeksforgeeks.org/dsa/understanding-the-coin-change-problem-with-dynamic-programming/
from random import randint

### Part 1: Lumber Mill

def lumberSelection(prices:list[float], n:int) -> float:
    """ Given the length of a board, return the optimal price we can earn 
    	based on the list of price of boards with different length
    :param prices: (list[float]) a list of prices of boards with different length (represented by index)
					index 0 = length 1
    :param n: (int) the total length of board we will cut
    : return: (float) the optimal price 
    
    >>> lumber_prices = [0.25, 1.45, 0, 3.58, 0, 4.4, 0, 5.18, 0, 6.58, 0, 8.28]
    >>> print("The max value for 3 feet is $" + str(lumberSelection(lumber_prices, 3)))
    The max value for 3 feet is $1.7
    """
    # The index starts from 0, so the total length is n+1 so that the index matches to length
    perm:list[float] = [0.0]*(n+1)
    
	# Keep track of the best price we can obtain
    max_price = 0.0

	# Loop through perm in order to add every max price into corresponding index
    for i in range(n+1):
        # Set 0 with 0
        if i == 0:
            perm[i] = 0.0
        else:
			# Loop through each available length based on current index
            length = 1
            while length <= i and length <= len(prices):
                current_price = prices[length-1] + perm[i-length]
        
                # Find the maximum between max stored and current price
                if max_price < current_price:
                    max_price = current_price
                
				# Update length
                length += 1
                
			# Update the table
            perm[i] = max_price
                
    return perm[n]

### Part 2: Cash Register
reversed_denomination = [100, 50, 20, 10, 5, 2, 1] 

def find_combo(remaining: int, index: int, combo_str: str) -> None: 
    """ Prints of all the combinations of dollars to use for a specific value
    :param remaining: (int) The remining amount of dollar need to be determined with combos of dollars
    :param index: (int) The index of the corresponding dollar in reversed_denomination 
    :param combo_str: (int) The combination of dollars 
    >>> 
    """
    if remaining == 0: 
        print(combo_str) 
        return 
    if index >= len(reversed_denomination): 
        return 
    
    d = reversed_denomination[index] 
    max_count = remaining // d 

    for c in range(max_count, -1, -1): #stops at -1, also needs to multiply 0
        if c > 0: 
            new_combo_str = combo_str + str(c) + "*$" + str(d) + " " 
        else: 
            new_combo_str = combo_str 

        find_combo(remaining - c * d, index + 1, new_combo_str) 


def calcPermutations(val: int) -> None:
    """Prints of all the combinations of dollars to use for a specific value
    :param val: (int) The value need to be determined with combos of dollars
    >>> calcPermutations(4)
    2*$2 
    1*$2 2*$1 
    4*$1 

    """
    # I know we should not use a helper function like this
    # But I have no idea how to use recursion by just keeping track of the value
    find_combo(val, 0, "")
    print()



def new_array(size: int) -> list[int]:
    """ Creates a new array of a given size.
    :param size: (int) the number of 0s you want in the array
    :return : (list) the array with zeros 
    >>> new_array(3)
    [0,0,0]
    """
    L = [0] * size
    return L

def getNumberOfWays(change_amount:int, bill_list:list[int]) -> int:
    """ This calculates the number of combinations we can get for this change
    :param change_amount: (int) The value you want to find the combinations of dollars
    :param bill_list: (list[int]) A list of possible dollar values
    :return: (int) The number of combinations we can get for this change_amount
    >>> bills = [1, 2, 5, 10, 20, 50, 100]
    >>>  print(getNumberOfWays(4, bills))
    3
    """
    ways = new_array(change_amount + 1)

    ways[0] = 1

    for i in range(len(bill_list)):
        for j in range(len(ways)):
                if (bill_list[i] <= j):
                    ways[j] += ways[(int)(j - bill_list[i])]
    
    return ways[change_amount]
        
    


def main():
    """ This function drives the program and will call each of your functions.
    """
    lumber_prices = [0.25, 1.45, 0, 3.58, 0, 4.4, 0, 5.18, 0, 6.58, 0, 8.28]
    size = randint(1,len(lumber_prices))
    print("The max value for " + str(size) + " feet is $" + str(lumberSelection(lumber_prices, size)))
    
	# More tests
    # print("The max value for 1 feet is $" + str(lumberSelection(lumber_prices, 1)))
    # print("The max value for 2 feet is $" + str(lumberSelection(lumber_prices, 2)))
    # print("The max value for 3 feet is $" + str(lumberSelection(lumber_prices, 3)))
    # print("The max value for 4 feet is $" + str(lumberSelection(lumber_prices, 4)))
    # print("The max value for 5 feet is $" + str(lumberSelection(lumber_prices, 5)))
    # print("The max value for 6 feet is $" + str(lumberSelection(lumber_prices, 6)))
    # print("The max value for 7 feet is $" + str(lumberSelection(lumber_prices, 7)))
    # print("The max value for 8 feet is $" + str(lumberSelection(lumber_prices, 8)))
    # print("The max value for 9 feet is $" + str(lumberSelection(lumber_prices, 9)))
    # print("The max value for 10 feet is $" + str(lumberSelection(lumber_prices, 10)))
    # print("The max value for 11 feet is $" + str(lumberSelection(lumber_prices, 11)))
    # print("The max value for 12 feet is $" + str(lumberSelection(lumber_prices, 12)))
    
    bills = [1, 2, 5, 10, 20, 50, 100]
    change = randint(1, 100)
    print("For $" + str(change) + " there are " + str(getNumberOfWays(change, bills)) + " combinations.")

    print(getNumberOfWays(4, bills))
    calcPermutations(4)
    # calcPermutations(12)
    

if __name__ == '__main__': 
    main()


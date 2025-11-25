# Name:  - Tanya Chen & Emily Wang
# Peers:  - names of CSC252 students who you consulted or ``N/A'' <br>
# References:  - https://www.geeksforgeeks.org/dsa/understanding-the-coin-change-problem-with-dynamic-programming/
# from random import randint

### Part 1: Lumber Mill
# def lumberSelection(prices:list, n:int) -> float:
# 	return 0.0

### Part 2: Cash Register
reversed_denomination = [100, 50, 20, 10, 5, 2, 1] 

def find_combo(remaining: int, index: int, combo_str: str) -> None: 
    if remaining == 0: 
        print(combo_str) 
        return 
    if index >= len(reversed_denomination): 
        return 
    
    d = reversed_denomination[index] 
    max_count = remaining // d 

    for c in range(max_count, -1, -1): #stops at -1, works at 0 
        if c > 0: 
            new_combo_str = combo_str + str(c) + "*$" + str(d) + " " 
        else: 
            new_combo_str = combo_str 

        find_combo(remaining - c * d, index + 1, new_combo_str) 


def calcPermutations(val: int) -> None:
    # I know we should not use a helper function like this
    # But I have no idea how to use recursion by just keeping track of the value
    find_combo(val, 0, "")
    print()

def new_array(size: int):
    """ Creates a new array of a given size.
    :param size: (int) the number of 0s you want in the array
    :return : (list) the array with zeros 
    >>> new_array(3)
    [0,0,0]
    """
    L = [0] * size
    return L

def getNumberOfWays(change_amount:int, bill_list:list[int]) -> int:
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
    # lumber_prices = [0.25, 1.45, 0, 3.58, 0, 4.4, 0, 5.18, 0, 6.58, 0, 8.28]
    # size = randint(1,len(lumber_prices))
    # print("The max value for " + str(size) + " feet is $" + str(lumberSelection(lumber_prices, size)))
    
    bills = [1, 2, 5, 10, 20, 50, 100]
    # change = randint(1, 100)
    # print("For $" + str(change) + " there are " + str(getNumberOfWays(6, bills)) + " combinations.")

    print(getNumberOfWays(4, bills))
    # print(find_smaller(4))
    #calcPermutations(4)
    # calcPermutations(12)

if __name__ == '__main__': 
    main()


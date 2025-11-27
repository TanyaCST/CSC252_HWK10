# Name:  - Tanya Chen & Emily Wang
# Peers:  - names of CSC252 students who you consulted or ``N/A'' <br>
# References:  - URL of resources used <br>
from random import randint

### Part 1: Lumber Mill

def lumberSelection(prices:list[float], n:int) -> float:
    """ Given the length of a board, return the optimal price we can earn 
    	based on the list of price of boards with different length
    :param prices: (list[float]) a list of prices of boards with different length (represented by index)
					index 0 = length 1
    :param n: (int) the total length of board we will cut
    : return: (float) the optimal price 
    """
    # The index starts from 0, so the total length is n+1 so that the index matches to length
    perm:list[float] = [0.0]*(n+1)

	# Loop through perm in order to add every max price into corresponding index
    for i in range(n+1):
        # Set 0 with 0
        if i == 0:
            perm[i] = 0.0
        else:
			# Keep track of the best price we can obtain
            max_price = 0.0
            
			# Loop through each available length based on current index
            length = 1
            while length <= i and length <= len(prices):
                current_price = prices[i-1] + perm[i-length]
        
                # Find the maximum between max stored and current price
                if max_price < current_price:
                    max_price = current_price
                
				# Update length
                length += 1
                
				# Update the table
                perm[i] = max_price
                
    return perm[n]

### Part 2: Cash Register
def calcPermutations(val:int) -> None:
    pass

def getNumberOfWays(change_amount:int, bill_list:list) -> int:
	return 0



def main():
    """ This function drives the program and will call each of your functions.
    """
    lumber_prices = [0.25, 1.45, 0, 3.58, 0, 4.4, 0, 5.18, 0, 6.58, 0, 8.28]
    size = randint(1,len(lumber_prices))
    print("The max value for " + str(size) + " feet is $" + str(lumberSelection(lumber_prices, size)))
    
    bills = [1, 2, 5, 10, 20, 50, 100]
    change = randint(1, 100)
    print("For $" + str(change) + " there are " + str(getNumberOfWays(6, bills)) + " combinations.")

if __name__ == '__main__': 
    main()


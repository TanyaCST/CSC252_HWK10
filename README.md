# Homework Assignment 10: Dynamic Programming
Note: This homework assignment should be submitted individually or as a pair. If working with a partner, both partners must submit identical files.

Start all assignments in this class at least four days before the deadline. This will enable you to get help when needed and ensure your success in this course.

Please read the entire assignment description prior to starting any part.

## Goal
The goal of this assignment is to apply dynamic programming and see different configurations for how to build a dynamic programming table.

## Instructions
See individual parts.

### Part 1: Lumber Mill
After trees have been debarked and sliced into planks, they are brought into the lumber mill. The first machine (called the Wood Eye and Optimizer Saw or WEO saw) uses computer vision to find the knots in the wood to establish the best parts of the board to sell for a premium price. For a given board length, your job is to automate the part of the WEO saw that picks what size(s) to saw the boards into for sale.

Boards are 2" by 4" (inch) and of various lengths. Prices vary based on length. For example, a 1' (foot or 12") board can be sold for $0.25, see the rest of the prices below.

Length	Price
1	$0.25
2	$1.45
4	$3.58
6	$4.40
8	$5.18
10	$6.58
12	$8.28


#### Question #1
(a) Write out all the permutations of board you can create with a 12' (twelve foot) board.
(b) What is the maximum amount of money you can acquire for a 12' (twelve foot) board?

#### Question #2
(a) Take the last digit of your 99 number. Write out all the combinations for a board of that length in feet. If your last number is 0, use the value ten. (If you are working in a pair, both partners should complete this step individually with their respective 99 numbers and add it to the shared file.)
(b) What is the maximum amount of money you can acquire for this value?

#### Programming
Use dynamic programming to implement the lumberSelection(prices:list, n:int) -> float function. The function should return the best obtainable price for a board of length n and prices[] as prices of different lengths.

### Part 2: Cash Register
Recall in class we discussed a cash register, see here for a description. We are going to figure out all the permutations to make change in bills for the clerk. For this question, let us assume American paper currency comes in seven denominations: $1, $2, $5, $10, $20, $50, and $100.

For example, if the customers change is $6 dollars, the cash register could issue any of the five possible combinations of bills:

1 x $5 + 1 x $1
3 x $2
2 x $2 + 2 x $1
1 x $2 + 4 x $1
6 x $1
#### Question #3
Write out all the permutations of change for each of the following amounts:
(a) $4
(b) $12

#### Programming
Write the function calcPermutations(val:int) -> None that prints all the permutations of change for the cash register problem, given an initial value val. Note: if you complete this step first you can copy the output of your function to answer the questions above.

Use dynamic programming to implement the getNumberOfWays(change_amount:int, bill_list:list) -> int function. The function should return the number of different combination of bills that are possible given the values of the customers change in bills (change_amount) and a list of possible bills (bill_list).

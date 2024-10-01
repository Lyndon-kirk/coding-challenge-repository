# Problem Set 2: Valid Parentheses
## Problem Description
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is
valid. 
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
## Solution Overview
1. A function called isValid is created to accept a string as parameter.
2. An empty list called stack is created to contain all opening symbols in the string.
3. A dictionary with keys of closing brackets is initialized with their opening brackets as values.
4. The function iterates through each char or symbol of the string.
5. If the symbol is a opening, then it is added to the list named stack.
6. If the symbol is closing, then the stack is popped and checked in the dictionary if the value matches.
7. If the value matches then the iteration continues until nothing is left in the stack.
8. If the stack is empty it means the closing symbols are matched with the opening ones perfectly.
9. If the last symbol popped in the stack is not equal to the symbol in the current iteration based on the dictionary, the whole function returns false.
## Instructions to Run the Code
The code may be run using VS Code.

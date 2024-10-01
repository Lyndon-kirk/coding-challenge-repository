# Problem Set 1: Palindrome Pairs
## Problem Description
Find all pairs of distinct indices (i, j) in a given list so that
the concatenation of the two words, i.e., words[i] + words[j], forms a palindrome
## Solution Overview
1.Create a function to check if the reverse of the string forms a palindrome
2.Create another function that will accept list as a parameter
3.Create a dictionary to hold the index that maps to the words in the list for easier searching of palindrome pairs
4.Each word in the list is split in every iteration to check the reverse of each part if it is in the dictionary.
5.If split is in the dictionary and the index in the dictionary is not equal to the iterator, then the pair of indices is added to the result.
## Instructions to Run the Code
The code may be run in VS Code.

# Problem Set 3: Longest Increasing Subsequence
## Problem Description
Given an unsorted array of integers, find the length of the longest increasing subsequence.
## Solution Overview
1. A function named lenghtOfLIS that accepts a list as parameter is created.
2. If the list is empty it returns 0 as length.
3. A tails list is created to contain the smallest possible values for increasing subsequence.
4. A binary search in the tails array for each number is performed to find the position where the value can be inserted.
5. If the current number in the iteration is greater than the last number in the list then it appends it.
6. If it fits in the middle, replace the value in tails to ensure the smallest possible value for the length of subsequence.
7. After all the iterations the length of the tails list is returned.
## Instructions to Run the Code
The code may be run using VS Code.

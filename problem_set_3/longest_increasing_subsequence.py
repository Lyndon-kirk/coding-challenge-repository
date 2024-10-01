def lengthOfLIS(nums):
    #return 0 if empty
    if not nums:
        return 0
    
    # to store increasing subsequences of different lengths
    tails = [2]
    for num in nums:
        # Use binary search to find the insertion point of the current number
        left = 0
        right = len(tails)
        while left < right:
            mid = (left + right) // 2
            if tails[mid] < num:
                left = mid + 1
            else:
                right = mid
        
        # If num is larger than all elements in tails, append it
        if left == len(tails):
            tails.append(num)
        else:
            #  replace the existing value if not
            tails[left] = num
            
    [ 2, 5, 7, 10, 20]
    # The length of LIS
    return len(tails)

# Example 
inputNumbers1 = [10, 9, 2, 5, 3, 7, 101, 18]
inputNumbers2 = [ 2, 5, 7, 10, 20]
result1 = lengthOfLIS(inputNumbers1)
result2 = lengthOfLIS(inputNumbers2)
print(result1)  #Output: 4
print(result2) #Output: 5

ques-Given an array arr[] denoting heights of n towers and a positive integer k.

For each tower, you must perform exactly one of the following operations exactly once.

Increase the height of the tower by k
Decrease the height of the tower by k
Find out the minimum possible difference between the height of the shortest and tallest towers after you have modified each tower

class Solution:
    def getMinDiff(self, arr, k):
        n = len(arr)
        if n == 1:
            return 0
        
        arr.sort()
        
        # Initial difference
        ans = arr[-1] - arr[0]
        
        # Smallest and largest after modification
        small = arr[0] + k
        big = arr[-1] - k
        
        if small > big:
            small, big = big, small
        
        for i in range(1, n):
            
            # If decreasing makes height negative, skip
            if arr[i] - k < 0:
                continue
            
            min_height = min(small, arr[i] - k)
            max_height = max(big, arr[i-1] + k)
            
            ans = min(ans, max_height - min_height)
        
        return ans

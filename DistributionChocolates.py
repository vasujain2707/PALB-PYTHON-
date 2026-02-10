  QUES-Given an array arr[] of positive integers, where each value represents the number of 
chocolates in a packet. Each packet can have a variable number of chocolates. There 
are m students, the task is to distribute chocolate packets among m students such that - 
      i. Each student gets exactly one packet. 
     ii. The difference between maximum number of chocolates given to a student and 
minimum number of chocolates given to a student is minimum and return that 
minimum possible difference.


class Solution:
    def findMinDiff(self, arr, m):
        n = len(arr)
        
        # Edge case
        if m == 0 or n == 0 or m > n:
            return 0
        
        # Step 1: Sort the array
        arr.sort()
        
        # Step 2: Initialize minimum difference
        min_diff = float('inf')
        
        # Step 3: Check all windows of size m
        for i in range(n - m + 1):
            diff = arr[i + m - 1] - arr[i]
            min_diff = min(min_diff, diff)
        
        return min_diff

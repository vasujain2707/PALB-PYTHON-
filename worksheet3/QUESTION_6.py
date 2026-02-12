QUES-Given an array arr[] of integers, calculate the median.

class Solution:
    def find_median(self, arr):
        arr.sort()
        n = len(arr)
        
        if n % 2 == 1:   # Odd length
            return arr[n // 2]
        else:            # Even length
            return (arr[n // 2 - 1] + arr[n // 2]) / 2

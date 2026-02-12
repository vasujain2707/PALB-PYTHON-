QUES- Given an array arr and a number k. One can apply a swap operation on the array any 
number of times, i.e choose any two index i and j (i < j) and swap arr[i] , arr[j] . Find 
the minimum number of swaps required to bring all the numbers less than or equal 
to k together, i.e. make them a contiguous subarray

class Solution:
    def minSwap(self, arr, k):
        n = len(arr)
        
        # Step 1: Count elements <= k
        good = 0
        for num in arr:
            if num <= k:
                good += 1
        
        # Step 2: Count bad elements in first window
        bad = 0
        for i in range(good):
            if arr[i] > k:
                bad += 1
        
        ans = bad
        
        # Step 3: Slide the window
        left = 0
        for right in range(good, n):
            
            # Remove left element from window
            if arr[left] > k:
                bad -= 1
            left += 1
            
            # Add right element to window
            if arr[right] > k:
                bad += 1
            
            ans = min(ans, bad)
        
        return ans

    

